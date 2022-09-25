import unittest

from coding_problems.numbers_exercises import NumbersExercises


class TestNumbersExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]
        self.nested_list = [[1], [2, 3], [4, 5, 6, 7]]
        self.num = 1234

    def tearDown(self):
        pass

    def test_swap_values(self):
        self.assertEqual(NumbersExercises.swap_values(2, 4), (4, 2))
        self.assertEqual(NumbersExercises.swap_values(10, 10), (10, 10))
        self.assertEqual(NumbersExercises.swap_values(0, 10), (10, 0))

    def test_flatten_nested_list(self):
        self.assertEqual(NumbersExercises.flatten_nested_list(self.nested_list), [1, 2, 3, 4, 5, 6, 7])

    def test_find_max(self):
        self.assertEqual(NumbersExercises.find_max(self.nums), 12)
        self.assertNotEqual(NumbersExercises.find_max(self.nums), 2)

    def test_add_two_lists(self):
        self.assertEqual(NumbersExercises.add_two_lists([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 1])
        self.assertEqual(NumbersExercises.add_two_lists([4, 7, 1], [8, 1]), [2, 9, 1])

    def test_reverse_number(self):
        self.assertEqual(NumbersExercises.reverse_number_bad_smell(self.num), 4321)
        self.assertEqual(NumbersExercises.reverse_number_bad_smell(1), 1)
        self.assertEqual(NumbersExercises.reverse_number_bad_smell(0), 0)

        self.assertEqual(NumbersExercises.reverse_number_optimized(-2456), -6542)


if __name__ == "__main__":
    unittest.main()
