class ArrayTrainLine(TrainLine):
    """A train line stored in a dynamic array."""

    def __init__(self) -> None:
        self._stations: list[str] = []

    def is_empty(self) -> bool:
        """Return True if the line has no stations."""
        return len(self._stations) == 0

    def __len__(self) -> int:
        """Return the number of stations."""
        return len(self._stations)

    def __str__(self) -> str:
        """Return station names in order, arrow-joined."""
        return ' -> '.join(self._stations)

    def add_first(self, data: str) -> None:
        """Insert data at the beginning of the line."""
        self._stations.insert(0, data)

    def add_last(self, data: str) -> None:
        """Append data at the end of the line."""
        self._stations.append(data)

    def insert_after(self, new_val: str, after_val: str) -> None:
        """Insert new_val after the first occurrence of after_val."""
        index = 0

        while index < len(self._stations) and self._stations[index] != after_val:
            index += 1

        if index < len(self._stations):
            self._stations.insert(index + 1, new_val)

    def remove(self, value: str) -> bool:
        """Remove the first occurrence of value; return True if removed."""
        removed = False
        index = 0

        while index < len(self._stations) and self._stations[index] != value:
            index += 1

        if index < len(self._stations):
            self._stations.pop(index)
            removed = True

        return removed

    def search(self, value: str) -> bool:
        """Return True if value exists in the line."""
        index = 0

        while (
            index < len(self._stations)
            and self._stations[index] != value
        ):
            index += 1

        return index < len(self._stations)
