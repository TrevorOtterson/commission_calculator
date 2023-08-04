# test_main.py
import json
from main import calculate_commission, group_and_calculate
from functools import reduce
import pytest

def load_json_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)

# Load data from json files
deal_data = load_json_data("data/deals.json")
product_data = load_json_data("data/products.json")

# Define test cases for calculate_commission
def test_calculate_commission():
    # Test case for a sale without 2x multiplier
    sale = {
        "id": 10001,
        "sales_rep_name": "David",
        "date": "2023-04-15",
        "quantity_products_sold": 3,
        "product_id": 20007,
        "has_2x_multiplier": 0
    }
    assert calculate_commission(sale, product_data) == 0.11 * 13000 * 3

    # Test case for a sale with 2x multiplier
    sale = {
        "id": 10005,
        "sales_rep_name": "Jo",
        "date": "2023-03-15",
        "quantity_products_sold": 3,
        "product_id": 20004,
        "has_2x_multiplier": 1
    }
    assert calculate_commission(sale, product_data) == 2 * 0.08 * 3000 * 3

# Define test case for group_and_calculate
def test_group_and_calculate():
    # Test case with a single sale
    deals_data = [
        {
            "id": 10001,
            "sales_rep_name": "David",
            "date": "2023-04-15",
            "quantity_products_sold": 3,
            "product_id": 20007,
            "has_2x_multiplier": 0
        }
    ]
    commission_by_sales_rep = reduce(group_and_calculate, deals_data, {})
    assert commission_by_sales_rep == {
        "David": {
            "commission": 0.11 * 13000 * 3,
            "dates": ("2023-04-15", "2023-04-15")
        }
    }

# Run the tests
if __name__ == "__main__":
    pytest.main()