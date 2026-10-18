# Data Visualization with Matplotlib & Seaborn

An analytical data dashboard containing structured exploratory visualizations created with **Matplotlib** and **Seaborn** to profile demographic distribution trends from the real-world waiter tipping dataset.

## 📊 Project Visual Overview
This project compiles a complete 2x2 multi-panel layout saved at **150 DPI**, fulfilling the technical story-driven visualization project criteria:

1. **Histogram (Distribution):** Visualizes how `total_bill` transactions cluster heavily within specific cost limits.
2. **Box Plot (Structural Group Comparison):** Charts median tip variations across business operation days.
3. **Scatter Plot (Relationship):** Illustrates the positive directional correlation between consumption totals and rewards.
4. **Correlation Heatmap:** Automatically isolates statistical dependencies across numerical classifications.

## 🛠️ Design & Formatting Choices
* **Palette Stability:** Utilizes a colorblind-friendly soft tone layout configuration (`palette="muted"`).
* **Self-Documented Insights:** Every graphic incorporates strict structural labels, unit parameters (USD, Counts), and descriptive takeaways directly inside the grid workspace.

## 📈 Key Visual Discoveries
* **Distribution Peak:** The majority of consumption checks remain densely concentrated between **\$10 and \$25**.
* **Reward Drivers:** Sunday operations routinely yield the highest baseline median tips.
* **Statistical Ties:** A high linear correlation (**0.68**) exists explicitly between total bill amounts and resulting gratuity tips.

## 🚀 Repository Contents
* `tips_visualization.py` - The production script used to process the source manifest data and generate frames.
* `tips_dashboard_overview.png` - The final compiled 150 DPI layout dashboard overview image.
