from abc import ABC, abstractmethod


class TrainLine(ABC):
    """An ordered sequence of station names."""

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def add_first(self, data: str) -> None:
        pass

    @abstractmethod
    def add_last(self, data: str) -> None:
        pass

    @abstractmethod
    def insert_after(self, new_val: str, after_val: str) -> None:
        pass

    @abstractmethod
    def remove(self, value: str) -> bool:
        pass
