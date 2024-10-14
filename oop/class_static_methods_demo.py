# Calculator class demonstrating static and class methods
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: Does not use any class or instance data
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: Uses the class itself through the cls parameter
    @classmethod
    def multiply(cls, a, b):
        # Access class attribute calculation_type
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
