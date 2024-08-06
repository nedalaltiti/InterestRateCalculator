"""
This script serves as the main entry point for the Interest Rate Calculator application. It utilizes utility functions from `user_inputs.py` to gather necessary data from the user and employs calculation functions from `interest_rate_helpers.py` to compute the interest rates for various types of debts. The script manages user interactions, processes input data, and displays the computed interest rates, providing a comprehensive tool for financial analysis regarding debt settlement.

Features:
- Collects date and financial inputs directly from the user.
- Determines the type of interest calculation (compound or simple) based on the type of debt.
- Calculates the duration between two dates and uses this duration to compute the interest rate.
- Displays the calculated interest rate to the user in a clear and precise format.

Workflow:
1. Prompt the user for the necessary dates, amounts, and debt type.
2. Use these inputs to calculate the time span in years between the given dates.
3. Determine the appropriate interest rate calculation method based on the specified debt type.
4. Calculate and display the annual interest rate for the given debt.

The script supports calculations for both compound and simple interest, distinguishing between debt types like Credit Cards and Installment Loans. This enables accurate financial planning and analysis for users looking to understand the implications of different interest accrual methods on their debts.

Usage:
Run this script from the command line to start the interactive Interest Rate Calculator. The user will be guided through a series of inputs before receiving the calculated interest rate based on their specific circumstances.

Name: Nedal Altiti
Date: 2024-08-06
"""

from user_inputs import get_date_input, get_float_input
from interest_rate_helpers import calculate_duration_in_years, calculate_compound_interest_rate, calculate_simple_interest_rate

def main():
    print("Welcome to the Interest Rate Calculator!")

    principal_date = get_date_input("Enter the date for the original amount of the debt (YYYY-MM-DD): ")
    current_date = get_date_input("Enter the date for the current amount of the debt (YYYY-MM-DD): ")
    principal = get_float_input("Enter the original amount of the debt (principal): ")
    amount = get_float_input("Enter the current amount of the debt: ")
    debt_type = input("Enter the type of debt (e.g., Credit Card, Federal Credit Union, Installment, Collections, etc.): ")

    # Calculate the duration in years between the two dates
    time_years = calculate_duration_in_years(principal_date, current_date)

    # Define debt categories that use compound interest and assume daily compounding
    compound_categories = ['Credit Card', 'Federal Credit Union']
    n = 365  # Daily compounding

    if debt_type in compound_categories:
        rate = calculate_compound_interest_rate(principal, amount, time_years, n)
    else:
        rate = calculate_simple_interest_rate(principal, amount, time_years)

    print(f"The calculated annual interest rate for {debt_type} debt is: {rate:.2f}%")

if __name__ == "__main__":
    main()