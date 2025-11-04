"""
calculator.py

A simple calculator module provides a `Calculator` class for performing
basic arithmetic operations.

"""


class Calculator:
    """
    A calculator class for basic arithmetic operations.
    Class supports operations: addition, subtraction,multiplication, and
    division between two numeric operands. Before performing any operation,
    the operands are validated to ensure they are numeric
    types (`int` or `float`).

    Attributes:
        __op1: The first operand.
        __op2: The second operand.

    Methods:
        __check_values(): Validate that the operands are numeric types.
        sum(): Return the sum of the two operands.
        subtract(): Return the difference between the two operands.
        multiply(): Return the product of the two operands.
        divide(): Return the quotient of two operands.

    """
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def __check_values(self):
        """
        Validate that the operands are numeric types.

        This method checks whether both `self.__op1` and `self.__op2` are
        instances of `int` or `float`. If either operand is not numeric,
        `TypeError` is raised with an explanatory message.

        Raises:
            TypeError: If either `self.__op1` or `self.__op2`
            is not an int or float.

        """
        if not (isinstance(self.__op1, (int, float))
                and isinstance(self.__op2, (int, float))):
            raise TypeError

    def sum(self):
        """
        Return the sum of the two operands.

        Raises:
            TypeError: If one of the operands is not a number.

        """
        try:
            self.__check_values()
            return self.__op1 + self.__op2
        except TypeError:
            return "Both operands must be numbers"

    def subtract(self):
        """
        Return the difference between the two operands.

        Raises:
            TypeError: If one of the operands is not a number.

        """
        try:
            self.__check_values()
            return self.__op1 - self.__op2
        except TypeError:
            return "Both operands must be numbers"

    def multiply(self):
        """
        Return the product of two operands.

        Raises:
            TypeError: If one of the operands is not a number.

        """
        try:
            self.__check_values()
            return self.__op1 * self.__op2
        except TypeError:
            return "Both operands must be numbers"

    def divide(self):
        """
        Return the quotient of two operands.

        Raises:
            ZeroDivisionError: If the second operand is zero.
            TypeError: If one of the operands is not a number.

        """
        try:
            self.__check_values()
            return self.__op1 / self.__op2
        except ZeroDivisionError:
            return "You cannot divide by zero"
        except TypeError:
            return "Both operands must be numbers"


if __name__ == "__main__":
    calculator = Calculator(10, 2)
    calculator.sum()
    calculator.subtract()
    calculator.multiply()
    calculator.divide()
