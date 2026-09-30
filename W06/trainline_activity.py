​def insert_at(self, index: int, name: str) -> bool:
    """Insert a station at the given zero-based index.

    Args:
        index: Position at which to insert, from FRONT through the current size.
        name: Name of the station to insert.

    Returns:
        True if the station was inserted; False if the index is invalid.
    """
    inserted: bool = False

    if index == FRONT:
        self.add_first(name)
        inserted = True

    elif FRONT < index <= self.__size:
        # TODO 1: Move `previous` to the station immediately
        # before position `index`.

        # TODO 2: Make the new node point to the station after
        # `previous`, then make `previous` point to the new node.

        # TODO 3: Increment the size and set `inserted` to True.
        pass

    return inserted
