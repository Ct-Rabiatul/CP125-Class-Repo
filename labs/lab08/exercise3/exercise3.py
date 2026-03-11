# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    f = open(products_file, "r", newline="")
    product = csv.reader(f)

    prices = {}
    next(product)
    for row in product :
        product_id = row[0]
        price = float(row[2])
        prices[product_id] = price
    

    
    j = open(order_file, "r", newline="")
    order = csv.reader(j)
    t = open(output_file, "w", newline="")
    total= csv.writer(t)

    total.writerow(["product_id", "total_cost"])

    total_all = 0
    next(order)
    for row in order:

        product_id = row[0]
        quantity = int(row[1])

        total_cost = prices[product_id] * quantity
        total_all += total_cost

        total.writerow([product_id, f"{total_cost:.2f}"])

    f.close()
    j.close()
    t.close()
    return total_all



    
# Test your code here
result = calculate_order_total("CP125-Class-Repo/labs/lab08/exercise3/data/products.csv", "CP125-Class-Repo/labs/lab08/exercise3/data/order.csv", "CP125-Class-Repo/labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
