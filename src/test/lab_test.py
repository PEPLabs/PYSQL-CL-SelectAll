import unittest

from src.main.song import Song
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_get_all_songs(self):
        """
        In this test we have a hardcoded version of the song table in Python.
        This test calls the function with the SQL syntax that you wrote and then compares it to the hardcoded
        list here, if they are the same then the test passes.
        """
        # arrange
        expected_result = [
            Song("Let it be", "Beatles"),
            Song("Hotel California", "Eagles"),
            Song("Kashmir", "Led Zeppelin"),
        ]

        # act
        actual_result = problem1()

        # assert
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
