import unittest

from coding_problems.filter_exercises import FilterExercises


class TestFilterExercises(unittest.TestCase):
    """Testcases for FindPairSum."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        pass

    def test_find_even_numbers(self) -> 'even numbers':
        self.assertEqual(FilterExercises.find_even_numbers(self.nums), [4, 8, 12])
        self.assertNotEqual(FilterExercises.find_even_numbers(self.nums), [6, 5, 6, 9])

    def test_extract_vowels(self) -> 'list-of-vowels':
        self.assertEqual(FilterExercises.extract_vowels(self.fruits[3]), ['i', 'e', 'a', 'e'])
        self.assertEqual(FilterExercises.extract_vowels(self.fruits[2]), ['a', 'a', 'a'])


if __name__ == "__main__":
    unittest.main()
