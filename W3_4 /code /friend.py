from datetime import date

class Friend:
    """Represents one contact in an address book."""

    friends_number = 0

    def __init__(self, first_name: str, last_name: str, phone: str, dob: date) -> None:
        # Each parameter becomes an attribute: this is the object's state
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__phone : str = phone
        self.__dob : date = dob
        friends_number += 1

    @property
    def fname(self):
        """Returns first name """
        return self.__first_name.upper()
    
    @fname.setter
    def fname(self, name: str):
        if name == '':
            print("Invalid Name")
        else:
            self.__first_name = name

    @property
    def lname(self):
        """Returns last name """
        return self.__last_name.upper()
    
    @lname.setter
    def first_name(self, name: str):
        if name == '':
            print("Invalid Name")
        else:
            self.__last_name = name
    
    def __str__(self) -> str:
        """String representation of a friend object""""
        return self.__first_name + ', '+ self.__last_name
    def __repr__(self) -> str:
        """ Delegated to __str__"""
        return self.__str__()
    
    def __eq__(self, other) -> bool: 
         """Two friends are equal if they share the same name and dob."""
        result = False
        if self.__first_name == other.__first_name and self.__last_name == other.__last_name and self.__dob == other.__dob:
            result = True
        return result
    
    def __lt__(self, other: "Friend") -> bool:
        """Compare friends by last name, then by first name."""
        if self.last_name < other.last_name:
            return True
        elif self.last_name == other.last_name:
            return self.first_name < other.first_name
        else:
            return False
        # More Pythonic version:
        # return (self.last_name, self.first_name) < (other.last_name, other.first_name)
        #
        # This works because the tuple class defines __lt__ to compare its
        # elements in order: first the last names, then the first names
        # if the last names are equal.


    def __len__(self) -> int:
        """Return the friend's age in complete years."""
        today = date.today()
        age = today.year - self.dob.year

        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age = age - 1

        return age


    def introduce(self) -> str:
        """Return a one-line self-introduction: this is the object's behavior."""
        return f"Hi, I'm {self.__first_name} {self.__last_name}. You can reach me at {self.__phone}."
    
    def describe_relationship(self) -> str:
        """Return a general description of the relationship."""
        return "This person is my friend."

    def __secret(self) -> str:
        return "My friend's secret is ..."
    
    @classmethod
    def increment_friends_number(i : int):
        friends_number += i
    
    @classmethod
    def create_friend_by_email(email : str): 
        lname = email.split('@')[0]
        return Friend(lname, '', '', '')
        






def main():

    print("number of friends I have:", Friend.friends_number)
    Friend.increment_friends_number(3)
    # Creating an instance/object
    mySchoolFriend = Friend("Joy", "Doe", "123 475 698",  date(2000, 1, 31))
    myWorkFriend = Friend("Joy", "Doe", " ",  date(2009, 4, 1))
    myBFF = Friend.create_friend_by_email("ennaoui@...")
    print("number of friends I have:", Friend.friends_number)

    #Call and modify a property
    print(mySchoolFriend.fname)
    mySchoolFriend = "Joel"

    #Calling INSTANCE methods
    print(mySchoolFriend.introduce())
    print(mySchoolFriend.describe_relationship())
    print(myWorkFriend.introduce())
    print(myWorkFriend.describe_relationship())

    #Uncomment this if you want to try accessing a private method
    #print(mySchoolFriend.__secret())

    #Using ternary expression, we compare both friends. 
    #mySchoolFriend == myWorkFriend calls __eq__
    print("My school friend is " + ("" if mySchoolFriend == myWorkFriend else "not ") + "the same as my work friend.")

    #Next mySchoolFriend < myWorkFriend calls __lt__
    # Try to write this using ternary expressions, it's fun!
    if mySchoolFriend < myWorkFriend:
        print(mySchoolFriend, "appears in my contacts book before", myWorkFriend)
    else: 
        print(myWorkFriend, "appears in my contacts book before", mySchoolFriend)
    
    #This one calls __len__ to calculate the age of mySchoolFriend
    print(mySchoolFriend, "is", len(mySchoolFriend) years old)

    
      
main()
