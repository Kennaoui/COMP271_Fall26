
CHICAGO_AREAS = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont"]

def contains(list_to_search: list[str], item_to_find: str) -> bool:
    """Returns True if item_to_find is in list_to_search, False otherwise."""
    return index_of(list_to_search, item_to_find) != -1

def index_of(list_to_search: list[str], item_to_find: str) -> int:
    """Returns the index of item_to_find in list_to_search, or -1 if not found.""" 
    index: int = -1
    i = 0
    while i < len(list_to_search) and index == -1:
        if list_to_search[i] == item_to_find:
            index = i
        i += 1
    return index 

def index_of_all(list_to_search: list[str], item_to_find: str) -> list[int]:
    """Returns list of indices where item_to_find is found in list_to_search, or empty list if not found.""" 
    indices: list[int] = []
    for i in range(len(list_to_search)):
        if list_to_search[i] == item_to_find:
            indices.append(i)
    return indices

