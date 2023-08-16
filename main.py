import json
import argparse
import pprint
from commission_calc import CC

# define constants for file paths to deal and product json data
DEAL_FILE = "data/deals.json"
PRODUCT_FILE = "data/products.json"

def arg_mode():
    """Calculate commission for a single sales rep in arg mode."""
    return calc.calculate_commission(args.name, args.start, args.end)

def interactive() -> tuple[str, str, str, float]:
    """Interactive mode for calculating commissions."""
    name = input("Enter a sales rep's name: ")
    start_date = input("Enter a start date (YYYY-MM-DD): ")
    end_date = input("Enter an end date (YYYY-MM-DD): ")
    return name, start_date, end_date, calc.calculate_commission(name, start_date, end_date)

if __name__ == '__main__':
    """Main entry point for the program."""

    # Load data from JSON files
    with open(DEAL_FILE, "r") as deal_file:
        deal_data = json.load(deal_file)

    with open(PRODUCT_FILE, "r") as product_file:
        product_data = json.load(product_file)

    # parse command line arguments(run -h for arg help)
    # parsing args for interactive mode, all commissions, and a single sales rep
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interactive", help="Run in interactive mode", action="store_true")
    parser.add_argument("-a", "--all", help="Calculate all commissions", action="store_true")
    parser.add_argument("-n", "--name", help="Sales rep's name")
    parser.add_argument("-s", "--start", help="Start date (YYYY-MM-DD)")
    parser.add_argument("-e", "--end", help="End date (YYYY-MM-DD)")
    calc = CC(deal_data, product_data)
    args = parser.parse_args()

    # loop through data if interactive mode is enabled and print results
    if args.interactive:
        print("Interactive mode enabled. Press Ctrl+C to exit.")
        while True:
            try:
                name, start, stop, commission = interactive()
                print(
                    f""
                    f"\nsales_rep_name='{name}', start_date='{start}', end_date='{stop}' = ${commission:.2f}"
                    f"\n")
            # this allows the user to exit the program by pressing Ctrl+C and not throw an error
            except KeyboardInterrupt:
                print("\nExiting...")
                break

    elif args.all:  # print all commissions if -a flag is passed in
        res = calc.calc_all(args.start, args.end)
        pprint.pprint(res)
    else:  # print commission for a single sales rep if -n flag is passed in with a name argument
        if not args.name:
            raise ValueError("Must provide a name")  # cant run in arg mode without a name
        res = arg_mode()
        print(
            f""
            f"\nsales_rep_name='{args.name}', start_date='{args.start}', end_date='{args.end}' = ${res:.2f}"
            f"\n")