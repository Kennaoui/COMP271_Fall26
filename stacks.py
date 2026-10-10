"""Week 9: the Stack ADT and three implementations (matches the slides)."""
from abc import ABC, abstractmethod

EMPTY_STACK = "pop or peek on an empty stack"
FULL_STACK = "push on a full stack"
DEFAULT_CAPACITY = 10
EMPTY_TOP = -1        # __top when nothing is stored


class StackADT(ABC):
    """A collection where the last item in
    is the first item out (LIFO)."""

    @abstractmethod
    def push(self, item: object) -> None:
        """Put item on the top."""

    @abstractmethod
    def pop(self) -> object:
        """Remove and return the top item."""

    @abstractmethod
    def peek(self) -> object:
        """Return the top item, keep it."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Tell whether there are no items."""

    @abstractmethod
    def size(self) -> int:
        """Tell how many items there are."""


class ListStack(StackADT):
    """A stack stored in a Python list.
    The right end of the list is the top."""

    def __init__(self) -> None:
        # the items: bottom at index 0, top at -1
        self.__data: list[object] = []

    def push(self, item: object) -> None:
        """Put item on the top of the stack."""
        self.__data.append(item)    # right end = top

    def pop(self) -> object:
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        return self.__data.pop()    # removes the last item

    def peek(self) -> object:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        return self.__data[-1]      # look, don't touch

    def is_empty(self) -> bool:
        """Tell whether there are no items."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Tell how many items there are."""
        return len(self.__data)


class ArrayStack(StackADT):
    """A fixed-capacity stack stored in an array.
    The top is the highest filled index."""

    def __init__(self,
                 capacity: int = DEFAULT_CAPACITY) -> None:
        # the slots, all created up front
        self.__data: list[object | None] = [None] * capacity
        # maximum number of items, fixed forever
        self.__capacity: int = capacity
        # index of the top item; EMPTY_TOP if empty
        self.__top: int = EMPTY_TOP

    def push(self, item: object) -> None:
        """Put item on top. Refuses if the stack is full."""
        if self.__top == self.__capacity - 1:
            raise OverflowError(FULL_STACK)
        self.__top += 1                  # move the top up
        self.__data[self.__top] = item   # fill that slot

    def pop(self) -> object:
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        item = self.__data[self.__top]   # remember it
        self.__data[self.__top] = None   # release the slot
        self.__top -= 1                  # move the top down
        return item

    def peek(self) -> object:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        return self.__data[self.__top]

    def is_empty(self) -> bool:
        """Tell whether there are no items."""
        return self.__top == EMPTY_TOP

    def size(self) -> int:
        """Tell how many items there are."""
        return self.__top + 1


class _Node:
    """One link: an item and the node below."""

    def __init__(self, data: object,
                 below: "_Node | None") -> None:
        self.data = data     # the item
        self.next = below    # node underneath


class LinkedStack(StackADT):
    """A stack stored as a chain of nodes.
    The head of the chain is the top."""

    def __init__(self) -> None:
        # node holding the top item (None if empty)
        self.__top: _Node | None = None
        # number of items in the stack
        self.__size: int = 0

    def push(self, item: object) -> None:
        """Put item on the top of the stack."""
        # new node sits above the old top
        self.__top = _Node(item, self.__top)
        self.__size += 1

    def pop(self) -> object:
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        item = self.__top.data           # remember it
        self.__top = self.__top.next     # top moves down
        self.__size -= 1
        return item

    def peek(self) -> object:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError(EMPTY_STACK)
        return self.__top.data

    def is_empty(self) -> bool:
        """Tell whether there are no items."""
        return self.__top is None

    def size(self) -> int:
        """Tell how many items there are."""
        return self.__size


if __name__ == "__main__":
    for stack in [ListStack(), ArrayStack(), LinkedStack()]:
        for value in [99, 5, 17, 42]:
            stack.push(value)
        print(type(stack).__name__, stack.peek(), stack.pop(),
              stack.pop(), stack.size())
