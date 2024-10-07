import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for Addition
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)   # Test positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Test negative + positive
        self.assertEqual(self.calc.add(-1, -1), -2) # Test negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)   # Test zeros

    # Test for Subtraction
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)    # Test positive numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)   # Test negative numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)    # Test zero from positive
        self.assertEqual(self.calc.subtract(5, 0), 5)     # Test positive from zero

    # Test for Multiplication
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 5), 15)   # Test positive numbers
        self.assertEqual(self.calc.multiply(-1, 5), -5)  # Test negative * positive
        self.assertEqual(self.calc.multiply(0, 5), 0)    # Test multiplication by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Test negative * negative

    # Test for Division
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)    # Test positive division
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Test negative/positive
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Test negative/negative
        self.assertEqual(self.calc.divide(0, 1), 0)     # Test zero numerator

        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))       # Expect None for divide by zero
        self.assertIsNone(self.calc.divide(-5, 0))      # Test with negative numerator

if __name__ == '__main__':
    unittest.main()
