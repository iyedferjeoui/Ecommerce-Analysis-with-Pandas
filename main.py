import pandas as pd
import matplotlib.pyplot as plt

def load_and_prepare_data(filepath: str) -> pd.DataFrame:
    """
    Loads the CSV file and calculates derived columns (revenue, profit, etc.).
    """
    df = pd.read_csv(filepath)
    
    df["revenue"] = df["price_x"] * df["quantity"]
    df["profit"] = df["revenue"] - (df["cost"] * df["quantity"])
    
    df["return_reason"] = df["return_reason"].fillna("No return")
    df["return_id"] = df["return_id"].fillna(0)
    
    return df

def print_revenue_by_category(df: pd.DataFrame) -> None:
    """
    Calculates and prints revenue grouped by product category.
    """
    print("\n REVENUE BY CATEGORY (sorted)")
    rev = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    for cat, val in rev.items():
        print(f"  {cat:<15} ${val:,.0f}")

def print_revenue_by_country(df: pd.DataFrame) -> None:
    """
    Calculates and prints revenue grouped by country for completed orders only.
    """
    print("\n REVENUE BY COUNTRY (sorted)")
    completed_df = df[df["status"] == "completed"]
    rev_country = completed_df.groupby("country")["revenue"].sum().sort_values(ascending=False)
    
    for country, val in rev_country.items():
        print(f"  {country:<12} ${val:,.0f}")

def print_customer_behavior(df: pd.DataFrame) -> None:
    """
    Analyzes and prints overall order status distribution and abandonment rates by country.
    """
    print("\n CUSTOMER BEHAVIOR")
    total = len(df)
    completed = (df["status"] == "completed").sum()
    abandoned = (df["status"] == "abandoned").sum()
    cancelled = (df["status"] == "cancelled").sum()
    
    print(f"  Completed   {completed} orders ({completed/total*100:.0f}%)")
    print(f"  Abandoned   {abandoned} orders ({abandoned/total*100:.0f}%)")
    print(f"  Cancelled   {cancelled} orders ({cancelled/total*100:.0f}%)")

    print("\n  Abandonment rate by country (sorted):")
    ab_rate = df.groupby("country")["status"].apply(
        lambda x: round((x == "abandoned").sum() / len(x) * 100, 1)
    ).sort_values(ascending=False)
    
    for country, rate in ab_rate.items():
        print(f"    {country:<12} {rate}%")

def print_returns_analysis(df: pd.DataFrame) -> None:
    """
    Analyzes and prints return statistics, reasons, and top returned categories.
    """
    print("\n RETURNS")
    returns = df[df["return_id"] != 0]
    total_orders = len(df)
    total_returns = len(returns)
    
    print(f"  Total returns: {total_returns} out of {total_orders} orders ({total_returns/total_orders*100:.1f}%)")
    
    print("\n  Return reasons (sorted):")
    reasons = returns["return_reason"].value_counts()
    for reason, count in reasons.items():
        print(f"    {reason:<20} {count} returns")
        
    print("\n  Most returned category:")
    top_return_cat = returns["category"].value_counts()
    for cat, count in top_return_cat.items():
        print(f"    {cat:<15} {count} returns")

def main():
    """
    Main execution function that orchestrates the report generation.
    """
    df = load_and_prepare_data("ecommerce_small_300.csv")
    
    print(" E-COMMERCE QUICK REPORT")
    
    # Execute Report Parts
    print_revenue_by_category(df)
    print_revenue_by_country(df)
    print_customer_behavior(df)
    print_returns_analysis(df)

if __name__ == "__main__":
    main()