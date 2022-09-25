import unittest

from coding_problems.find_factorial import Factorial


class TestFactorial(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        pass

    def tearDown(self):
        pass

    def test_find_factorial_bf(self):
        self.assertEqual(Factorial.find_factorial_bf(5), 120)
        self.assertEqual(Factorial.find_factorial_bf(23), 25852016738884976640000)

        self.assertEqual(Factorial.find_factorial_recursive(5), 120)
        self.assertEqual(Factorial.find_factorial_recursive(23), 25852016738884976640000)


if __name__ == "__main__":
    unittest.main()
