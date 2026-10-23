"""Activity: Catch the Buggy Queue.

Write tests from the Queue contract, then run them against each suspect.
Change ONE line (the import below) to switch which queue is tested.
"""

import unittest

# Change this ONE line: GoodQueue, SuspectA, SuspectB, ... SuspectE
from queue_suspects import GoodQueue as QueueUnderTest


class TestQueueContract(unittest.TestCase):
    """Small, focused tests written from the Queue contract."""

    def setUp(self) -> None:
        """A fresh, empty queue before every test."""
        self.q = QueueUnderTest()

    def test_new_queue_is_empty(self) -> None:
        """Example test: a new queue has no items."""
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)
    def test_queue_after_one_enqueue(self) -> None:
        """After one enqueue, the queue is not empty and its size is 1."""
        self.q.enqueue("Test")
        self.assertFalse(self.q.is_empty())
        self.assertEqual(self.q.size(), 1)

    # TODO: write one small test method for each promise below.
    # 1. After one enqueue, the queue is not empty and its size is 1.
    # 2. Items come out in the order they went in (first in, first out).
    # 3. peek returns the front item and does NOT remove it.
    # 4. size goes down by one after a dequeue.
    # 5. After removing every item, the queue is empty again.
    # 6. dequeue on an empty queue raises IndexError.
    # 7. peek on an empty queue raises IndexError.


if __name__ == "__main__":
    unittest.main(verbosity=2)
