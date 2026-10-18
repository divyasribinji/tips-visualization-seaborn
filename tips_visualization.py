import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("====================================================")
print("   DATA VISUALIZATION WITH MATPLOTLIB & SEABORN     ")
print("====================================================\n")

# 1. Load the real tips dataset
tips = sns.load_dataset("tips")

# 2. Set style configuration (Colorblind-friendly theme)
sns.set_theme(style="whitegrid", palette="muted")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- CHART 1: Histogram (Distribution of one number) ---
# Question 1: How are total bills distributed across all meals?
sns.histplot(data=tips, x="total_bill", bins=20, ax=axes[0, 0], color="b", kde=True)
axes[0, 0].set_title("1. Distribution of Total Bills", fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel("Total Bill Amount (USD)", fontsize=10)
axes[0, 0].set_ylabel("Number of Meals", fontsize=10)
# Takeaway 1 text directly embedded into the graph area
axes[0, 0].text(22, 25, "Takeaway: Most meal bills sit heavily between $10 and $25.", 
                fontsize=9, bbox=dict(facecolor='white', alpha=0.8))

# --- CHART 2: Box Plot (Comparing structural groups) ---
# Question 2: Do tip values significantly differ by day of the week?
sns.boxplot(data=tips, x="day", y="tip", ax=axes[0, 1], order=["Thur", "Fri", "Sat", "Sun"])
axes[0, 1].set_title("2. Tip Amounts by Day of the Week", fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel("Day of the Week", fontsize=10)
axes[0, 1].set_ylabel("Tip Value (USD)", fontsize=10)
axes[0, 1].text(0.5, 8.5, "Takeaway: Sunday dinners produce the highest median tips.", 
                fontsize=9, bbox=dict(facecolor='white', alpha=0.8))

# --- CHART 3: Scatter Plot (Relationship between two numbers) ---
# Question 3: Does a higher total bill mean a larger tip amount?
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time", ax=axes[1, 0], s=60)
axes[1, 0].set_title("3. Relationship: Total Bill vs. Tip Amount", fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel("Total Bill (USD)", fontsize=10)
axes[1, 0].set_ylabel("Tip Given (USD)", fontsize=10)
axes[1, 0].text(5, 8.5, "Takeaway: Strong positive trend; higher bills yield larger tips.", 
                fontsize=9, bbox=dict(facecolor='white', alpha=0.8))

# --- CHART 4: Correlation Heatmap (How variables move together) ---
# Question 4: Which numeric variables have the strongest correlation relationships?
numeric_df = tips.select_dtypes(include=["number"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues", fmt=".2f", ax=axes[1, 1], cbar=True)
axes[1, 1].set_title("4. Correlation Matrix of Variables", fontsize=12, fontweight='bold')
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0)
axes[1, 1].set_yticklabels(axes[1, 1].get_yticklabels(), rotation=0)
# Strongest relationship identification text
axes[1, 1].text(-0.2, 2.8, "Takeaway: Total bill and tip amount show the strongest correlation (0.68).", 
                fontsize=9, fontweight='bold', color="navy")

# 3. Final layout cleanups to prevent clipping issues
plt.tight_layout()

# Save the unified dashboard image at 150 DPI requirement
output_filename = "tips_dashboard_overview.png"
plt.savefig(output_filename, dpi=150)
print(f"[✓] Dashboard graphic successfully compiled and saved as: '{output_filename}'")
plt.show()
