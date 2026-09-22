"""
Supermarket Sales Analysis
Developed by Gandhi Kalasi
AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn theme
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 10})

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'supermarket_sales.xlsx')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
EXCEL_OUTPUT_PATH = os.path.join(OUTPUT_DIR, 'summary.xlsx')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("==========================================")
    print("  Developed by Gandhi Kalasi")
    print("  Supermarket Sales Analysis Project")
    print("  AICTE | IBM SkillsBuild Internship")
    print("==========================================")
    print()

    # --- SECTION 1: DATA LOADING ---
    print("--- SECTION 1: DATA LOADING ---")
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset missing at {DATA_PATH}")
    df = pd.read_excel(DATA_PATH, engine="openpyxl")
    print(f"Successfully loaded dataset from: {DATA_PATH}")
    print()

    # --- SECTION 2: DATA EXPLORATION ---
    print("--- SECTION 2: DATA EXPLORATION ---")
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nMissing Values Per Column:")
    print(df.isnull().sum())
    print(f"\nDuplicate Rows Count: {df.duplicated().sum()}")
    print()

    # --- SECTION 3: DATA CLEANING ---
    print("--- SECTION 3: DATA CLEANING ---")
    # Drop duplicates
    initial_len = len(df)
    df = df.drop_duplicates().copy()
    print(f"Dropped {initial_len - len(df)} duplicate row(s). Total rows remaining: {len(df)}")

    # Handle missing values numeric -> median, categorical -> mode
    numeric_cols = ['Quantity', 'Unit Price', 'Rating', 'Sales']
    categorical_cols = ['Invoice ID', 'Date', 'Branch', 'City', 'Customer Type', 'Gender', 'Product', 'Category', 'Payment']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            if df[col].isnull().sum() > 0:
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                print(f"Imputed missing values in '{col}' with median: {median_val}")

    for col in categorical_cols:
        if col in df.columns:
            if df[col].isnull().sum() > 0:
                mode_val = df[col].mode()[0]
                df[col] = df[col].fillna(mode_val)
                print(f"Imputed missing values in '{col}' with mode: {mode_val}")

    print("Data cleaning completed successfully.")
    print()

    # --- SECTION 4: ANALYSIS ---
    print("--- SECTION 4: ANALYSIS ---")
    
    # a) Highest-selling product: group by Product, sum Sales, sort desc
    top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).reset_index()
    highest_selling_prod = top_products.iloc[0]
    print("\na) Top 10 Highest-Selling Products:")
    print(top_products.head(10).to_string(index=False))
    
    # b) Best branch: group by Branch, sum Sales
    branch_sales = df.groupby('Branch')['Sales'].sum().sort_values(ascending=False).reset_index()
    print("\nb) Sales by Branch:")
    print(branch_sales.to_string(index=False))

    # c) Best category: group by Category, sum Sales
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).reset_index()
    print("\nc) Sales by Category:")
    print(category_sales.to_string(index=False))

    # d) Most-used payment method: value_counts on Payment
    payment_counts = df['Payment'].value_counts().reset_index()
    payment_counts.columns = ['Payment', 'Count']
    print("\nd) Most-Used Payment Methods:")
    print(payment_counts.to_string(index=False))

    # e) Avg transaction value Member vs Normal: group by Customer Type, mean Sales
    cust_type_avg = df.groupby('Customer Type')['Sales'].mean().reset_index()
    cust_type_avg.columns = ['Customer Type', 'Average Sales']
    print("\ne) Average Transaction Value by Customer Type:")
    print(cust_type_avg.to_string(index=False))

    # f) Avg rating: mean of Rating rounded 2 decimals
    avg_rating = round(df['Rating'].mean(), 2)
    total_sales = round(df['Sales'].sum(), 2)
    total_orders = len(df)
    print(f"\nf) Overall Average Customer Rating: {avg_rating} / 10.0")
    print(f"   Total Cumulative Sales: ${total_sales:,.2f}")
    print(f"   Total Recorded Transactions: {total_orders}")
    print()

    # --- SECTION 5: VISUALIZATION ---
    print("--- SECTION 5: VISUALIZATION ---")
    print("Generating 6 high-resolution charts in output/...")
    
    footer_text = "Developed by Gandhi Kalasi"

    # 1. 01_top_products.png (bar: top 10 products by sales)
    plt.figure(figsize=(10, 6))
    top10_prods = top_products.head(10)
    ax1 = sns.barplot(data=top10_prods, x='Sales', y='Product', hue='Product', palette='pastel', legend=False)
    plt.title('Top 10 Products by Total Sales', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Total Sales ($)', fontsize=11, fontweight='bold')
    plt.ylabel('Product Name', fontsize=11, fontweight='bold')
    for p in ax1.patches:
        width = p.get_width()
        ax1.annotate(f"${width:,.2f}", 
                     (width, p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=9)
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '01_top_products.png'), dpi=300)
    plt.close()

    # 2. 02_sales_by_branch.png (bar: sales by branch)
    plt.figure(figsize=(8, 5))
    ax2 = sns.barplot(data=branch_sales, x='Branch', y='Sales', hue='Branch', palette='pastel', legend=False)
    plt.title('Total Sales Revenue by Branch', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Branch Code', fontsize=11, fontweight='bold')
    plt.ylabel('Total Sales ($)', fontsize=11, fontweight='bold')
    for p in ax2.patches:
        height = p.get_height()
        ax2.annotate(f"${height:,.2f}",
                     (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='bottom', xytext=(0, 4), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '02_sales_by_branch.png'), dpi=300)
    plt.close()

    # 3. 03_sales_by_category.png (bar: sales by category)
    plt.figure(figsize=(9, 5))
    ax3 = sns.barplot(data=category_sales, x='Category', y='Sales', hue='Category', palette='pastel', legend=False)
    plt.title('Total Sales Revenue by Product Category', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Category', fontsize=11, fontweight='bold')
    plt.ylabel('Total Sales ($)', fontsize=11, fontweight='bold')
    plt.xticks(rotation=15, ha='right')
    for p in ax3.patches:
        height = p.get_height()
        ax3.annotate(f"${height:,.2f}",
                     (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='bottom', xytext=(0, 4), textcoords='offset points', fontsize=9, fontweight='bold')
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '03_sales_by_category.png'), dpi=300)
    plt.close()

    # 4. 04_payment_distribution.png (pie: payment method distribution)
    plt.figure(figsize=(7, 6))
    colors = sns.color_palette('pastel')[0:len(payment_counts)]
    plt.pie(payment_counts['Count'], labels=payment_counts['Payment'], autopct='%1.1f%%',
            startangle=140, colors=colors, textprops={'fontsize': 11, 'weight': 'bold'})
    plt.title('Payment Method Distribution', fontsize=14, fontweight='bold', pad=15)
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '04_payment_distribution.png'), dpi=300)
    plt.close()

    # 5. 05_customer_type_avg.png (bar: avg sales Member vs Normal)
    plt.figure(figsize=(8, 5))
    ax5 = sns.barplot(data=cust_type_avg, x='Customer Type', y='Average Sales', hue='Customer Type', palette='pastel', legend=False)
    plt.title('Average Order Value by Customer Type', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Customer Type', fontsize=11, fontweight='bold')
    plt.ylabel('Average Sales ($)', fontsize=11, fontweight='bold')
    for p in ax5.patches:
        height = p.get_height()
        ax5.annotate(f"${height:,.2f}",
                     (p.get_x() + p.get_width() / 2., height),
                     ha='center', va='bottom', xytext=(0, 4), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '05_customer_type_avg.png'), dpi=300)
    plt.close()

    # 6. 06_rating_distribution.png (histogram of ratings)
    plt.figure(figsize=(8, 5))
    ax6 = sns.histplot(df['Rating'], bins=10, kde=True, color=sns.color_palette('pastel')[2])
    plt.title('Customer Rating Distribution', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Rating (1 to 5 / 10)', fontsize=11, fontweight='bold')
    plt.ylabel('Frequency (Transactions)', fontsize=11, fontweight='bold')
    plt.figtext(0.99, 0.01, footer_text, ha='right', fontsize=9, fontstyle='italic', color='gray')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, '06_rating_distribution.png'), dpi=300)
    plt.close()

    # Excel Summary Export
    with pd.ExcelWriter(EXCEL_OUTPUT_PATH, engine='openpyxl') as writer:
        top_products.to_excel(writer, sheet_name='Top Products', index=False)
        branch_sales.to_excel(writer, sheet_name='Sales by Branch', index=False)
        category_sales.to_excel(writer, sheet_name='Sales by Category', index=False)
        payment_counts.to_excel(writer, sheet_name='Payment Methods', index=False)
        cust_type_avg.to_excel(writer, sheet_name='Customer Type Avg Sales', index=False)
        
        kpi_df = pd.DataFrame([
            {'Metric': 'Total Revenue ($)', 'Value': total_sales},
            {'Metric': 'Total Transactions', 'Value': total_orders},
            {'Metric': 'Average Rating', 'Value': avg_rating},
            {'Metric': 'Top Selling Product', 'Value': highest_selling_prod['Product']},
            {'Metric': 'Top Product Revenue ($)', 'Value': highest_selling_prod['Sales']},
            {'Metric': 'Top Branch', 'Value': branch_sales.iloc[0]['Branch']},
            {'Metric': 'Top Branch Revenue ($)', 'Value': branch_sales.iloc[0]['Sales']},
            {'Metric': 'Top Category', 'Value': category_sales.iloc[0]['Category']},
            {'Metric': 'Top Category Revenue ($)', 'Value': category_sales.iloc[0]['Sales']}
        ])
        kpi_df.to_excel(writer, sheet_name='Overall KPIs & Ratings', index=False)

    print("All charts and output/summary.xlsx successfully generated!")
    print()

    # --- SECTION 6: BUSINESS INSIGHTS ---
    print("--- SECTION 6: BUSINESS INSIGHTS ---")
    best_prod_name = highest_selling_prod['Product']
    best_prod_rev = highest_selling_prod['Sales']
    best_branch_name = branch_sales.iloc[0]['Branch']
    best_branch_rev = branch_sales.iloc[0]['Sales']
    best_cat_name = category_sales.iloc[0]['Category']
    best_cat_rev = category_sales.iloc[0]['Sales']
    top_pay_method = payment_counts.iloc[0]['Payment']
    top_pay_cnt = payment_counts.iloc[0]['Count']
    top_pay_pct = round((top_pay_cnt / total_orders) * 100, 1)
    member_avg = cust_type_avg[cust_type_avg['Customer Type'] == 'Member']['Average Sales'].values[0]
    normal_avg = cust_type_avg[cust_type_avg['Customer Type'] == 'Normal']['Average Sales'].values[0]

    print("\nKEY FINDINGS (Empirical Real Data):")
    print(f"1. Total Gross Sales Revenue across all branches stands at ${total_sales:,.2f} over {total_orders} transactions.")
    print(f"2. The single highest-selling product is '{best_prod_name}', generating ${best_prod_rev:,.2f} in sales.")
    print(f"3. Branch '{best_branch_name}' emerged as the top-performing store location with ${best_branch_rev:,.2f} in revenue.")
    print(f"4. Category '{best_cat_name}' recorded the highest sales volume across categories at ${best_cat_rev:,.2f}.")
    print(f"5. The most popular payment method is '{top_pay_method}', used in {top_pay_cnt} transactions ({top_pay_pct}% of total volume).")
    print(f"6. Average transaction value for Member customers (${member_avg:,.2f}) compared to Normal shoppers (${normal_avg:,.2f}), while overall customer satisfaction rating averaged {avg_rating} / 10.0.")

    print("\nBUSINESS RECOMMENDATIONS:")
    print("1. Inventory Prioritization: Double down on stocking high-performing inventory in top revenue categories to prevent stockouts.")
    print("2. Loyalty Program Enhancement: Leverage targeted incentives for Member customers to further elevate basket sizes and convert Normal shoppers.")
    print("3. Payment Gateway Optimization: Streamline checkout for the most popular digital and card payment methods to accelerate transaction throughput.")
    print("4. Branch Resource Reallocation: Benchmark top-performing branch operational strategies and apply them to underperforming store locations.")
    print("5. Strategic Product Bundling: Package high-demand products with lower-performing items to increase overall order values.")
    print()

if __name__ == '__main__':
    main()
