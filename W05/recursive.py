def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forward and backward.

    Assume text contains only lowercase letters.
    """
    # Base case: What should happen when text has 0 or 1 characters?
    

    # If the first and last characters differ, what can you conclude?
    

    # Recursive case: Check the part between the first and last characters.
    


def main() -> None:
    """Test the is_palindrome function."""
    test_cases = [
        ("racecar", True),
        ("abba", True),
        ("python", False),
        ("a", True),
        ("", True),
    ]

    for text, expected in test_cases:
        result = is_palindrome(text)
        print(f"{text!r}: expected {expected}, got {result}")


if __name__ == "__main__":
    main()
