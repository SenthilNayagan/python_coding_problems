import unittest

from coding_problems.find_pair_sums_given_val import FindPairSum


class TestFindPairSum(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.nums = [4, 1, 5, -3, 6]

    def tearDown(self):
        pass

    def test_find_pair_bf(self):
        self.assertTrue(FindPairSum.find_pair_bf(self.nums, 11))
        self.assertFalse(FindPairSum.find_pair_bf(self.nums, -4))
        self.assertTrue(FindPairSum.find_pair_bf(self.nums, -2))

    def test_find_pair_sorted(self):
        self.assertTrue(FindPairSum.find_pair_sorted(self.nums, 11))
        self.assertFalse(FindPairSum.find_pair_sorted(self.nums, -4))
        self.assertTrue(FindPairSum.find_pair_sorted(self.nums, -2))


if __name__ == "__main__":
    unittest.main()