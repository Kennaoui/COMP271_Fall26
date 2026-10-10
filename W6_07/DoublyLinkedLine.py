from __future__ import annotations


class DoublyStation:
    """One station with links to the next and previous stations."""

    def __init__(self, data: str) -> None:
        self._data: str = data
        self._next: DoublyStation | None = None
        self._previous: DoublyStation | None = None

    @property
    def data(self) -> str:
        """Return the station name."""
        return self._data

    @property
    def next(self) -> DoublyStation | None:
        """Return the next station."""
        return self._next

    @next.setter
    def next(self, station: DoublyStation | None) -> None:
        """Set the next station."""
        self._next = station

    @property
    def previous(self) -> DoublyStation | None:
        """Return the previous station."""
        return self._previous

    @previous.setter
    def previous(self, station: DoublyStation | None) -> None:
        """Set the previous station."""
        self._previous = station


class DoublyLinkedLine(TrainLine):
    """A train line with links in both directions."""

    def __init__(self) -> None:
        self._head: DoublyStation | None = None
        self._size: int = 0

    def is_empty(self) -> bool:
        """Return True when the line has no stations."""
        return self._head is None

    def __len__(self) -> int:
        """Return the number of stations."""
        return self._size

    def __str__(self) -> str:
        """Return the stations in order, arrow-joined."""
        names: list[str] = []
        current = self._head

        while current is not None:
            names.append(current.data)
            current = current.next

        return ' <-> '.join(names)

    def add_first(self, data: str) -> None:
        """Insert data as the new first station."""
        new_node = DoublyStation(data)
        new_node.next = self._head

        if not self.is_empty():
            self._head.previous = new_node

        self._head = new_node
        self._size += 1

    def add_last(self, data: str) -> None:
        """Append data as the new last station."""
        new_node = DoublyStation(data)

        if self.is_empty():
            self._head = new_node
        else:
            current = self._head

            while current.next is not None:
                current = current.next

            current.next = new_node
            new_node.previous = current

        self._size += 1

    def insert_after(self, new_val: str, after_val: str) -> None:
        """Insert new_val after the first station named after_val."""
        current = self._head

        while current is not None and current.data != after_val:
            current = current.next

        if current is not None:
            new_node = DoublyStation(new_val)
            new_node.previous = current
            new_node.next = current.next

            if current.next is not None:
                current.next.previous = new_node

            current.next = new_node
            self._size += 1

    def search(self, value:str) -> DoublyStation | None: 
        """search for a station named value. If found return it, otherwise return None """
        pass

    

    def remove(self, value: str) -> bool:
        """Remove the first matching station; return True if removed."""
        pass
