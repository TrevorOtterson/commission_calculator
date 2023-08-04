# Commission Calculator
Commission Calculator is a Python program that will calculate the total amount of commission that is earned by sales reps. This is based on the sales data and product details. This program reads its data from two different JSON files. `deals.json` (sales data) and `products.json` (product information). It will take into account the date range and calculate all the commissions from the sales on the given dates.

## Requirements
python 3+

`json` module (built-in)

`functools.reduce` function (built-in)

## Getting Started
1. Clone the repository to your local machine.
2. Download Python 3+
3. Install required modules by running `pip install pytest` in your terminal.

## Usage
Prepare the data files:
Place sales data in `data/deals.json`
Place product info in `data/products.json`

Run the program:
Execute main.py script by running: `python main.py` to calculate commissions and display results inside the terminal.

Unit Tests:
To run the unit tests for the calculate_commission and group_and_calculate functions, execute the test.py script: `python test_main.py`

## How it Works
The program loads sales and product data from the provided JSON files.

It uses the calculate_commission function to calculate the commissions for each sale which is based on product amount, qty sold, and the commission rate. If the particular sale has a 2x multiplier then the commission total gets doubled.

The group_and_calculate lambda function will group the same name sales reps together (since they are the same salesman) and it will calculate their total commission based on their date range (first sale to the last).

Commission Calculator will then print the total commission, the sales reps names, and their date range for the sales to the terminal.

## License
This project is licensed under the MIT License