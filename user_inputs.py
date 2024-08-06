"""
This module provides utility functions to handle user inputs for interest-rate calculation , ensuring that all inputs are correctly formatted and valid before processing. The module facilitates the collection of date and floating-point number inputs from users, applying rigorous validation to maintain data integrity and prevent errors during subsequent calculations.

Functions:
- get_date_input(prompt): Requests and validates a user-inputted date, ensuring it conforms to the 'YYYY-MM-DD' format. This function is essential for applications requiring precise date specifications, such as calculating durations or scheduling future financial events.
- get_float_input(prompt): Prompts the user for a floating-point number and validates that it is a positive value, converting user input to numpy's float64 for high precision in financial calculations.

The functions in this module are designed with robust error handling to prevent common input errors such as incorrect formats and negative values. These utilities support a seamless user experience by providing clear error messages and continuously prompting for corrections until valid inputs are received.

Usage:
These input functions are intended to be directly invoked wherever user input is required in financial applications, particularly those involving date and monetary calculations. By centralizing input handling in this module, developers can ensure consistent validation logic across their applications, enhancing maintainability and scalability.

Examples of usage and detailed error handling are included within each function's docstring to facilitate easy integration and troubleshooting during development.

Name: Nedal Altiti
Date: 2024-08-06
"""

from datetime import datetime
import numpy as np


def get_date_input(prompt):
    """
    Safely retrieve a date input from the user, ensuring it is correctly formatted.

    Args:
        prompt (str): The prompt message displayed to the user asking for a date.

    Returns:
        str: A valid date string in YYYY-MM-DD format.
    """
    while True:
        date_input = input(prompt)
        try:
            valid_date = datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format. Example: 1998-11-10")
            continue  # Prompt again right here without breaking the workflow

def get_float_input(prompt):
    """
    Safely retrieve a float input from the user, ensuring it is a positive number.

    Args:
        prompt (str): The prompt message displayed to the user.

    Returns:
        float: A valid, positive floating-point number entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            value = np.float64(user_input.replace(',', ''))
            if value < 0:
                raise ValueError("The entered value must be positive. Negative values are not allowed.")
            return value
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Invalid input: Please enter a numeric value.")
            else:
                print(f"Invalid input: {e}. Please enter a positive number.")
            continue  # Prompt again right here without breaking the workflow
