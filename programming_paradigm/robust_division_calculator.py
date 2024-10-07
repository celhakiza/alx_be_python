# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division of two numbers with error handling.

    Parameters:
    - numerator (str or float): The numerator for division.
    - denominator (str or float): The denominator for division.

    Returns:
    - str: Result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
