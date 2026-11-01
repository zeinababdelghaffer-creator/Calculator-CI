import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):

    # Addition tests
    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(5, 3, "+"), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(calculate(-5, -3, "+"), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(calculate(-5, 3, "+"), -2)

    def test_addition_with_zero(self):
        self.assertEqual(calculate(5, 0, "+"), 5)

    def test_addition_decimal_numbers(self):
        self.assertAlmostEqual(calculate(1.5, 2.5, "+"), 4.0)

    # Subtraction tests
    def test_subtraction_positive_numbers(self):
        self.assertEqual(calculate(8, 3, "-"), 5)

    def test_subtraction_result_is_negative(self):
        self.assertEqual(calculate(3, 8, "-"), -5)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(calculate(-3, -8, "-"), 5)

    def test_subtraction_with_zero(self):
        self.assertEqual(calculate(5, 0, "-"), 5)

    def test_subtraction_decimal_numbers(self):
        self.assertAlmostEqual(calculate(2.5, 1.5, "-"), 1.0)

    # Multiplication tests
    def test_multiplication_positive_numbers(self):
        self.assertEqual(calculate(4, 3, "*"), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(calculate(-4, 3, "*"), -12)

    def test_multiplication_with_zero(self):
        self.assertEqual(calculate(10, 0, "*"), 0)

    def test_multiplication_decimal_numbers(self):
        self.assertAlmostEqual(calculate(1.5, 2, "*"), 3.0)

    # Division tests
    def test_division_exact_result(self):
        self.assertEqual(calculate(8, 2, "/"), 4)

    def test_division_decimal_result(self):
        self.assertEqual(calculate(7, 2, "/"), 3.5)

    def test_division_negative_number(self):
        self.assertEqual(calculate(-8, 2, "/"), -4)

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, "/")

    # Invalid operations and inputs "Negative Testing"
    def test_unsupported_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(5, 2, "//")

    def test_empty_operation_raises_error(self):
        with self.assertRaises(ValueError):
            calculate(5, 2, "")

    def test_string_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate("5", 2, "+")

    def test_none_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate(None, 2, "+")

    def test_boolean_operand_raises_error(self):
        with self.assertRaises(TypeError):
            calculate(True, 2, "+")


if __name__ == "__main__":
    unittest.main()
