import unittest

from coding_problems.numbers_exercises import NumbersExercises


class TestNumbersExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.obj = NumbersExercises()
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]
        self.nums_with_zeros = [2, 6, 0, 7, 1, 0, 0, 4, 3]
        self.nested_list = [[1], [2, 3], [4, 5, 6, 7]]
        self.num = 1234

    def tearDown(self):
        self.obj = None

    def test_swap_values(self):
        self.assertEqual(self.obj.swap_values(2, 4), (4, 2))
        self.assertEqual(self.obj.swap_values(10, 10), (10, 10))
        self.assertEqual(self.obj.swap_values(0, 10), (10, 0))

    def test_flatten_nested_list(self):
        self.assertEqual(self.obj.flatten_nested_list(self.nested_list), [1, 2, 3, 4, 5, 6, 7])

    def test_find_max(self):
        self.assertEqual(self.obj.find_max(self.nums), 12)
        self.assertNotEqual(self.obj.find_max(self.nums), 2)

    def test_add_two_lists(self):
        self.assertEqual(self.obj.add_two_lists([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 1])
        self.assertEqual(self.obj.add_two_lists([4, 7, 1], [8, 1]), [2, 9, 1])

    def test_reverse_number(self):
        self.assertEqual(self.obj.reverse_number_bad_smell(self.num), 4321)
        self.assertEqual(self.obj.reverse_number_bad_smell(1), 1)
        self.assertEqual(self.obj.reverse_number_bad_smell(0), 0)

        self.assertEqual(self.obj.reverse_number_optimized(-2456), -6542)

    def test_move_zeros_towards_end(self):
        self.assertEqual(self.obj.move_zeros_towards_end(self.nums_with_zeros), [2, 6, 7, 1, 4, 3, 0, 0, 0])
        self.assertEqual(self.obj.move_zeros_towards_end([2, 0, 1, 8]), [2, 1, 8, 0,])
        self.assertEqual(self.obj.move_zeros_towards_end([0, 0, 0]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
