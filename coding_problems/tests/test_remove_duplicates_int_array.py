import unittest

from coding_problems.remove_duplicates_int_array import RemoveDuplicatesIntArray


class TestRemoveDuplicatesIntArray(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.lst_of_nums_1 = [4, 2, 5, 3, 3, 1, 2, 4, 1, 5, 5, 5, 3, 1]
        self.lst_of_nums_2 = [1, 1, 1, 1, 1, 1, 1, 1]
        self.obj = RemoveDuplicatesIntArray()

    def tearDown(self):
        pass

    def test_remove_duplicates_bf(self):
        self.assertEqual(self.obj.remove_duplicates_bf(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(self.obj.remove_duplicates_bf(self.lst_of_nums_2), [1])
        self.assertNotEqual(self.obj.remove_duplicates_bf(self.lst_of_nums_2), [])

    def test_remove_duplicates_sorted(self):
        self.assertEqual(self.obj.remove_duplicates_sorted(self.lst_of_nums_1), [1, 2, 3, 4, 5])
        self.assertNotEqual(self.obj.remove_duplicates_sorted(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(self.obj.remove_duplicates_sorted(self.lst_of_nums_2), [1])
        self.assertNotEqual(self.obj.remove_duplicates_sorted(self.lst_of_nums_2), [])

    def test_remove_duplicates_hash(self):
        self.assertEqual(self.obj.remove_duplicates_hash(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(self.obj.remove_duplicates_hash(self.lst_of_nums_2), [1])
        self.assertNotEqual(self.obj.remove_duplicates_hash(self.lst_of_nums_2), [])

    def test_remove_duplicates_list_comp(self):
        self.assertEqual(self.obj.remove_duplicates_list_comp(self.lst_of_nums_1), [4, 2, 5, 3, 1])
        self.assertEqual(self.obj.remove_duplicates_list_comp(self.lst_of_nums_2), [1])
        self.assertNotEqual(self.obj.remove_duplicates_list_comp(self.lst_of_nums_2), [])

    def test_remove_duplicates_using_set(self):
        # Note: Set is an unordered data structure, so it does not preserve the insertion order.
        self.assertEqual(self.obj.remove_duplicates_using_set(self.lst_of_nums_1), [1, 2, 3, 4, 5])
        self.assertEqual(self.obj.remove_duplicates_using_set(self.lst_of_nums_2), [1])
        self.assertNotEqual(self.obj.remove_duplicates_using_set(self.lst_of_nums_2), [])


if __name__ == "__main__":
    unittest.main()

