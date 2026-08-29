"""Block-letter data used by the horizontal river activity."""

M = [
    " M       M",
    " M M   M M",
    " M  M M  M",
    " M   M   M",
    " M       M",
    " M       M",
    " M       M",
]

I = [
    "  I ",
    "  I ",
    "  I ",
    "  I ",
    "  I ",
    "  I ",
    "  I ",
]

S = [
    "   SSSSSSS",
    " SS       ",
    " SS       ",
    "  SSSSSS  ",
    "        SS",
    "        SS",
    " SSSSSSS  ",
]

P = [
    " PPPPPPPP ",
    " P      PP",
    " P     PP ",
    " PPPPPP   ",
    " P        ",
    " P        ",
    " P        ",
]


def sanity_check(letters):
    """Return True when all letters are nonempty and have the same height."""
    if len(letters) == 0 or len(letters[0]) == 0:
        return False

    expected_height = len(letters[0])

    for letter in letters:
        if len(letter) != expected_height:
            return False

    return True


# Catch malformed letter data before the activity begins.
assert sanity_check([M, I, S, P])
