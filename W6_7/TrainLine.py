from abc import ABC, abstractmethod


class TrainLine(ABC):
    """An ordered sequence of station names. Duplicate names are allowed."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the line has no stations, False otherwise."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of stations as a nonnegative integer."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return station names in order; return '' for an empty line."""
        pass

    @abstractmethod
    def add_first(self, data: str) -> None:
        """Insert data at the beginning, increasing the size by one."""
        pass

    @abstractmethod
    def add_last(self, data: str) -> None:
        """Insert data at the end, increasing the size by one."""
        pass

    @abstractmethod
    def insert_after(self, new_val: str, after_val: str) -> None:
        """Insert new_val after the first occurrence of after_val.

        Increase the size by one if inserted.
        Leave the line unchanged if after_val is not found.
        """
        pass

    @abstractmethod
    def remove(self, value: str) -> bool:
        """Remove the first occurrence of value.

        Return True and decrease the size by one if removed.
        Return False and leave the line unchanged if value is not found.
        """
        pass

    @abstractmethod
    def search(self, value: str) -> bool:
        """Return True if a station named value exists in the line, False otherwise.

        Leave the line unchanged.
        """
        pass
