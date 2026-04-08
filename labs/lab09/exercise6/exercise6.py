import pandas as pd


def critical_inventory(filename):
    
    df = pd.read_csv(filename)

    

    stock = df["StockLevel"] < df["ReorderThreshold"]
    restock = df["DaysSinceRestock"] > 30
    critical = stock & restock

    critical_count = critical.sum()

    critical_products = df[critical]
    product = set(critical_products["ProductName"])

    return {
        "total_products": len(df),
        "critical_count": critical_count,
        "critical_products": product
    }
