import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Patch

# 1. APPLY STYLE FIRST
# This must happen before setting custom fonts, or it will overwrite them.
plt.style.use('seaborn-v0_8-whitegrid')

# 2. THEN SET FONTS
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'

# 1. Load Data
df = pd.read_csv("EngChain_Model_Comparison_Level.csv")

# 2. Select Narrative Models
selected_models = [
    "gpt-5-mini",           
    "gemini-3-pro-preview", 
    "deepseek-reasoner",    
    "meta-llama-3.1-70b"    
]

display_names = {
    "gpt-5-mini": "GPT-5 Mini",
    "gemini-3-pro-preview": "Gemini 3 Pro",
    "deepseek-reasoner": "DeepSeek R1",
    "meta-llama-3.1-70b": "Llama 3.1 70B"
}

# 3. Process Data
df_filtered = df[df['model'].isin(selected_models)].copy()
df_filtered['level'] = df_filtered['level'].astype(str).str.capitalize()
level_order = ["Easy", "Intermediate", "Advanced"]

# Pivot
pivot_df = df_filtered.pivot(index='model', columns='level', values='final_answer_match') * 100
pivot_df = pivot_df[level_order] 
pivot_df = pivot_df.reindex(selected_models) 

# 4. Setup Plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 8))

# X positions
x = np.arange(len(selected_models))
width = 0.22 

# 5. Define Styles
color_palettes = {
    "gpt-5-mini": [
        "#82b8e8",
        "#b0d4ed",
        "#d0e6f5"
    ],
    "gemini-3-pro-preview": [
        "#85ca87",
        "#b0e0aa",
        "#d3f0c8"
    ],
    "deepseek-reasoner": [
        "#b0a8d9",
        "#d0c9e6",
        "#e6e2f3"
    ],
    "meta-llama-3.1-70b": [
        "#a8a8a8",
        "#d0d0d0",
        "#e6e6e6"
    ]
}

# Patterns
patterns = ["", "///", "..."] 

# 6. Plot Bars
offsets = [-width, 0, width] 

for i, level in enumerate(level_order):
    values = pivot_df[level].values
    
    current_colors = [color_palettes[m][i] for m in selected_models]
    
    bars = ax.bar(x + offsets[i], values, width, 
                  label=level, 
                  color=current_colors, 
                  hatch=patterns[i],
                  edgecolor='#a8a8a8', linewidth=0.7, alpha=1.0)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1.5,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=20, fontweight='bold', color='black', fontname='Times New Roman')

# 7. Formatting
ax.set_xticks(x)
ax.set_xticklabels([display_names[m] for m in selected_models], fontsize=26, fontweight='bold', fontname='Times New Roman')
ax.set_ylabel("Final Answer Accuracy (%)", fontsize=20, fontweight='bold', fontname='Times New Roman')
ax.set_ylim(0, 100)

# Grid and axes
ax.grid(axis='y', linestyle='--', alpha=0.4, linewidth=0.8, color='gray', zorder=0)
ax.grid(axis='x', alpha=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Axis ticks styling
ax.tick_params(axis='y', colors='black')
ax.tick_params(axis='x', colors='black')

# Enhanced Custom Legend
legend_elements = [
    Patch(facecolor='#4a90d9', edgecolor='black', linewidth=1.5, hatch='', label='Easy'),
    Patch(facecolor='#7db3e8', edgecolor='black', linewidth=1.5, hatch='///', label='Intermediate'),
    Patch(facecolor='#b8d9f5', edgecolor='black', linewidth=1.5, hatch='...', label='Advanced')
]

legend = ax.legend(handles=legend_elements, title="Difficulty Level", 
                   loc='upper right', frameon=True, fontsize=14,
                   fancybox=False, shadow=False, borderpad=1.2,
                   edgecolor='black', framealpha=1, facecolor='white',
                   title_fontsize=16,
                   prop={'family': 'Times New Roman', 'size': 14})
legend.get_title().set_fontweight('bold')
legend.get_title().set_fontname('Times New Roman')
legend.get_frame().set_linewidth(1.5)

plt.tight_layout()
plt.savefig('Level_Performance_Bar.pdf', dpi=300, bbox_inches='tight')
plt.show()
