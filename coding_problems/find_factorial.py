"""
Find factorial for the given number.

For example, if the given number is 5, then the factorial for 5 is 1 * 2 * 3 * 4 * 5 = 120
"""


class Factorial(object):
    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def find_factorial_bf(n):
        """Brute force approach, which uses n iterations.

        Time complexity: O(n)
        Space complexity: O(n) - Because we store the factorial in a separate variable
        """
        factorial = 1
        if n == 1:
            return 1
        else:
            for i in range(1, n + 1):
                factorial *= i  # same as factorial = factorial * i
        return factorial

    @staticmethod
    def find_factorial_recursive(n):
        """Finds factorial using recursion.

        Time complexity: O(n)
        Space complexity: O(n) - Because every call to the recursive function, the state is saved onto the call stack.
        """
        if n == 1:
            return 1
        else:
            return n * Factorial.find_factorial_recursive(n - 1)


if __name__ == "__main__":
    print(Factorial.find_factorial_bf(5))
