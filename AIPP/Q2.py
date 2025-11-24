def calc(a, b):
    c = a + b
    d = c * 2
    return d
def calculate_double_sum(a, b):
    """
    Calculate double of the sum of two numbers.

    Args:
        a (int or float): First input number.
        b (int or float): Second input number.

    Returns:
        int or float: Double the value of (a + b).

    Example:
        calculate_double_sum(2, 3) → 10
    """
    # Add both numbers
    total = a + b

    # Multiply the result by 2
    result = total * 2

    return result


# ------------- Testing ---------------

print(calculate_double_sum(5, 7))
print(calculate_double_sum(-1, 4))
