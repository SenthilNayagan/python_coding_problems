import unittest

from coding_problems.regex_exercises import RegExExercises


class TestRegExExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.obj = RegExExercises()
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        self.obj = None

    def test_sum_nums_start_with_one(self):
        self.assertEqual(self.obj.sum_nums_start_with_one(1, 20), 146)
        self.assertEqual(self.obj.sum_nums_start_with_one(1, 10), 11)


if __name__ == "__main__":
    unittest.main()
