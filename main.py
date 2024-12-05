import math


def calculate_square_root(number):
    if not isinstance(number, (int, float)) or number < 0:
        return "Invalid Input"
    return math.sqrt(number)
