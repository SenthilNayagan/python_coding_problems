import unittest

from coding_problems.find_number_of_lights import NumberOfLights


class TestNumberOfLights(unittest.TestCase):
    """Unit testcases."""
    def setUp(self) -> None:
        """Test fixture."""
        self.obj = NumberOfLights()

    def tearDown(self):
        self.obj = None

    def test_find_no_lights(self):
        self.assertEqual(self.obj.find_no_lights(12134), 18)
        self.assertEqual(self.obj.find_no_lights(-10), 0)
        self.assertEqual(self.obj.find_no_lights(0), 0)
        self.assertNotEqual(self.obj.find_no_lights(-27), 27)


if __name__ == "__main__":
    unittest.main()
