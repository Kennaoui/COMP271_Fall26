# COMP 271: Assignment 6, Testing a Lookup Table

## Context

A lookup table stores entries made of a **key** and a **value**. You have built one before in earlier weeks: `Cast` kept one record per character, found by its key `(first_name, last_name)` with a `_find_index` helper that returned `-1` when the key was missing. This time the table is a course catalog: key `"COMP 271"`, value `"Data Structures I"`.

You will build the table twice (on a Python list, then on a linked list) and write **one** `unittest` suite that checks both.

Follow the Programmer's Pact. You may use more than one return statement when necessary.

## Rules

- No sets or dictionaries.
- No imports except those in the starter code.
- `ArrayLookupTable`: no `in` on lists (`for x in ...` is fine), no `index()`, `count()`, or `remove()`.
- `LinkedLookupTable`: no Python lists, except to build the list `keys()` returns.
- Tests call **only** the ADT methods: no private attributes, no `print`.

## The contract

The ADT is at the end of this assignment. Do not change it.

| Method | Promise |
|---|---|
| `put(key, value)` | New key: add it **last**. Existing key: replace its value only (same size, same position). |
| `get(key)` | Return the value. `KeyError` if absent. |
| `contains(key)` | `True` if the key is in the table. |
| `remove(key)` | Remove the entry and return its value. `KeyError` if absent. |
| `size()` / `is_empty()` | Number of entries / no entries. |
| `keys()` | A **new** list of the keys, oldest first. |

- `put` raises `TypeError` if the key or value is not a string, and `ValueError` if the key is `""`.
- A rejected request leaves the table unchanged.
- Keys are case-sensitive. A removed key that is added again goes last.

## Part 1: Two implementations

Write both classes in `lookup_table.py`, below the ADT.

**`ArrayLookupTable`** keeps a list of `_Entry` objects, oldest first. Write a private helper `__find(key)` that returns the key's index, or `NOT_FOUND` (`-1`), and build the other methods on it.

**`LinkedLookupTable`** keeps a chain of `_Node` objects: `__head` is the oldest entry, `__tail` the newest, and `__size` the count.

```python
class _Entry:
    """One key-value pair stored in an ArrayLookupTable."""

    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value


class ArrayLookupTable(LookupTableADT):
    """A lookup table stored in a Python list of _Entry objects."""

    NOT_FOUND = -1

    def __init__(self) -> None:
        self.__entries = []  # _Entry objects, oldest first

    def __find(self, key: str) -> int:
        """Return the index of key's entry, or NOT_FOUND."""
        pass

    # TODO: implement every method of LookupTableADT.
```

```python
class _Node:
    """One key-value pair in a LinkedLookupTable, plus a link to the next."""

    def __init__(self, key: str, value: str,
                 next_node: _Node | None = None) -> None:
        self.key = key
        self.value = value
        self.next = next_node


class LinkedLookupTable(LookupTableADT):
    """A lookup table stored in a singly linked chain of _Node objects."""

    def __init__(self) -> None:
        self.__head = None  # oldest entry
        self.__tail = None  # newest entry
        self.__size = 0

    # TODO: implement every method of LookupTableADT.
```

Watch out for `remove` in the linked version: removing the head, the tail, or the only node.

## Part 2: The test suite

Every test you write comes straight from **one sentence** of a docstring in the ADT. Copy this into `test_lookup_table.py`. It has one example.

```python
import unittest

from lookup_table import ArrayLookupTable as TableUnderTest  # change me

# Sample data used by several tests: (course code, course title).
COMP_163 = ("COMP 163", "Discrete Structures")
COMP_170 = ("COMP 170", "Introduction to Object-Oriented Programming")
COMP_271 = ("COMP 271", "Data Structures I")
MISSING_KEY = "COMP 999"


class TestLookupTableContract(unittest.TestCase):
    """Tests written from the LookupTableADT contract only."""

    def setUp(self) -> None:
        """Runs BEFORE each test method: a fresh, empty table."""
        self.table = TableUnderTest()

    def put_three_courses(self) -> None:
        """Helper (not a test): add COMP 163, COMP 170, COMP 271 in order."""
        for code, title in (COMP_163, COMP_170, COMP_271):
            self.table.put(code, title)

    def test_get_returns_stored_value(self) -> None:
        """get: 'Return the value stored under key'."""
        # ARRANGE
        self.put_three_courses()
        # ACT and ASSERT
        self.assertEqual(self.table.get("COMP 271"), "Data Structures I")

    # TODO (Part 2): add the five required tests.

    # TODO (Part 3): add five tests of your own.


if __name__ == "__main__":
    unittest.main()
```

Run it with `python -m unittest -v test_lookup_table`. Then change the import to `LinkedLookupTable` and run it again. Both runs must end with `OK`.

### Required tests

Add these five tests. Each one checks one promise from a docstring.

| Method | Docstring promise | Test name |
|---|---|---|
| `put` | Existing key: its value is replaced. | `test_put_existing_key_replaces_value` |
| `put` | `ValueError` if key is `""`. | `test_put_empty_key_raises_value_error` |
| `remove` | Returns the value. | `test_remove_returns_value` |
| `remove` | After a `KeyError`, the table is unchanged. | `test_failed_remove_leaves_table_unchanged` |
| `keys` | Oldest entry first. | `test_keys_oldest_first` |

## Part 3: Your own tests

Read the docstrings again and find **five more** promises that no test checks yet. Write one test for each, with a one-line docstring quoting the promise, like the example.

I will also run your suite against a few of my own implementations, some broken on purpose.

## Reflection

1. Give the Big-O of each operation in both implementations.
2. Add one bug to your code on purpose (for example, forget to update `__tail` in `remove`). Which tests fail? Undo it.
3. All tests pass. Does that mean there are no bugs? Explain briefly.

## Submission

Submit on Sakai:

- `lookup_table.py`
- `test_lookup_table.py`
- `reflection.pdf`, including the `-v` test output for both implementations

## Starter code: the ADT

Place this at the top of `lookup_table.py`.

```python
from __future__ import annotations

from abc import ABC, abstractmethod


class LookupTableADT(ABC):
    """A collection of entries, each made of a unique key and a value.

    Keys and values are strings. Keys are matched exactly (case matters).
    The table remembers the order in which keys were first added.
    """

    @abstractmethod
    def put(self, key: str, value: str) -> None:
        """Store value under key.

        If key is new, a new entry is added after all existing entries.
        If key is already present, only its value is replaced: the size
        and the position of the key do not change.
        Raise TypeError if key or value is not a string.
        Raise ValueError if key is the empty string.
        A rejected put leaves the table unchanged.
        """

    @abstractmethod
    def get(self, key: str) -> str:
        """Return the value stored under key; raise KeyError if absent."""

    @abstractmethod
    def contains(self, key: str) -> bool:
        """Return True if key is in the table, False otherwise."""

    @abstractmethod
    def remove(self, key: str) -> str:
        """Remove the entry for key and return its value.

        Raise KeyError if key is absent; the table is then unchanged.
        """

    @abstractmethod
    def size(self) -> int:
        """Return the number of entries in the table."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the table has no entries."""

    @abstractmethod
    def keys(self) -> list[str]:
        """Return a NEW list of the keys, oldest entry first.

        Changing the returned list must not change the table.
        """
```
