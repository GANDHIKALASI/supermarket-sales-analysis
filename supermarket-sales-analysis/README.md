# Supermarket Sales Analysis

[![Developed by Gandhi Kalasi | AICTE | IBM SkillsBuild Internship 2026](https://img.shields.io/badge/Developed%20by-Gandhi%20Kalasi-blue.svg)](https://github.com/GandhiKalasi)
[![Program: AICTE | IBM SkillsBuild](https://img.shields.io/badge/Program-AICTE%20%7C%20IBM%20SkillsBuild-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

This repository contains a comprehensive exploratory data analysis (EDA), statistical summary, and visual reporting system for retail sales performance across supermarket branches. Developed as part of the **AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026** in partnership with **BharatCares**, this project provides empirical data insights to optimize retail inventory allocation, store branch operations, and customer engagement strategies.

---

## 📊 Dataset Information

- **Dataset Link**: [Google Sheets Dataset Source](https://docs.google.com/spreadsheets/d/1QIX__4VObHFMEXnRM2xJyXmB5JAB2peHrJcQ41_U9TE/edit?usp=sharing)
- **Dataset Size**: 500 records / rows
- **Dataset Columns (Exact Schema)**:
  `Invoice ID`, `Date`, `Branch`, `City`, `Customer Type`, `Gender`, `Product`, `Category`, `Quantity`, `Unit Price`, `Payment`, `Rating`, `Sales`

---

## 🛠️ Technologies Used

- **Language**: Python 3.10+
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `seaborn`, `matplotlib`
- **Spreadsheet & Document Generation**: `openpyxl`, `python-docx`

---

## 📁 Project Structure

```text
supermarket-sales-analysis/
├── data/
│   └── supermarket_sales.xlsx           # Real 500-row Excel dataset
├── output/
│   ├── 01_top_products.png              # Top 10 products by sales bar chart
│   ├── 02_sales_by_branch.png           # Sales by branch bar chart
│   ├── 03_sales_by_category.png         # Sales by category bar chart
│   ├── 04_payment_distribution.png      # Payment method pie chart
│   ├── 05_customer_type_avg.png         # Member vs Normal avg sales bar chart
│   ├── 06_rating_distribution.png       # Rating distribution histogram
│   └── summary.xlsx                     # Multi-tab analysis Excel report
├── GandhiKalasi_SupermarketSalesAnalysis.py # Main Python analysis script
├── GandhiKalasi_ProjectReport.docx      # Comprehensive executive Word report
├── requirements.txt                     # Project dependencies
├── README.md                            # Project documentation
└── .gitignore                           # Git ignore rules
```

---

## 🚀 Setup & Run Instructions

1. **Clone Repository**:
   ```bash
   git clone https://github.com/GandhiKalasi/supermarket-sales-analysis.git
   cd supermarket-sales-analysis
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis Script**:
   ```bash
   python3 GandhiKalasi_SupermarketSalesAnalysis.py
   ```

---

## 💡 Key Findings

1. **Total Revenue**: Total Gross Sales Revenue across all branches stands at **$244,411.08** over 500 transaction records.
2. **Top Product**: The single highest-selling product is **Cheese**, generating **$27,906.30** in revenue.
3. **Leading Branch**: Branch **C** emerged as the top-performing store location with **$72,469.45** in sales revenue.
4. **Dominant Category**: Category **Beverages** recorded the highest sales volume across categories at **$56,108.24**.
5. **Preferred Payment**: **UPI** is the most popular payment method, used in 127 transactions (**25.4%** of total order volume).
6. **Customer Segment Metrics**: Average order value for Member customers is **$483.14** compared to **$497.07** for Normal shoppers, while overall customer rating averaged **3.99 / 5**.

---

## 📈 Business Recommendations

1. **Inventory Prioritization**: Double down on stocking high-performing inventory in top revenue categories (Beverages, Personal Care, Dairy) to prevent stockouts.
2. **Loyalty Program Enhancement**: Leverage targeted incentives for Member customers to further elevate basket sizes and convert Normal shoppers into long-term members.
3. **Payment Gateway Optimization**: Streamline checkout throughput for the most popular digital payment methods (UPI & Net Banking).
4. **Branch Resource Reallocation**: Benchmark Branch C operational strategies and apply them to underperforming store locations.
5. **Strategic Product Bundling**: Package high-demand products (like Cheese and Coffee) with lower-performing items to increase overall order value.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Developed by Gandhi Kalasi — AICTE | IBM SkillsBuild Internship 2026
