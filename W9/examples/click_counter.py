"""A tally counter, like the clicker a doorman uses."""


class ClickCounter:
    """Count clicks, starting from zero."""

    START = 0
    STEP = 1

    def __init__(self) -> None:
        """Create a counter that starts at zero."""
        self.__clicks = ClickCounter.START  # private: only methods change it

    def click(self) -> None:
        """Add one click."""
        self.__clicks += ClickCounter.STEP

    def value(self) -> int:
        """Return the number of clicks so far."""
        return self.__clicks

    def reset(self) -> None:
        """Set the counter back to zero."""
        self.__clicks = ClickCounter.START
