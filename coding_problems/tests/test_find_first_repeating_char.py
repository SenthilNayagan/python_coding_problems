import unittest

from coding_problems.find_first_repeating_char import FindRepeatingChar


class TestFindRepeatingChar(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        pass

    def tearDown(self):
        pass

    def test_first_repeating_character_bf(self):
        self.assertEqual(FindRepeatingChar.first_repeating_character_bf("inside code"), 'i')  # returns 'i'
        self.assertEqual(FindRepeatingChar.first_repeating_character_bf("programming"), 'r')  # returns 'r'
        self.assertEqual(FindRepeatingChar.first_repeating_character_bf("abcd"), '\0')  # returns '\0'

    def test_first_repeating_character_hash(self):
        self.assertEqual(FindRepeatingChar.first_repeating_character_hash("inside code"), 'i')  # returns 'i'
        self.assertEqual(FindRepeatingChar.first_repeating_character_hash("programming"), 'r')  # returns 'r'
        self.assertEqual(FindRepeatingChar.first_repeating_character_hash("abcd"), '\0')  # returns '\0'


if __name__ == "__main__":
    unittest.main()
