import unittest

from coding_problems.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        pass

    def test_binary_search(self):
        self.assertEqual(BinarySearch.binary_search(self.nums, "Found"))
        self.assertEqual(BinarySearch.binary_search(self.nums, "Not found"))

    def test_binary_search_recursive(self):
        self.assertEqual(BinarySearch.binary_search_recursive(self.nums, 0, len(self.nums) -1, 7))
        self.assertEqual(BinarySearch.binary_search_recursive(self.nums, 0, len(self.nums) -1, 10))


if __name__ == "__main__":
    unittest.main()
