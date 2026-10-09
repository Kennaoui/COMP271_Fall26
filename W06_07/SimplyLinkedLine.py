from __future__ import annotations


class Station:
    """One station on the line."""

    def __init__(self, data: str) -> None:
        # The station name this Station carries.
        self._data: str = data
        # The following station; None until it is linked.
        self._next: Station | None = None

    @property
    def data(self) -> str:
        """Return the station name."""
        return self._data

    @property
    def next(self) -> Station | None:
        """Return the following station."""
        return self._next

    @next.setter
    def next(self, next_station: Station | None) -> None:
        """Link this station to next_station."""
        self._next = next_station


class SimplyLinkedLine:
    """A train line: Stations chained from the head."""

    def __init__(self) -> None:
        # The first station; None means an empty line.
        self._head: Station | None = None
        # The number of stations in the line
        self._size: int = 0

    def is_empty(self) -> bool:
        """Return True when the line has no stations."""
        return self._head is None

    def __str__(self) -> str:
        """Return the stations in order, arrow-joined."""
        names: list[str] = []
        # Board at the head.
        current: Station | None = self._head
        # Ride until we fall off the end of the line.
        while current is not None:
            names.append(current.data)
            # Move one station along.
            current = current.next
        return ' -> '.join(names)
        
    def __len__(self) -> int:
        """Return the size of the line (number of stations)."""
        return self._size

    def add_first(self, data: str) -> None:
        """Insert data as the new first station."""
        new_node: Station = Station(data)
        # New station points at the old first station.
        new_node.next = self._head
        # The line now starts at the new station.
        self._head = new_node
        self._size += 1 

    def add_last(self, data: str) -> None:
        """Append data as the new last station."""
        new_node: Station = Station(data)
        if self.is_empty():
            # The new station is the whole line.
            self._head = new_node
        else:
            # Ride to the last station.
            current: Station | None = self._head
            while current.next is not None:
                current = current.next
            # Hook the new station on after it.
            current.next = new_node
        self._size += 1 

    def insert_after(self, new_val: str, after_val: str) -> None:
        """Insert new_val after the first station named after_val."""
        current = self._head
    
        while current is not None and current.data != after_val:
            current = current.next
    
        if current is not None:
            new_node = Station(new_val)
            new_node.next = current.next
            current.next = new_node
            self._size += 1


    def remove(self, value:str) -> bool: 
        """If found, remove the station named value. Return True if found and removed, False otherwise"""
        removed = False
        if not self.is_empty():
            if self._head.data == value:
                self._head = self._head.next
                self._size -= 1
                removed = True
                
            else: 
                previous = self._head
                current = previous.next
                while current is not None and not removed: 
                    if current.data == value:
                        previous.next = current.next
                        self._size -= 1
                        removed = True
                    else: 
                        previous = current
                        current = current.next
    
        return removed 

    def search(self, value:str) -> Station | None: 
        """search for a station named value. If found return it, otherwise return None """
        pass
                        
                
            
        
        


def main() -> None:
    """Demonstrate node properties, manual links, and list operations."""
    print('1. A single station')
    loyola: Station = Station('Loyola')
    print(loyola.data)  # Loyola
    print(loyola.next)  # None

    print('\n2. Linking nodes by hand')
    howard: Station = Station('Howard')
    jarvis: Station = Station('Jarvis')
    morse: Station = Station('Morse')
    howard.next = jarvis
    jarvis.next = morse
    morse.next = loyola
    print(howard.next.data)  # Jarvis
    print(howard.next.next.data)  # Morse

    print('\n3. Building a LinkedList')
    red_line: SimplyLinkedLine = SimplyLinkedLine()
    print(red_line.is_empty())  # True
    red_line.add_first('Loyola')
    red_line.add_first('Morse')
    red_line.add_first('Jarvis')
    print(red_line)  # Jarvis -> Morse -> Loyola
    red_line.add_first('Howard')
    print(red_line)  # Howard -> Jarvis -> Morse -> Loyola
    red_line.add_last('Granville')
    print(red_line)  # Howard -> Jarvis -> Morse -> Loyola -> Granville
    print(red_line.is_empty())  # False

    print('\n4. Adding at the end of an empty list')
    another_line: SimplyLinkedLine = SimplyLinkedLine()
    another_line.add_last('Loyola')
    print(another_line)  # Loyola


if __name__ == '__main__':
    main()
