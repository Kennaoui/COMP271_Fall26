class Friend:
    """Represents one contact in an address book."""

    def __init__(self, first_name: str, last_name: str, phone: str, dob: str) -> None:
        # Each parameter becomes an attribute: this is the object's state
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.dob = dob

    def introduce(self) -> str:
        """Return a one-line self-introduction: this is the object's behavior."""
        return f"Hi, I'm {self.first_name} {self.last_name}. You can reach me at {self.phone}."

  def main():
    # Creating an instance/object
    myfriend = Friend("Joy", "Doe", "0000", "01/01/2000")
      
    # Accessing a field/attribute of the object
    print(f"{myfriend.fir}'s phone number. We will update in the next.")
      
    # Updating a field/attribute of the object
    myfriend.phone = "765 492 534"

    # Call an instance method
    prin(myfriend.introduce)
      
main()
