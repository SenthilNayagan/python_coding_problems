import unittest

from coding_problems.remove_duplicates_int_array import RemoveDuplicatesIntArray


class TestRemoveDuplicatesIntArray(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.lst_of_nums_1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
        self.lst_of_nums_2 = [1, 1, 1, 1, 1, 1, 1, 1]

    def tearDown(self):
        pass

    def test_remove_duplicates_bf(self):
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_bf(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_bf(self.lst_of_nums_2), [1])
        self.assertNotEqual(RemoveDuplicatesIntArray.remove_duplicates_bf(self.lst_of_nums_2), [])

    def test_remove_duplicates_sorted(self):
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_sorted(self.lst_of_nums_1), [1, 2, 3, 4, 5])
        self.assertNotEqual(RemoveDuplicatesIntArray.remove_duplicates_sorted(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_sorted(self.lst_of_nums_2), [1])
        self.assertNotEqual(RemoveDuplicatesIntArray.remove_duplicates_sorted(self.lst_of_nums_2), [])

    def test_remove_duplicates_hash(self):
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_hash(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(RemoveDuplicatesIntArray.remove_duplicates_hash(self.lst_of_nums_2), [1])
        self.assertNotEqual(RemoveDuplicatesIntArray.remove_duplicates_hash(self.lst_of_nums_2), [])


if __name__ == "__main__":
    unittest.main()

