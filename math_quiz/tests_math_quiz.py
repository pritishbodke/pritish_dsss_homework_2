import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result
function_C = calculate_result
function_A = generate_random_integer 
function_B = generate_random_operator
class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of the expected operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = function_B()
            self.assertIn(operator, operators)

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 4, '*', '3 * 4', 12),
            (8, 3, '-', '8 - 3', 5),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
