from typing import List, Dict

class CC: #CC short for Commission Calculator
    """Class for calculating commissions based on sales data."""
    
    # Initialize the class with deals and products data.
    def __init__(self, _deals: list[dict], _products: list[dict]):
        self.products = _products
        self.deals = _deals

    # Calculate commission for a given sales rep.
    def calculate_commission(self, name: str, start: str, stop: str) -> float:
        if not start:
            start = '2000-01-01'
        if not stop:
            stop = '3000-01-01'
        if name:
            rep_data = [self.calculate_commission_helper(x) for x in self.deals if
                        x['sales_rep_name'] == name and start <= x['date'] <= stop]
            return sum(rep_data)
        
    # Calculate commission for a given sale.
    def calculate_commission_helper(self, sale: dict) -> float:
        product_index = int(sale["product_id"]) - 20001
        product = self.products[product_index]
        commission = product['product_amount'] * product['commission_rate'] * sale['quantity_products_sold']
        if sale["has_2x_multiplier"]:
            commission *= 2
        return commission

    # Calculate commission for all sales reps.
    def calc_all(self, start: str = None, stop: str = None):
        employees = set([x['sales_rep_name'] for x in self.deals])
        return {x: self.calculate_commission(x, start, stop) for x in employees}