import unittest

from coding_problems.binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]
        self.seq = [5, 2, 8, 7, 3, 1, 9, 4, 6]

    def tearDown(self):
        pass

    def test_binary_search(self):
        self.assertEqual(BinarySearch.binary_search(self.seq, 7), "Found")
        self.assertEqual(BinarySearch.binary_search(self.seq, 10), "Not found")

    def test_binary_search_recursive(self):
        self.assertEqual(BinarySearch.binary_search_recursive(self.seq, 0, len(self.seq)-1, 2), "Found")
        self.assertEqual(BinarySearch.binary_search_recursive(self.seq, 0, len(self.seq)-1, 10), "Not found")


if __name__ == "__main__":
    unittest.main()
