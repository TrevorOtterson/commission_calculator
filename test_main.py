import json
import pytest
from commission_calc import CC

# Load test data from JSON files
with open("data/deals.json", "r") as deal_file:
    test_deal_data = json.load(deal_file)
with open("data/products.json", "r") as product_file:
    test_product_data = json.load(product_file)

# pytest fixture is used to initialize the commission calculator with test data
@pytest.fixture
def commission_calculator():
    return CC(test_deal_data, test_product_data)

# calculates all commissions for all sales reps
def test_calc_all(commission_calculator):
    valid_data = {
        'Brad': 116880.0,
        'Carol': 5580.0,
        'David': 261430.00000000006,
        'Ian': 92370.0,
        'Jo': 343720.00000000006,
        'Poppy': 247220.0
    }
    commissions = commission_calculator.calc_all()
    assert valid_data == commissions

# tests that the commission calculator returns the correct commission for a single sales rep
def test_get_commissions_for_sales_rep(commission_calculator):
    sales_rep_name = "David"  # Replace with an actual sales rep name from your test data
    start_date = "2023-01-01"
    end_date = "2023-01-31"

    commission = commission_calculator.calculate_commission(sales_rep_name, start_date, end_date)
    assert commission == 1380


# Run tests
if __name__ == '__main__':
    pytest.main()