import unittest

from coding_problems.bubble_sort import BubbleSort


class TestBubbleSort(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.obj = BubbleSort()
        self.seq = [5, 2, 8, 7, 3, 1, 9, 4, 6]

    def tearDown(self):
        self.seq = None

    def test_bubble_sort_with_iteration_count(self):
        self.assertEqual(self.obj.bubble_sort_with_iteration_count(self.seq), ([1, 2, 3, 4, 5, 6, 7, 8, 9], 36))
        self.assertEqual(self.obj.bubble_sort_with_iteration_count([5, 2, 3, 1]), ([1, 2, 3, 5], 6))
        self.assertEqual(self.obj.bubble_sort_with_iteration_count([2, 1]), ([1, 2], 1))
        self.assertEqual(self.obj.bubble_sort_with_iteration_count([0]), ([0], 0))


if __name__ == "__main__":
    unittest.main()
