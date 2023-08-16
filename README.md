# Commission Calculator
Commission Calculator is a Python program that will calculate the total amount of commission that is earned by sales reps. This is based on the sales data and product details. This program reads its data from two different JSON files. `deals.json` (sales data) and `products.json` (product information). It will take into account the date range and calculate all the commissions from the sales on the given dates.

## Requirements

`python`

`json` module (built-in)

`pytest`

`typing`

`argparse`

`pprint`

## Getting Started
1. Clone the repository to your local machine.
2. Install required modules by running `pip install pytest`, `pip install argparse`, `pip install pprint`, and `pip install typing` in your terminal.

## Usage
Prepare the data files:
Place sales data in `data/deals.json`
Place product info in `data/products.json`

Run the program:
Execute main.py script by running: `python main.py -h` to see the help menu on how to use the flags.
`python main.py -i` will run interactive mode where a user can input the sales rep name, start date, and end date.
`python main.py -a` will calculate all commissions over all time for each sales rep and print it to the terminal.
`python main.py -n` will calculate all commissions for a given sales rep over all time.

Unit Tests:
To run the unit tests for the test_calc_all and test_get_commissions_for_sales_rep functions, execute the test.py script: `python test_main.py` you should see 2 tests ran successfully.

## How it Works
The program loads sales and product data from the provided JSON files.

It uses the CC class from commission_calc.py to calculate the commissions for each sale which is based on product amount, qty sold, and the commission rate. If the particular sale has a 2x multiplier then the commission total gets doubled.

In the argument parser module it is used to parse command line arguments and flags passed in when running the program from the command line. It then will initialize the commission calculator with the data from the json files and the args.

Using the flags the user is able to enter interactive mode where they can enter the sales reps name, sales date range and get a calculation for the given args. They are also able to calculate all sales reps commissions over time with the all flag. They can even calculate all commissions for a given rep by entering their name argument.

## License
This project is licensed under the MIT License