"""Unit tests for is_palindrome."""

import unittest

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Each method checks one behavior of is_palindrome."""

    def test_simple_palindrome(self) -> None:
        """A word that reads the same both ways."""
        self.assertTrue(is_palindrome("level"))

    def test_not_a_palindrome(self) -> None:
        """A word that does not read the same both ways."""
        self.assertFalse(is_palindrome("hello"))

    def test_ignores_upper_and_lower_case(self) -> None:
        """'Anna' should count, even with a capital A."""
        self.assertTrue(is_palindrome("Anna"))

    def test_empty_string(self) -> None:
        """Edge case: the empty string reads the same both ways."""
        self.assertTrue(is_palindrome(""))

    def test_number_raises_type_error(self) -> None:
        """Invalid input: the function promises a TypeError."""
        with self.assertRaises(TypeError):
            is_palindrome(121)


if __name__ == "__main__":
    unittest.main()
