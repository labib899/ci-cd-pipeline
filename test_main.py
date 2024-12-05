from main import calculate_square_root


def test_calculate_square_root():
    assert calculate_square_root(16) == 4.0
    assert calculate_square_root(0) == 0.0
    assert calculate_square_root(-4) == "Invalid Input"
    assert calculate_square_root("string") == "Invalid Input"
