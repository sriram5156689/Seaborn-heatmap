import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Generate synthetic business data
# ----------------------------
np.random.seed(42)

# Days of the week and time slots
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_slots = ["Morning", "Afternoon", "Evening", "Night"]

# Create engagement data (realistic synthetic data)
data = np.random.randint(20, 100, size=(len(days), len(time_slots)))

# Convert to DataFrame
df = pd.DataFrame(data, index=days, columns=time_slots)

# ----------------------------
# Seaborn Heatmap
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready font sizes

# Create figure: 8 inches * 64 dpi = 512 px
plt.figure(figsize=(8, 8))

# Heatmap
ax = sns.heatmap(
    df,
    annot=True,              # Show numbers inside cells
    fmt="g",                 # Works for ints and floats
    cmap="YlGnBu",           # Business-appropriate color map
    linewidths=0.5,          # Light grid lines
    linecolor="white",       # White grid lines
    cbar_kws={'label': 'Engagement Score'}  # Color bar label
)

# Titles and labels
plt.title("Customer Engagement Heatmap", fontsize=18, pad=20)
plt.xlabel("Time of Day", fontsize=14)
plt.ylabel("Day of the Week", fontsize=14)

# Save chart as exactly 512x512 px
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
