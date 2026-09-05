def indices_of(list_to_search: list, item_to_find: str, find_all: bool) -> int | list[int]:
    """
    Return all matching indices when all is True.
    Otherwise, return the first matching index or -1 if not found.
    """
    # Results will be stored in indices. The function will decide
    # what to return at the end based on the value of all.
    indices: list[int] = []

    # Iterate through the list.
    i: int = 0
    while i < len(list_to_search):
        if list_to_search[i] == item_to_find:
            # A match was found; store its index.
            indices.append(i)

            # Exit early if we are interested only in the first occurrence.
            if not all:
                i = len(list_to_search)

        i += 1

    # Decide what to return.
    result: int | list[int] = indices

    if not all:
        # We are interested only in the first occurrence.
        if len(indices) == 0:
            # No occurrence found.
            result = -1
        else:
            result = indices[0]

    return result
