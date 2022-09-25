import unittest

from coding_problems.dictionary_exercises import DictionaryExercises


class TestStringExercises(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.dt_num = {5: 4, 1: 6, 6: 3}
        self.dt_str = {"Apple": 4, "Banana": 6, "Pineapple": 3}
        self.obj = DictionaryExercises()

    def tearDown(self):
        self.obj = None

    def test_sort_dict_by_key(self):
        print(self.obj.sort_dict_by_key(self.dt_num))
        self.assertEqual(self.obj.sort_dict_by_key(self.dt_num), {6: 3, 5: 4, 1: 6})
        self.assertEqual(self.obj.sort_dict_by_key(self.dt_str), {'Pineapple': 3, 'Apple': 4, 'Banana': 6})

    # TODO: Dictionary comparision for differently sorted dictionaries
    def test_sort_dict_by_value(self):
        self.assertEqual(self.obj.sort_dict_by_value(self.dt_num), {6: 3, 5: 4, 1: 6})
        self.assertEqual(self.obj.sort_dict_by_value(self.dt_str), {'Pineapple': 3, 'Apple': 4, 'Banana': 6})


if __name__ == "__main__":
    unittest.main()
