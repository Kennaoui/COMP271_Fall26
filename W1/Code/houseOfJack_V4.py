PREFIX = "This is the"
SUFFIX = "house that Jack built."
 
ITEMS = ["", "malt", "rat", "cat", "dog"]
ACTIONS = ["", "lay", "ate", "killed", "worried"]

malt_string = f"{ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}"
rat_string = f"{ITEMS[2]} that {ACTIONS[2]} the {malt_string}"
cat_string = f"{ITEMS[3]} that {ACTIONS[3]} the {rat_string}"
dog_string = f"{ITEMS[4]} that {ACTIONS[4]} the {cat_string}"


def house():
    print(f"{PREFIX} {SUFFIX}")


def malt():
    print(f"{PREFIX} {malt_string}")


def rat():
    print(f"{PREFIX} {rat_string}")


def cat():
    print(f"{PREFIX} {cat_string}")


def dog():
    print(f"{PREFIX} {dog_string}")


house()
print()
malt()
print()
rat()
print()
cat()
print()
dog()
