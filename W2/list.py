
CHICAGO_AREAS = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont"]

def contains(list_to_search: list[str], item_to_find: str) -> bool:
    """Returns True if item_to_find is in list_to_search, False otherwise."""
    found = False
    i = 0
    while i < len(list_to_search) and not found:
        found = (list_to_search[i] == item_to_find)
        i += 1
    return found 

def index_of(list_to_search: list[str], item_to_find: str) -> int:
    """Returns the index of item_to_find in list_to_search, or -1 if not found.""" 
    pass 

