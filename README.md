# Quarterly Sales Analysis & Visualization

## Overview
This project is a Python-based data analysis and visualization script. It generates synthetic sales data for three product categories (Laptops, Phones, Accessories) across four quarters and visualizes their performance. The script serves as a practical demonstration of data manipulation, aggregation, and business-oriented data visualization.

## Key Features
* **Data Generation:** Uses `NumPy` to create reproducible synthetic sales data.
* **Data Processing:** Leverages `Pandas` to calculate annual totals and cumulative year-to-date (YTD) sums.
* **Business-Oriented Visualizations:** Generates a clean 1x3 subplot layout using `Matplotlib`:
  1. **Annual Total per Product:** A bar chart comparing total yearly sales, featuring an **Annual Target** reference line.
  2. **Sales Evolution by Quarter:** A line chart tracking the quarterly performance of each product against an **Ideal Quarterly Threshold**.
  3. **Cumulative Sales (YTD):** A trend line chart illustrating cumulative growth towards a **Final Cumulative Goal**.
* **Clean Formatting:** Utilizes Matplotlib's `seaborn-v0_8-whitegrid` style for clear, readable, and professional charts.

## Technologies Used
* **Python 3.x**
* **Pandas** (Data manipulation and analysis)
* **NumPy** (Numerical operations and synthetic data generation)
* **Matplotlib** (Data visualization)

## How to Run

1. **Clone this repository:**
   ```bash
   git clone [https://github.com/GigioneRadu/Portfolio_Quarterly_Sales_Analysis.git](https://github.com/GigioneRadu/Portfolio_Quarterly_Sales_Analysis.git)
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Portfolio_Quarterly_Sales_Analysis
   ```

3. **Install the required dependencies:**
   ```bash
   pip install pandas numpy matplotlib
   ```

4. **Run the script:**
   ```bash
   python Sales_Analysis_Report.py
   ```
