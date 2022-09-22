import unittest

from coding_problems.reduce_exercises import ReduceExercises


class TestReduceExercises(unittest.TestCase):
    """Testcases for FindPairSum."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]
        self.nested_list = [[1], [2, 3], [4, 5, 6, 7]]

    def tearDown(self):
        pass

    def test_sum_elements(self):
        self.assertEqual(ReduceExercises.sum_elements(self.nums), 43)

    def test_flatten_nested_list(self):
        self.assertEqual(ReduceExercises.flatten_nested_list(self.nested_list), [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()

