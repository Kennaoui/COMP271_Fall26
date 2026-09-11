# Named constants replace "magic" index numbers
FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1
ROLE_INDEX = 2


def contains_prefix(records, prefix):
    """
    Return True if at least one record has a first name
    that starts with the given prefix. Otherwise, return False.
    """
    found = False

    for rec in records:
        first = rec[FIRST_NAME_INDEX]      # look up the first name by position
        if first.startswith(prefix):
            found = True

    return found


def indices_prefix(records, prefix):
    """
    Return a list of indices for all records whose first name
    starts with the given prefix.
    """
    matches = []

    for i in range(len(records)):
        first = records[i][FIRST_NAME_INDEX]
        if first.startswith(prefix):
            matches.append(i)              # remember the position, not the record

    return matches

print("Any first name starts with 'L'? ->", contains_prefix(st_characters, "L"))
print("Indices where first name starts with 'L' ->", indices_prefix(st_characters, "L"))
