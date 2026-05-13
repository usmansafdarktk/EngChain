import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Load the Data
df = pd.read_csv('EngChain_Model_Comparison_Domain.csv')

# 2. Select Narrative Models
selected_models = [
    'deepseek-reasoner',    
    'gemini-3-pro-preview', 
    'gemini-2.5-pro',       
    'meta-llama-3.1-70b'    
]

# Map to display names
display_names = {
    'deepseek-reasoner': 'DeepSeek R1',
    'gemini-3-pro-preview': 'Gemini 3 Pro',
    'gemini-2.5-pro': 'Gemini 2.5 Pro',
    'meta-llama-3.1-70b': 'Llama 3.1 70B'
}

# 3. Process Data
df_filtered = df[df['model'].isin(selected_models)].copy()
pivot_df = df_filtered.pivot(index='model', columns='domain', values='final_answer_match') * 100

# Define Order (Grouped by Branch)
domain_order = [
    'thermodynamics', 'reaction_kinetics', 'transport_phenomena',
    'digital_communications', 'signals_and_systems', 'electromagnetics_and_waves',
    'mechanics_of_materials', 'vibrations_and_acoustics', 'fluid_mechanics'
]
pivot_df = pivot_df[domain_order]

# Create readable labels
labels = [
    'Thermodynamics', 'Reaction\nKinetics', 'Transport\nPhenomena',
    'Digital\nComms', 'Signals &\nSystems', 'Electromag.\n& Waves',
    'Mechanics of\nMaterials', 'Vibrations\n& Acoustics', 'Fluid\nMechanics'
]

# 4. Setup Plot
N = len(labels)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Set transparent/very light background
plt.style.use('default')
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
fig.patch.set_facecolor('white')
fig.patch.set_alpha(0.0)  # Transparent figure background
ax.set_facecolor('white')
ax.patch.set_alpha(0.0)  # Transparent plot background

# Axes setup - remove labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Remove domain labels

# Y-Axis with lighter grid
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80], ["20%", "40%", "60%", "80%"], color="#666666", size=9)
plt.ylim(0, 100)
ax.grid(color='#AAAAAA', linewidth=0.8, alpha=0.7)

# Make outer border solid black and pronounced
ax.spines['polar'].set_color('black')
ax.spines['polar'].set_linewidth(1.2)
ax.spines['polar'].set_zorder(10)

# 5. Bright colors with VERY distinct line styles
colors = ['#56B4E9', '#E69F00', '#009E73', '#CC79A7']

styles = {
    'deepseek-reasoner':    {
        'color': colors[0], 
        'ls': (0, (1, 1)),  # Small dotted
        'lw': 2.5,
        'marker': 'o', 
        'ms': 8,
        'mew': 1.5
    },
    'gemini-3-pro-preview': {
        'color': colors[1], 
        'ls': (0, (3, 1, 1, 1, 1, 1)),  # Dash-dot-dot
        'lw': 2.5,
        'marker': '^', 
        'ms': 8,
        'mew': 1.5
    },
    'gemini-2.5-pro':       {
        'color': colors[2], 
        'ls': (0, (5, 2, 1, 2)),  # Long dash-dot
        'lw': 2.5,
        'marker': 's', 
        'ms': 7,
        'mew': 1.5
    },
    'meta-llama-3.1-70b':   {
        'color': colors[3], 
        'ls': '-',  # Solid
        'lw': 2.5,
        'marker': 'D', 
        'ms': 7,
        'mew': 1.5
    }
}

# 6. Plot Lines with distinct styles
for model in selected_models:
    if model not in pivot_df.index: 
        continue
    
    values = pivot_df.loc[model].values.flatten().tolist()
    values += values[:1]
    
    st = styles.get(model)
    name = display_names.get(model, model)
    
    # Plot line with markers
    ax.plot(angles, values, 
            linewidth=st['lw'], 
            linestyle=st['ls'], 
            label=name, 
            color=st['color'],
            marker=st['marker'],
            markersize=st['ms'],
            markeredgewidth=st['mew'],
            markeredgecolor=st['color'],
            markerfacecolor='white',
            zorder=3)
    
    # Very light fill - more transparent like reference
    ax.fill(angles, values, color=st['color'], alpha=0.03, zorder=1)

# Legend at Top with better styling
legend = plt.legend(loc='upper center', 
                   bbox_to_anchor=(0.5, 1.25), 
                   ncol=4, 
                   frameon=True,
                   fontsize=14,
                   fancybox=True,
                   shadow=True,
                   edgecolor='#999999',
                   framealpha=0.98,
                   columnspacing=1.5,
                   handlelength=3.0,
                   handletextpad=0.8,
                   borderpad=1.0)
legend.get_frame().set_facecolor('#FFFFFF')
legend.get_frame().set_alpha(0.95)

plt.tight_layout()
plt.savefig('Domain_Performance_Radar_Refined.png', dpi=300, bbox_inches='tight', facecolor='white', transparent=True)
plt.show()