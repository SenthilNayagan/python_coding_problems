import unittest

from coding_problems.string_exercises import StringExercises


class TestStringExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        pass

    def test_string_multiplication(self):
        self.assertEqual(StringExercises.string_multiplication("Hi", 3), "HiHiHi")
        self.assertEqual(StringExercises.string_multiplication("10 ", 2), "10 10 ")
        self.assertEqual(StringExercises.string_multiplication("", 2), "")
        self.assertEqual(StringExercises.string_multiplication("Hello", 1), "Hello")


if __name__ == "__main__":
    unittest.main()
