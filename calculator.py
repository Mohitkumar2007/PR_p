"""A simple calculator utility for basic arithmetic operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference between a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    return a / b


if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"7 - 4 = {subtract(7, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"8 / 2 = {divide(8, 2)}")
