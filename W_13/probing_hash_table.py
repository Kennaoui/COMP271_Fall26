"""COMP 271 - Assignment 11: Open Addressing and Probing."""

from __future__ import annotations

import random
import string


class ProbingHashTable:
    """Store strings using linear or quadratic probing."""

    _DEFAULT_CAPACITY: int = 11
    _PROBE_MODES: tuple[str, str] = ("linear", "quadratic")
    _DEFAULT_PROBING_MODE: str = _PROBE_MODES[0]

    def __init__(
        self, capacity: int = _DEFAULT_CAPACITY,
        mode: str = _DEFAULT_PROBING_MODE,
    ) -> None:
        """Create an empty table with the given capacity and probing mode."""
        if mode not in self._PROBE_MODES:
            mode = self._DEFAULT_PROBING_MODE
        self._capacity = capacity
        self._mode = mode
        self._table: list[str | None] = [None] * capacity
        self._size = 0
        # TODO (Part 1): Choose a tombstone marker and update the slot type.

    def _hash(self, key: int) -> int:
        """Convert an integer key to a table index."""
        return key % self._capacity

    def _probe(self, position: int, attempt: int) -> int:
        """Return the index for the given probing attempt."""
        if self._mode == "linear":
            prob = (position + attempt) % self._capacity
        else:
            prob = (position + attempt * attempt) % self._capacity
        return prob

    def load_factor(self) -> float:
        """Return the proportion of active entries in the table."""
        return self._size / self._capacity

    def size(self) -> int:
        """Return the number of active entries."""
        return self._size

    def insert(self, value: str) -> tuple[bool, list[int]]:
        """Insert a new value; return (inserted, indices probed).

        inserted is True only when a new entry was added.
        """
        probes: list[int] = []
        inserted = False

        if self._size < self._capacity:
            index = self._hash(abs(hash(value)))
            attempt = 0
            finished = False

            while attempt < self._capacity and not finished:
                probe_index = self._probe(index, attempt)
                probes.append(probe_index)
                slot = self._table[probe_index]

                if slot is None:
                    self._table[probe_index] = value
                    self._size += 1
                    inserted = True
                    finished = True
                elif slot == value:
                    finished = True

                attempt += 1

        # TODO (Part 1): Reuse tombstones when inserting new values
        # Make sure a value already in the table is not inserted twice
        return inserted, probes

    def contains(self, value: str) -> bool:
        """Return True if value is present, otherwise False."""
        found = False
        index = self._hash(abs(hash(value)))
        attempt = 0
        finished = False

        while attempt < self._capacity and not finished:
            probe_index = self._probe(index, attempt)
            slot = self._table[probe_index]

            if slot is None:
                finished = True
            elif slot == value:
                found = True
                finished = True

            attempt += 1

        # TODO (Part 1): Update the search to handle tombstones.
        return found

    def remove(self, value: str) -> bool:
        """Remove value if found; return whether removal succeeded."""
        # TODO (Part 1): Mark the slot as deleted and update _size.
        raise NotImplementedError


def random_string(length: int) -> str:
    """Return a random string of letters of the requested length."""
    letters = string.ascii_letters
    result = ""
    for _ in range(length):
        result += random.choice(letters)
    return result


def run_experiment() -> None:
    """Compare insertion probes for linear and quadratic probing."""
    # TODO (Part 2): Use fresh tables for repeated trials.
    # Record probes for successful insertions at each load factor.
    # Track failed insertions separately; limit consecutive failures.
    # Average the results without using dictionaries or sets.
    pass


def main() -> None:
    """Run basic checks and the probing experiment."""
    table = ProbingHashTable(11, "linear")
    inserted, probes = table.insert("apple")
    print("Inserted:", inserted)
    print("Probes:", probes)
    print("Load factor:", table.load_factor())
    # TODO: Test collisions, contains(), remove(), and tombstone reuse.
    # TODO: Call run_experiment() and generate/export the graph.


if __name__ == "__main__":
    main()
