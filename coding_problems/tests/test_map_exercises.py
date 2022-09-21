import unittest

from coding_problems.map_exercises import MapExercises


class TestMapExercises(unittest.TestCase):
    """Testcases for FindPairSum."""
    def setUp(self) -> None:
        """Test fixture."""
        self.fruits = ["apple", "orange", "banana", "pineapple"]
        self.nums = [3, 4, 8, 9, 12, 7]

    def tearDown(self):
        pass

    def test_find_element_length(self):
        self.assertEqual(MapExercises.find_element_length(self.fruits), [5, 6, 6, 9])
        self.assertNotEqual(MapExercises.find_element_length(self.fruits), [6, 5, 6, 9])

    def test_double_numbers(self):
        self.assertEqual(MapExercises.double_numbers(self.nums), [6, 8, 16, 18, 24, 14])


if __name__ == "__main__":
    unittest.main()
