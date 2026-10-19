"""Unit tests for save_scores, using tearDown to delete the file."""

import os
import unittest

from score_saver import save_scores

TEST_FILE = "test_scores.txt"


class TestSaveScores(unittest.TestCase):
    """Each test writes a file; tearDown always deletes it."""

    def tearDown(self) -> None:
        """Runs AFTER each test, even if the test failed."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_file_is_created(self) -> None:
        """After saving, the file exists."""
        save_scores(TEST_FILE, [90, 75])
        self.assertTrue(os.path.exists(TEST_FILE))

    def test_one_score_per_line(self) -> None:
        """Each score is on its own line."""
        save_scores(TEST_FILE, [90, 75])
        with open(TEST_FILE) as file:
            self.assertEqual(file.read(), "90\n75\n")


if __name__ == "__main__":
    unittest.main()
