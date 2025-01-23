import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt


shot_data = {
    'x': [103, 112, 92, 105],  
    'y': [23, 32, 39, 50],  
    'on_target': [True, True, False, True],  
    'goal': [False, True, False, False]  
}

df_shots = pd.DataFrame(shot_data)

# --------------------------

pitch = Pitch(line_color='black', pitch_color='white')
fig, ax = pitch.draw(figsize=(12, 8))

# --------------------------

goals = df_shots[df_shots['goal']]
pitch.scatter(goals['x'], goals['y'], s=300, c='red', ax=ax, edgecolors='black', label='Goal')


on_target = df_shots[df_shots['on_target'] & ~df_shots['goal']]
pitch.scatter(on_target['x'], on_target['y'], s=200, c='green', ax=ax, edgecolors='black', label='On Target')


off_target = df_shots[~df_shots['on_target']]
pitch.scatter(off_target['x'], off_target['y'], s=200, c='blue', ax=ax, edgecolors='black', label='Off Target')

# --------------------------

text_data = """
Rafael Leão - Match vs Girona

Touches: 43
Accurate Passes: 19/24 (79%)
Key Passes: 2
Goals: 1
Shots on Target: 3
Shots off Target: 1
"""


plt.text(95, 90, text_data, fontsize=12, color='black', va='top', wrap=True)

# --------------------------

ax.legend(loc='upper left', fontsize=12)
ax.set_title("Rafael Leão - Shot Map vs Girona", fontsize=20)


plt.show()

# --------------------------

fig.savefig("rafael_leao_shots_vs_girona.png", dpi=300)

# --------------------------

from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('rafael_leao_shots_vs_girona.pdf') as pdf:
    pdf.savefig(fig)
