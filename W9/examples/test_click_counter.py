"""Unit tests for ClickCounter, using setUp for a fresh counter."""

import unittest

from click_counter import ClickCounter


class TestClickCounter(unittest.TestCase):
    """Every test starts with its own brand-new counter."""

    def setUp(self) -> None:
        """Runs BEFORE each test method."""
        self.counter = ClickCounter()

    def test_starts_at_zero(self) -> None:
        """A new counter shows 0."""
        self.assertEqual(self.counter.value(), 0)

    def test_three_clicks(self) -> None:
        """Three clicks show 3."""
        self.counter.click()
        self.counter.click()
        self.counter.click()
        self.assertEqual(self.counter.value(), 3)

    def test_reset_goes_back_to_zero(self) -> None:
        """reset() undoes all clicks."""
        self.counter.click()
        self.counter.reset()
        self.assertEqual(self.counter.value(), 0)


if __name__ == "__main__":
    unittest.main()
