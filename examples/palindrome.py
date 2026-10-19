"""A small function to test: is a word a palindrome?"""


def is_palindrome(word: str) -> bool:
    """Return True if word reads the same forwards and backwards.

    Uppercase and lowercase letters count as the same letter.
    Raise TypeError if word is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    cleaned = word.lower()  # so "Anna" counts as a palindrome
    return cleaned == cleaned[::-1]
