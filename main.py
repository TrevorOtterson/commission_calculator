import json
from functools import reduce

# load data from json files deserialized into python objects
with open("data/deals.json", "r") as deal_file:
    deal_data = json.load(deal_file)
with open("data/products.json", "r") as product_file:
    product_data = json.load(product_file)   
    
# get the sale dates
def get_date(sale):
    return sale['date']
  
""" 
calculating total commission for the output using sale instead of 
deal to get the exact date that these metrics are calculated at
"""
def calculate_commission(sale, product_data):
    product_id = sale['product_id']
    quantity_sold = sale['quantity_products_sold']
    multiplier = sale['has_2x_multiplier']

    # iterate through the product data to find the product id that matches the sale
    product = next(item for item in product_data if item["id"] == product_id)

    # product being defined above
    product_amount = product['product_amount']
    commission_rate = product['commission_rate']
    
    # calculate commission
    commission = product_amount * commission_rate * quantity_sold
    
    # some sales have a 2x multiplier on their commission, some do not
    if multiplier == True:
        commission *= 2
        
    return commission

# Function to group sales reps and calculate their total commission and date range
def group_and_calculate(acc, sale): 
    return {
    # use the key value pairs of a dict as input arguments for func call
    # groups sales reps and calculates their total commission and date range
    **acc,
    sale['sales_rep_name']: {
        'commission': acc.get(sale['sales_rep_name'], {}).get('commission', 0) + calculate_commission(sale, product_data),
        'dates': ((get_date(sale), get_date(sale)) if sale['sales_rep_name'] not in acc 
        else (min(get_date(sale), acc[sale['sales_rep_name']]['dates'][0]), max(get_date(sale), acc[sale['sales_rep_name']]['dates'][1])))
    }
}

# running the program and printing the completed output
def main():
    # Calculate the commission and date range for each sales rep
    commission_by_sales_rep = reduce(group_and_calculate, deal_data, {})

    # Print the result
    for sales_rep_name, data in commission_by_sales_rep.items():
        total_commission = data['commission']
        start_date, end_date = data['dates']
        print("-------------------------------")
        print("Sales Rep: " + str(sales_rep_name))
        print("Total Commission: ${:.2f}".format(total_commission))
        print(f"Date: {start_date} to {end_date}")
        print("-------------------------------")
        
if __name__ == "__main__":
    main()