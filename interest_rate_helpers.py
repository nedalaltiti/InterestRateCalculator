"""
This module contains functions for calculating the duration between dates and determining interest rates for debts based on given financial parameters. The module is designed to assist in financial analyses by providing tools to compute both compound and simple interest rates. Each function within the module is equipped with robust error handling to ensure accurate and reliable calculations.

Functions:
- calculate_duration_in_years(start_date, end_date): Computes the duration in years between two provided dates, with results cached for efficiency.
- calculate_compound_interest_rate(principal, amount, time_years, n): Calculates the compound interest rate given the principal, the current amount, the duration in years, and the number of compounding periods per year.
- calculate_simple_interest_rate(principal, amount, time_years): Calculates the simple interest rate given the principal, the current amount, and the duration in years.

Each function includes detailed error handling to manage and respond to various input errors, ensuring that calculations are performed only with valid and logical data inputs. This module is intended for use in financial systems where accurate interest rate predictions are crucial for decision-making processes.

Usage:
The functions in this module are designed to be imported and utilized in interest_rate_calculator_runner script where understanding the impact of interest over time is critical.

Examples and exceptions are documented within each function's docstring to aid in correct implementation and troubleshooting during development and deployment of the project.

Name: Nedal Altiti
Date: 2024-08-06
"""

import numpy as np
from datetime import datetime
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None means unlimited caching, adjust as needed for memory management
def calculate_duration_in_years(start_date, end_date):
    """
    Calculate the duration between two dates in years, accounting for leap years. Results are cached to improve efficiency
    for repeated calculations with the same dates.
    
    Args:
        start_date (str): The start date in "YYYY-MM-DD" format.
        end_date (str): The end date in "YYYY-MM-DD" format.
    
    Returns:
        float: The duration between the dates in years.
    
    Raises:
        ValueError: If the start date is not earlier than the end date.
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    if start >= end:
        raise ValueError("The start date must be earlier than the end date.")

    duration_days = (end - start).days
    return np.float64(duration_days) / 365.25  # Using 365.25 to account for leap years

def calculate_compound_interest_rate(principal, amount, time_years, n):
    """
    Calculate the compound interest rate based on the principal, amount, duration, and compounding frequency.

    Args:
        principal (float): The original amount of the debt.
        amount (float): The current amount of the debt.
        time_years (float): The time in years between the original and current amounts.
        n (int): The number of compounding periods per year.

    Returns:
        float: The annual compound interest rate in percentage.

    Raises:
        ValueError: If any of the inputs are logically incorrect or out of reasonable bounds.
    """
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if amount < 0:
        raise ValueError("Current amount cannot be negative.")
    if time_years <= 0:
        raise ValueError("Time in years must be greater than zero.")
    if n <= 0:
        raise ValueError("Number of compounding periods per year must be greater than zero.")
    if amount == principal:
        return 0  # No interest has accrued if the amount hasn't changed

    # Calculate the compound interest rate using the formula
    try:
        rate = n * (np.power(np.float64(amount) / principal, 1 / (n * time_years)) - 1) * 100
    except Exception as e:
        raise RuntimeError(f"Failed to calculate interest rate: {str(e)}")

    return rate



def calculate_simple_interest_rate(principal, amount, time_years):
    """
    Calculate the simple interest rate based on the principal, the current amount, and the duration in years.

    Args:
        principal (float): The original amount of the debt.
        amount (float): The current amount of the debt.
        time_years (float): The time in years between the original and current amounts.

    Returns:
        float: The annual simple interest rate in percentage.

    Raises:
        ValueError: If any of the inputs are logically incorrect or out of reasonable bounds.
    """
    # Validate the inputs to ensure they are logically correct
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if amount < principal:
        raise ValueError("Current amount cannot be less than the principal, assuming interest accrues.")
    if time_years <= 0:
        raise ValueError("Time in years must be greater than zero.")

    # Check for no change in amount, which implies no interest
    if amount == principal:
        return 0

    # Calculate the simple interest rate using the formula
    try:
        rate = (np.float64(amount) - principal) / (principal * time_years) * 100
    except Exception as e:
        raise RuntimeError(f"Failed to calculate interest rate: {str(e)}")

    return rate