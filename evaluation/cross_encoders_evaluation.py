# Cross Encoders
import torch
import numpy as np
from typing import Dict, Any

from engineering_parser import extract_steps
from sentence_transformers import CrossEncoder
from rouge_score import rouge_scorer
from bert_score import BERTScorer


# Retry and Timeout constants
MAX_RETRIES = 5
INITIAL_BACKOFF = 2  # seconds
REQUEST_TIMEOUT = 120 # seconds (2 minutes)


#  Model & Scorer Initialization 
print("Initializing evaluation models...")
CROSS_ENCODER = CrossEncoder('cross-encoder/stsb-roberta-large')
ROUGE_SCORER = rouge_scorer.RougeScorer(['rouge2', 'rougeL', 'rougeLsum'], use_stemmer=True)
BERT_SCORER = BERTScorer(model_type='allenai/longformer-base-4096', 
                         device='cuda' if torch.cuda.is_available() else 'cpu')
print("Evaluation models initialized.")


def safe_bert_score(gt: str, pred: str) -> float:
    """ A wrapper for BERTScore to handle potential errors and empty strings. """
    if not all(isinstance(s, str) for s in [gt, pred]) or not gt.strip() or not pred.strip():
        return 0.0
    try:
        _, _, f1 = BERT_SCORER.score([pred], [gt])
        return f1.item()
    except Exception as e:
        print(f"Warning: BERTScore failed with error: {e}")
        return 0.0


def evaluate_trace_eng(gt_solution: str, pred_generation: str) -> Dict[str, Any]:
    """
    Compares a ground-truth engineering solution with a model's generation.
    """

    # Handle empty inputs gracefully
    if not gt_solution or not pred_generation:
        return {
            'error': 'Input solution or generation is empty.', 
            'recall': 0, 
            'precision': 0, 
            'step_f1': 0, 
            'final_answer_match': 0, 
            'rouge2': 0, 
            'rougeL': 0, 
            'rougeLsum': 0, 
            'bertscore': 0
        }
    
    # Compute textual similarity metrics
    rouge_scores = ROUGE_SCORER.score(gt_solution, pred_generation)
    bertscore = safe_bert_score(gt_solution, pred_generation)

    # Extract structured reasoning steps and final answers
    gt_steps, gt_step_answers, gt_final_answer = extract_steps(gt_solution)
    pred_steps, pred_step_answers, pred_final_answer = extract_steps(pred_generation)
    final_answer_match = 0
    FINAL_ANSWER_TOLERANCE = 0.01

    # Final answer comparison with tolerance
    if gt_final_answer is not None and pred_final_answer is not None:
        if abs(gt_final_answer) > 1e-9:
            if abs(gt_final_answer - pred_final_answer) / abs(gt_final_answer) < FINAL_ANSWER_TOLERANCE:
                final_answer_match = 1
        elif abs(gt_final_answer - pred_final_answer) < 1e-9:
            final_answer_match = 1

    # Step-level similarity and recall/precision computation
    recall, precision = 0, 0
    if gt_steps and pred_steps:
        sentence_pairs = [[gt_step, pred_step] for gt_step in gt_steps for pred_step in pred_steps]
        scores = CROSS_ENCODER.predict(sentence_pairs, show_progress_bar=False)
        semantic_similarity = np.array(scores).reshape(len(gt_steps), len(pred_steps))

        # Numeric correctness check
        numeric_correctness = np.zeros((len(gt_steps), len(pred_steps)))
        STEP_ANSWER_TOLERANCE = 0.02

        for i, gt_ans in enumerate(gt_step_answers):
            if gt_ans is None: continue
            for j, pred_ans in enumerate(pred_step_answers):
                if pred_ans is None: continue
                if abs(gt_ans) > 1e-9:
                    if (abs(gt_ans - pred_ans) / abs(gt_ans)) < STEP_ANSWER_TOLERANCE:
                        numeric_correctness[i, j] = 1
                elif abs(gt_ans - pred_ans) < 1e-9:
                    numeric_correctness[i, j] = 1
        
        # Combine semantic and numeric correctness matrices
        combined_matrix = np.multiply(semantic_similarity, numeric_correctness)
        SIMILARITY_THRESHOLD = 0.7
        best_matches_scores = np.max(combined_matrix, axis=1)
        
        # Compute recall and precision based on matched steps
        recall = float(np.sum(best_matches_scores > SIMILARITY_THRESHOLD) / len(gt_steps))
        precision = float(np.sum(np.max(combined_matrix, axis=0) > SIMILARITY_THRESHOLD) / len(pred_steps))

    # Compute step-level F1 score
    step_f1 = 0
    if recall + precision > 0:
        step_f1 = 2 * (recall * precision) / (recall + precision)
    
    # Final result dictionary
    return {
        'recall': recall, 
        'precision': precision, 
        'step_f1': step_f1,
        'final_answer_match': final_answer_match, 
        'rouge2': rouge_scores['rouge2'].fmeasure,
        'rougeL': rouge_scores['rougeL'].fmeasure, 
        'rougeLsum': rouge_scores['rougeLsum'].fmeasure,
        'bertscore': bertscore
    }
