"""One test suite for the Stack contract (push, pop, peek, is_empty, size).

The tests only use the promises on the Stack menu, so they work for
ListStack, ArrayStack and LinkedStack. Change ONE line to switch.
"""

import unittest

from stacks import ListStack as StackUnderTest  # change this line only


class TestStackContract(unittest.TestCase):
    """Small, focused tests written from the Stack contract."""

    def setUp(self) -> None:
        """A fresh, empty stack before every test."""
        self.s = StackUnderTest()

    def test_new_stack_is_empty(self) -> None:
        """A new stack has no items."""
        self.assertTrue(self.s.is_empty())
        self.assertEqual(self.s.size(), 0)

    def test_push_changes_state(self) -> None:
        """Check the state BEFORE and AFTER a push."""
        # BEFORE (arrange)
        self.assertTrue(self.s.is_empty())
        # ACT
        self.s.push("plate")
        # AFTER (assert)
        self.assertFalse(self.s.is_empty())
        self.assertEqual(self.s.size(), 1)
        self.assertEqual(self.s.peek(), "plate")

    def test_pop_returns_last_pushed(self) -> None:
        """Last in, first out."""
        self.s.push("red")
        self.s.push("green")
        self.s.push("blue")
        self.assertEqual(self.s.pop(), "blue")
        self.assertEqual(self.s.pop(), "green")
        self.assertEqual(self.s.pop(), "red")

    def test_peek_does_not_remove(self) -> None:
        """peek looks at the top; the size must not change."""
        self.s.push("cup")
        size_before = self.s.size()  # snapshot
        self.assertEqual(self.s.peek(), "cup")
        self.assertEqual(self.s.size(), size_before)

    def test_pop_empty_raises(self) -> None:
        """Popping an empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.s.pop()

    def test_failed_pop_leaves_stack_unchanged(self) -> None:
        """After a rejected pop, the stack is still empty."""
        with self.assertRaises(IndexError):
            self.s.pop()
        self.assertTrue(self.s.is_empty())


if __name__ == "__main__":
    unittest.main()
