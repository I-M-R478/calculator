import math
import ast

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    def square_root(self, num):
        if num < 0:
            return "Error: Negative value"
        return math.sqrt(num)

    def exponentiate(self, base, exponent):
        return math.pow(base ** exponent)

    def logarithm(self, num, base=10):
        if num <= 0 or base <= 0:
            return "Error: Invalid input for logarithm
        return math.log(num, base)    

    def factorial(self, num):
        if num < 0:
            return "Error: Factorial of negative number doesn't exist"
        return math.factorial(num)

    def sin(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        return math.sin(angle_radians)

    def cos(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        return math.cos(angle_radians)

    def tan(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        return math.tan(angle_radians)

    def calculate(self, expression):
        try:
            result = ast.literal_eval(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {str(e)}"
