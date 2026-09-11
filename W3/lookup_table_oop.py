class Character:
    """A character with a unique (first_name, last_name) identity.

    Roles are stored as a list so one character can have multiple roles.
    """

    def __init__(self, first_name: str, last_name: str, role: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.roles = [role]

    def add_role(self, role: str) -> None:
        """Add a new role if it is not already present."""
        if role not in self.roles:
            self.roles.append(role)

    def key(self) -> tuple:
        """Return a tuple that uniquely identifies this character."""
        return (self.first_name, self.last_name)



class Cast:
    """A collection of unique Character records.

    Uniqueness rule: (first_name, last_name) must be unique.
    If the character already exists, the new role is attached to it.
    """

    def __init__(self) -> None:
        self.underlying = []  # list[Character]

    def find_index(self, first_name: str, last_name: str) -> int:
        """Return the index of the matching character, or -1 if not found."""
        target_key = (first_name, last_name)
        for i in range(len(self.underlying)):
            if self.underlying[i].key() == target_key:
                return i
        return -1

    def add_character(self, first_name: str, last_name: str, role: str) -> None:
        """Add a character if new; otherwise attach the role to the existing character."""
        idx = self.find_index(first_name, last_name)
        if idx == -1:
            self.underlying.append(Character(first_name, last_name, role))
        else:
            self.underlying[idx].add_role(role)

    def describe(self) -> str:
        """Return a multi-line string describing the cast."""
        lines = [str(char) for char in self.underlying]
        return "\n".join(lines)
