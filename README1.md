# Spiff Engineering Candidate Coding Exercises

## Purpose
These coding exercises are meant to help Spiff gain insight into how you would tackle actual development work as part of the team. The exercise is relatively simple, but you are encouraged to treat them as if you were working on the Spiff codebase. **This means applying the same attention to code quality, tests, pull requests, commits, etc as you normally would.** 

**_Quality is valued above quantity. We value simple and readable code_**

## Background

Spiff's primary product offering is a SAS solution that helps companies automate their commissions. While the real world logic and systems needed to calculate commissions gets rather complicated, the core idea is simple: Some product is sold by a sales representative at a given price and the commission is some percentage rate multiplied by the price of the product sold. For example, selling a car for \$30,000 at a 5\% commission rate would earn a \$1,500 (\$30,000 * 0.05) commission.

## Creating a Commission Calculator

Create code (preferably Ruby, Python, or Elixir but any language you are most comfortable with works) for this small scale commission calculator based on the provided sample data. In particular, your solution should be able take in a string of a sales representative's name along with a starting and ending date, then calculate the total commission for that sales rep during that period.

Here is a sample of what the main function/method might look like:

```{python}
def calculate_commission(sales_rep_name, start_date, end_date):
    """
    Function/method to calculate commission for a sales rep in a given time period.

    Args:
        sales_rep_name (str): Name of the sales rep to calculate commission for.
        start_date (str): Starting date for the date range where commissions will be valid.
        end_date (str): Ending date for the date range where commissions will be valid.

    Returns:
        float: A single float value for total commission amount based on the input criteria. e.g. $749.48
    """

    ### Your code and call to helper functions/methods here ###

    return total_commission
```

### Input Data

The input data can be found in the "data" folder of this repo. It contains two tables worth of data in .json format (one for the Deals and one for the Products). The Deals data contains information about an individual deal that was sold (i.e. sales_rep_name, date, quantity_products_sold, product_id) and the Products data contains related data about the products such as product_amount and the commission rate for that product. In order to get all of the data needed to calculate the commission the Deals data will require additional information from the Product table (product_id form Deals is the reference id of the Products data).

### Commission Calculation Logic

See the below example logic for how to calculate the commission on the first deal in the Deals data.

```{json}
{
    "id": 10001,
    "sales_rep_name": "David",
    "date": "2023-04-15",
    "quantity_products_sold": 3,
    "product_id": 20007,
    "has_2x_multiplier": 0
}
```

We will also need the corresponding data from the products table (using product_id = 20007)

```{json}
{
    "id": 20007,
    "name": "Product_7",
    "product_amount": 13000,
    "commission_rate": 0.11
}
```

The commission logic for this single line would be calculated as follows:
(Your code should use this same logic/formula)

```{math}
commission  = quantity_products sold (from Deals) * product_amount (from Products) * commission_rate (from products)
            = 3 * $13,000 * 0.11
            = $4,290
```

### Coding Aspects to Include

* Function/method for calculating the total commission based on the input criteria (sales_rep_name, start_date, end_date)
  * Helper functions/methods as needed to ensure readable code that is easy to troubleshoot
* Basic unit tests for the functions/methods above
* No need to include error handling in your solution, but sharing your thoughts on how you could during the interview is great

### Examples of Final Output

```{python}
calculate_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-4-30") =  55350.00

calculate_commission(sales_rep_name="David", start_date="2023-04-01", end_date="2023-06-30") = 89540.00

calculate_commission(sales_rep_name="Poppy", start_date="2023-03-01", end_date="2023-5-30") = 118190.00
```

## What We Are Looking For

* Clean and readable code
* Object-oriented programing that separates out smaller steps into easy to trouble shoot methods.
* The functions/methods you create have unit tests
* Code should be self contained, meaning someone else should have every thing in the repo they would need in order to run the code (locally or deployed with a production service).
  * Package requirements are included
  * Test are contained in the repo
  * README.md has basic summary of how the code works and steps needed to run

## What to Expect

* This coding exercise should take roughly 1-4 hours of effort to complete.
* For the working interview (~1 hour duration), you will have the chance to explain your solution and discuss your thought process behind your code.
* The second part of the working interview will consist of a product/feature enhancement to your solution. This will allow you to do a little bit of live coding with the interviewer while getting a feel for what working together could be like.


## How to Submit

1. Clone this repo **(don't fork)**
2. Set the GitHub origin to the newly cloned repo under your account
3. Commit your coding solution to your cloned repo
4. Email the link to your GitHub repo to the recruiting team or hiring manager you have been in contact during the earlier phases of the interview

Thank you for taking the time to complete this coding assessment! Don't stress too much about any one thing, we evaluate the exercises holistically.
