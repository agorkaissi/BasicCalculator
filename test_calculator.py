import pytest
from calculator import Calculator

class TestCalculator:
    @pytest.mark.parametrize("op1, op2, expected", [
        (-5, -10, -15), # negative numbers
        (5, 10, 15),    # positive numbers
        (-5, 10, 5),    # op1 negative, op2 positive
        (5, -10, -5),   # op1 positive, op2 negative
        (0, 2, 2),      # sum with zero: op1
        (2, 0, 2),      # sum with zero: op2
    ])

    def test_sum_parametrized(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.sum() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        ("op1", 3, "Both operands must be numbers"),
        (5, "op2", "Both operands must be numbers"),
        (None, 10, "Both operands must be numbers"),
        ([2, 3], 4, "Both operands must be numbers"),
        ({"x": 1}, 2, "Both operands must be numbers")
    ])

    def test_sum_invalid_value(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.sum() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        (-2, -5, 3),    # negative numbers
        (10, 5, 5),     # positive numbers
        (-5, 10, -15),  # op1 negative, op2 positive
        (5, -10, 15),   # op1 positive, op2 negative
        (0, 5, -5),     # subtract with zero: op1
        (5, 0, 5),      # subtract with zero: op2
    ])

    def test_subtract_parametrized(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.subtract() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        ("op1", 3, "Both operands must be numbers"),
        (5, "op2", "Both operands must be numbers"),
        (None, 10, "Both operands must be numbers"),
        ([2, 3], 4, "Both operands must be numbers"),
        ({"x": 1}, 2, "Both operands must be numbers")
    ])

    def test_subtract_invalid_value(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.subtract() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        (-2, -3, 6),    # negative numbers
        (4, 5, 20),     # positive numbers
        (-5, 10, -50),  # op1 negative, op2 positive
        (5, -10, -50),  # op1 positive, op2 negative
        (1.5, 1.5, 2.25),  # float numbers multiplication
        (0, 5, 0),      # multiplication with zero: op1
        (5, 0, 0),      # multiplication with zero: op2
    ])

    def test_multiply_parametrized(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.multiply() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        ("op1", 3, "Both operands must be numbers"),
        (5, "op2", "Both operands must be numbers"),
        (None, 10, "Both operands must be numbers"),
        ([2, 3], 4, "Both operands must be numbers"),
        ({"x": 1}, 2, "Both operands must be numbers")
    ])

    def test_multiply_invalid_value(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.multiply() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        (-10, -2, 5),   # negative numbers
        (10, 5, 2),     # positive numbers
        (-20, 10, -2),  # op1 negative, op2 positive
        (15, -3, -5),   # op1 positive, op2 negative
        (17.5, 2.5, 7), # float numbers multiplication
        (7.5, 3, 2.5),  # float result
    ])

    def test_divide_parametrized(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.divide() == expected

    @pytest.mark.parametrize("op1, op2, expected", [
        ("op1", 3, "Both operands must be numbers"),
        (5, "op2", "Both operands must be numbers"),
        (None, 10, "Both operands must be numbers"),
        ([2, 3], 4, "Both operands must be numbers"),
        ({"x": 1}, 2, "Both operands must be numbers"),
        (5, 0, "You cannot divide by zero")
    ])

    def test_divide_invalid_value(self, op1, op2, expected):
        calculator = Calculator(op1, op2)
        assert calculator.divide() == expected
