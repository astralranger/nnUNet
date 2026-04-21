import matplotlib.pyplot as plt
import numpy as np

# Extracted from training logs:
case_ids = ['la_007', 'la_016', 'la_021', 'la_024']
pz_dice = [0.684, 0.692, 0.673, 0.682] # Peripheral Zone Average
tz_dice = [0.884, 0.890, 0.888, 0.892] # Transitional Zone Average
total_avg = [0.784, 0.791, 0.780, 0.787] # Average Pseudo Dice

x = np.arange(len(case_ids))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

# Plot bars for PZ and TZ
rects1 = ax.bar(x - width/2, pz_dice, width, label='Peripheral Zone (PZ)', color='orange', alpha=0.8)
rects2 = ax.bar(x + width/2, tz_dice, width, label='Transitional Zone (TZ)', color='deepskyblue', alpha=0.8)

# Add average line
ax.axhline(y=np.mean(total_avg), color='red', linestyle='--', label=f'Mean Total Dice ({np.mean(total_avg):.2f})')

ax.set_ylabel('Dice Coefficient (Accuracy)')
ax.set_title('nnU-Net Multi-Label Prostate AI Results (Fold 0)')
ax.set_xticks(x)
ax.set_xticklabels(case_ids)
ax.legend()
ax.set_ylim(0, 1.0)

# Add values on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
out_path = r"c:\The Sketchbook\SEM VI\CV-Project\prostate_metrics_graph.png"
plt.savefig(out_path, dpi=120)
print("Prostate performance metrics graph saved to:", out_path)
