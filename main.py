import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    """
    Loads the CSV file.
    """
    # 1. File Error Handling
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file '{filepath}' not found. Please check the path.")
    
    df = pd.read_csv(filepath)
    
    # 2. Input Validation
    if df.empty:
        raise ValueError("The dataset is empty.")
        
    required_cols = ['price_x', 'quantity', 'cost', 'status', 'country', 'category', 'return_id', 'return_reason']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns in CSV: {', '.join(missing_cols)}")

    # 3. Data Preparation
    # Fixed: Removed trailing spaces from original code that would cause KeyError
    df['revenue'] = df['price_x'] * df['quantity']
    df['profit'] = df['revenue'] - (df['cost'] * df['quantity'])

    df['return_reason'] = df['return_reason'].fillna('No return')
    df['return_id'] = pd.to_numeric(df['return_id'], errors='coerce').fillna(0).astype(int)

    return df

def print_revenue_by_category(df: pd.DataFrame) -> None:
    """Calculates and prints revenue grouped by product category."""
    print("\n REVENUE BY CATEGORY (sorted)")
    rev = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
    for cat, val in rev.items():
        print(f"  {cat:<15} ${val:,.2f}")

def print_revenue_by_country(df: pd.DataFrame) -> None:
    """Calculates and prints revenue grouped by country for completed orders only."""
    print("\n REVENUE BY COUNTRY (Completed Orders Only)")
    completed_df = df[df['status'] == 'completed']
    if completed_df.empty:
        print("  No completed orders found.")
        return
        
    rev_country = completed_df.groupby('country')['revenue'].sum().sort_values(ascending=False)
    for country, val in rev_country.items():
        print(f"  {country:<12} ${val:,.2f}")

def print_customer_behavior(df: pd.DataFrame) -> None:
    """Analyzes and prints overall order status distribution and abandonment rates."""
    print("\n CUSTOMER BEHAVIOR")
    total = len(df)
    if total == 0:
        print("  No orders to analyze.")
        return

    completed = (df['status'] == 'completed').sum()
    abandoned = (df['status'] == 'abandoned').sum()
    cancelled = (df['status'] == 'cancelled').sum()

    print(f"  Completed   {completed:>4} orders ({completed/total*100:.1f}%)")
    print(f"  Abandoned   {abandoned:>4} orders ({abandoned/total*100:.1f}%)")
    print(f"  Cancelled   {cancelled:>4} orders ({cancelled/total*100:.1f}%)")

    print("\n  Abandonment rate by country:")
    ab_rate = df.groupby('country')['status'].apply(
        lambda x: round((x == 'abandoned').sum() / len(x) * 100, 1)
    ).sort_values(ascending=False)

    for country, rate in ab_rate.items():
        print(f"    {country:<12} {rate}%")

def print_returns_analysis(df: pd.DataFrame) -> None:
    """Analyzes and prints return statistics, reasons, and top returned categories."""
    print("\n RETURNS ANALYSIS")
    returns = df[df['return_id'] != 0]
    total_orders = len(df)
    total_returns = len(returns)
    
    if total_returns == 0:
        print("  No returns recorded in the dataset.")
        return

    print(f"  Total returns: {total_returns} out of {total_orders} orders ({total_returns/total_orders*100:.1f}%)")

    print("\n  Return reasons (sorted):")
    reasons = returns['return_reason'].value_counts()
    for reason, count in reasons.items():
        print(f"    {reason:<20} {count} returns")
    
    print("\n  Most returned category:")
    top_return_cat = returns['category'].value_counts()
    for cat, count in top_return_cat.items():
        print(f"    {cat:<15} {count} returns")

def visualize_data(df: pd.DataFrame) -> None:
    """Generates a 2x2 dashboard of analytical charts."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    fig.suptitle('E-Commerce Data Analysis Dashboard', fontsize=16, fontweight='bold')

    # 1. Revenue by Category
    rev_cat = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
    axes[0, 0].bar(rev_cat.index, rev_cat.values, color='#4A90E2')
    axes[0, 0].set_title('Total Revenue by Category')
    axes[0, 0].set_ylabel('Revenue ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)

    # 2. Revenue by Country (Completed)
    completed_df = df[df['status'] == 'completed']
    if not completed_df.empty:
        rev_country = completed_df.groupby('country')['revenue'].sum().sort_values(ascending=False)
        axes[0, 1].bar(rev_country.index, rev_country.values, color='#50C878')
        axes[0, 1].set_title('Revenue by Country (Completed)')
        axes[0, 1].set_ylabel('Revenue ($)')
        axes[0, 1].tick_params(axis='x', rotation=45)
    else:
        axes[0, 1].text(0.5, 0.5, 'No completed orders', ha='center', va='center', transform=axes[0, 1].transAxes)

    # 3. Order Status Distribution
    status_counts = df['status'].value_counts()
    axes[1, 0].pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', 
                   startangle=140, colors=['#4A90E2', '#FF6B6B', '#A9A9A9'])
    axes[1, 0].set_title('Order Status Distribution')

    # 4. Return Reasons
    returns = df[df['return_id'] != 0]
    if not returns.empty:
        reason_counts = returns['return_reason'].value_counts()
        axes[1, 1].barh(reason_counts.index, reason_counts.values, color='#FFA500')
        axes[1, 1].set_title('Most Common Return Reasons')
        axes[1, 1].set_xlabel('Count')
    else:
        axes[1, 1].text(0.5, 0.5, 'No returns in dataset', ha='center', va='center', transform=axes[1, 1].transAxes)

    plt.show()

def main():
    """Main execution function that orchestrates the report generation."""
    filepath = "ecommerce_small_300.csv"
    
    try:
        print(" Loading and validating data...")
        df = load_and_prepare_data(filepath)
        print(" Data loaded successfully!\n")

        print("="*45)
        print("       E-COMMERCE QUICK REPORT          ")
        print("="*45)

        print_revenue_by_category(df)
        print_revenue_by_country(df)
        print_customer_behavior(df)
        print_returns_analysis(df)

        print("\n Generating visualizations...")
        visualize_data(df)
        print(" Report complete.")

    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Validation Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
