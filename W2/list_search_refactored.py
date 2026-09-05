def indices_of(list_to_search: list, item_to_find: str, find_all: bool) -> int | list[int]:
    """
    Return all matching indices when find_all is True. Else, return the first matching index or -1 if not found.
    """
    # Results will be stored in indices. The function will decide
    # what to return at the end based on the value of find_all.
    indices: list[int] = []

    # Iterate through the list.
    i: int = 0
    while i < len(list_to_search):
        if list_to_search[i] == item_to_find:
            # A match was found; store its index.
            indices.append(i)

            # Exit early if we are interested only in the first occurrence.
            if not find_all:
                i = len(list_to_search)

        i += 1

    # Decide what to return.
    result: int | list[int] = indices

    if not find_all:
        # We are interested only in the first occurrence.
        if len(indices) == 0:
            # No occurrence found.
            result = -1
        else:
            result = indices[0]

    return result
    
def index_of_all(list_to_search: list[str], item_to_find: str) -> list[int]:
    """Returns list of indices where item_to_find is found in list_to_search, or empty list if not found."""
    return indices_of(list_to_search, item_to_find, True)

def index_of(list_to_search: list[str], item_to_find: str) -> int:
    """Returns the index of item_to_find in list_to_search, or -1 if not found.""" 
    return indices_of(list_to_search, item_to_find, False)

def contains(list_to_search: list[str], item_to_find: str) -> bool:
    """Returns True if item_to_find is in list_to_search, False otherwise."""
    return index_of(list_to_search, item_to_find) != -1
