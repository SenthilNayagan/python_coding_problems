import unittest

from coding_problems.numbers_exercises import NumbersExercises


class TestNumbersExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        pass

    def test_swap_values(self):
        self.assertEqual(NumbersExercises.swap_values(2, 4), (4, 2))
        self.assertEqual(NumbersExercises.swap_values(10, 10), (10, 10))
        self.assertEqual(NumbersExercises.swap_values(0, 10), (10, 0))


if __name__ == "__main__":
    unittest.main()
