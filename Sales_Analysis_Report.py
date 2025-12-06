import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Style and Data Configuration
# Setting a clean visual style
plt.style.use('seaborn-v0_8-whitegrid')

# Generating synthetic data: 3 Products across 4 Quarters
np.random.seed(42) # For reproducible results
data = {
    'Laptops': np.random.randint(50, 120, 4),
    'Phones': np.random.randint(80, 150, 4),
    'Accessories': np.random.randint(30, 90, 4)
}
index = ['Q1', 'Q2', 'Q3', 'Q4']

# Creating the DataFrame
df = pd.DataFrame(data, index=index)

# Calculate the cumulative sum for EACH product (down the quarters)
df_cumulative = df.cumsum()


# 2. Creating Subplots (1 row, 3 columns)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6), sharey=False)
fig.suptitle('Sales Analysis: Quarterly and Cumulative Performance', fontsize=16)

# --- SUBPLOT 1: Bar Chart per Product (Annual Total) ---
# Summing across the index (quarters) to get the annual total per product
annual_total_per_product = df.sum()

# Plotting directly from Pandas (kind='bar')
annual_total_per_product.plot(kind='bar', ax=axes[0], color=['#4c72b0', '#55a868', '#c44e52'], rot=0)

axes[0].set_title("Total Sales per Product")
axes[0].set_ylabel("Units Sold")
axes[0].set_xlabel("Category")

# Reference Line (Annual Target)
axes[0].axhline(y=350, color='red', linestyle='--', linewidth=2, label='Annual Target (350)')
axes[0].legend()

# --- SUBPLOT 2: Line Chart by Quarter (Evolution) ---
# Plotting evolution over quarters (implicit kind='line')
df.plot(ax=axes[1], marker='o', linewidth=2)

axes[1].set_title("Sales Evolution by Quarter")
axes[1].set_xlabel("Quarter")
axes[1].grid(True, which='both', linestyle='--', alpha=0.7)

# Reference Line (Ideal Quarterly Threshold)
axes[1].axhline(y=100, color='grey', linestyle=':', label='Ideal Quarterly Threshold')

# --- SUBPLOT 3: Cumulative Total (Year-to-Date Trend) ---
df_cumulative.plot(ax=axes[2], linestyle='--', marker='s', alpha=0.8)

axes[2].set_title("Cumulative Sales (Year-to-Date)")
axes[2].set_xlabel("Quarter")

# Reference Line (Final Cumulative Goal)
axes[2].axhline(y=1000, color='purple', linestyle='-.', linewidth=1.5, label='Final Cumulative Goal')

# 3. Finalization and Visual Synchronization
# Hiding the legend in subplot 2 to clean the chart
axes[1].legend().set_visible(False)

# Adjusting the legend in subplot 3 for clarity
axes[2].legend(loc='upper left', title="Products")

# Automatic adjustment of spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()