"""Five suspects and one good queue. Treat them as black boxes!

Every class here claims to keep the Queue contract:
    enqueue(item)  add item at the rear
    dequeue()      remove and return the front item (IndexError if empty)
    peek()         return the front item, keep it (IndexError if empty)
    is_empty()     True if the queue has no items
    size()         number of items in the queue

GoodQueue keeps every promise. Each suspect breaks exactly one.
Do not read the code below: find the bugs with your tests.
"""

EMPTY_MESSAGE = "queue is empty"
FRONT = 0
START = 0
STEP = 1


class GoodQueue:
    """A queue that keeps every promise of the contract."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []  # front is index 0, rear is the end

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop(FRONT)

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data[FRONT]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Return the number of items."""
        return len(self.__data)


class SuspectA:
    """A queue suspect."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop()

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data[FRONT]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Return the number of items."""
        return len(self.__data)


class SuspectB:
    """A queue suspect."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop(FRONT)

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop(FRONT)

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Return the number of items."""
        return len(self.__data)


class SuspectC:
    """A queue suspect."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []
        self.__count = START

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)
        self.__count += STEP

    def dequeue(self):
        """Remove and return the front item."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop(FRONT)

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data[FRONT]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Return the number of items."""
        return self.__count


class SuspectD:
    """A queue suspect."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        result = None
        if len(self.__data) > 0:
            result = self.__data.pop(FRONT)
        return result

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data[FRONT]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Return the number of items."""
        return len(self.__data)


class SuspectE:
    """A queue suspect."""

    def __init__(self) -> None:
        """Create an empty queue."""
        self.__data = []
        self.__used = False

    def enqueue(self, item) -> None:
        """Add item at the rear."""
        self.__data.append(item)
        self.__used = True

    def dequeue(self):
        """Remove and return the front item."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data.pop(FRONT)

    def peek(self):
        """Return the front item without removing it."""
        if len(self.__data) == 0:
            raise IndexError(EMPTY_MESSAGE)
        return self.__data[FRONT]

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return not self.__used

    def size(self) -> int:
        """Return the number of items."""
        return len(self.__data)
