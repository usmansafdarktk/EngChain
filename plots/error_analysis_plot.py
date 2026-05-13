from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. APPLY STYLE FIRST
# This ensures grid lines and background settings are loaded before our custom font overrides
plt.style.use('seaborn-v0_8-whitegrid')

# 2. THEN SET FONTS (Force Times New Roman Globally)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'

# 3. DATA PREPARATION
data = {
    'Category': ['Frontier Models', 'General Open Purpose Models', 'Math Enhanced Models'],
    'Alternative Correct': [97.2, 58.5, 72.0],  # Bottom
    'Calculation Error':   [1.0,  12.5,  8.0],  # Middle
    'Conceptual Error':    [1.8,  29.0, 20.0]   # Top
}

df = pd.DataFrame(data)
df = df.set_index('Category')

# 4. PLOT SETUP
fig, ax = plt.subplots(figsize=(10, 7))

# COLORS: Brighter Green, Mustard, Warm Brown
colors = ['#b3dda0', '#d9b86c', '#a87c5b']
patterns = ['', '//', '..']

# 5. CREATE STACKED BARS (3-Pass Method)
bottom = np.zeros(len(df))

for i, col in enumerate(df.columns):
    
    # PASS 1: Base Fill Color (No Edge, No Hatch)
    bars = ax.bar(
        df.index, df[col], bottom=bottom, color=colors[i],
        edgecolor='none', width=0.5, label=col, zorder=2
    )
    
    # PASS 2: Pattern Overlay (Light Gray Hatch)
    if patterns[i]:
        ax.bar(
            df.index, df[col], bottom=bottom, fill=False,
            hatch=patterns[i], edgecolor='#d3d3d3', linewidth=0,
            width=0.5, zorder=3
        )
        
    # PASS 3: Black Border Outline
    ax.bar(
        df.index, df[col], bottom=bottom, fill=False,
        edgecolor='black', linewidth=0.5, width=0.5, zorder=4
    )

    # Add Data Labels
    for bar in bars:
        height = bar.get_height()
        if height >= 2.0:
            ax.text(
                bar.get_x() + bar.get_width() / 2, 
                bar.get_y() + height / 2, 
                f'{height:.1f}%', 
                ha='center', va='center', color='black', 
                fontsize=18, fontweight='bold', fontname='Times New Roman', zorder=5
            )
    bottom += df[col]

# 6. FORMATTING (Matches your reference logic)
ax.set_ylim(0, 125)

# Grid and Spines
ax.grid(axis='y', linestyle='--', alpha=0.4, linewidth=0.8, color='gray', zorder=0)
ax.grid(axis='x', alpha=0) # No X grid

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Axis Labels
ax.set_ylabel('Percentage of Flagged Traces (%)', fontsize=18, fontweight='bold', fontname='Times New Roman', labelpad=10)
ax.set_xlabel('', fontsize=18)

# Ticks
ax.tick_params(axis='y', colors='black', labelsize=18)
ax.tick_params(axis='x', colors='black', labelsize=18)
# Force bold and Times New Roman on ticks manually if needed, or rely on global params
plt.xticks(fontweight='bold', rotation=0, fontname='Times New Roman')
plt.yticks(fontname='Times New Roman')

# Legend
# Define custom handles that combine Color + Pattern
legend_elements = [
    Patch(facecolor=colors[0], hatch=patterns[0], edgecolor='#d3d3d3', label='Alternative Correct'),
    Patch(facecolor=colors[1], hatch=patterns[1], edgecolor='#d3d3d3', label='Calculation Error'),
    Patch(facecolor=colors[2], hatch=patterns[2], edgecolor='#d3d3d3', label='Conceptual Error')
]

# Create the legend using these custom handles
legend = ax.legend(
    handles=legend_elements,     
    title='Tribunal Verdict', 
    loc='upper right', 
    frameon=True,
    edgecolor='black', 
    fancybox=False, 
    framealpha=1.0,
    fontsize=12, 
    title_fontsize=16, 
    ncol=1,
    prop={'family': 'Times New Roman', 'size': 12}
)

# Apply font styling
legend.get_title().set_fontweight('bold')
legend.get_title().set_fontname('Times New Roman')
legend.get_frame().set_linewidth(1.5)

plt.tight_layout()
plt.savefig('Error_Analysis_Stacked_Bar.pdf', dpi=300, bbox_inches='tight')
plt.show()
