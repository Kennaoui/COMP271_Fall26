
class Shape():
    """Represent the common characteristics of a geometric shape."""

    def __init__(self, color: str) -> None:
        self.color = color

    def describe(self) -> str:
        """Return a description of the shape."""
        return f"This is a {self.color} shape."

    
    def area(self) -> float:
        """Return the area of the shape."""
        pass


