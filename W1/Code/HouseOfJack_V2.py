PREFIX = "This is the"
SUFFIX = "house that Jack built."

ITEMS = ["", "malt", "rat", "cat", "dog"]
ACTIONS = ["", "lay", "ate", "killed", "worried"]


def house():
    print(f"{PREFIX} {SUFFIX}")


def malt():
    print(f"{PREFIX} {ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}")


def rat():
    print(
        f"{PREFIX} {ITEMS[2]} that {ACTIONS[2]} the {ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}"
    )


def cat():
    print(
        f"{PREFIX} {ITEMS[3]} that {ACTIONS[3]} the {ITEMS[2]} that {ACTIONS[2]} the {ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}"
    )
  
def dog():
    print(
        f"{PREFIX} {ITEMS[4]} that {ACTIONS[4]} the {ITEMS[3]} that {ACTIONS[3]} the {ITEMS[2]} that {ACTIONS[2]} the {ITEMS[1]} that {ACTIONS[1]} in the {SUFFIX}"
    )


house()
print()
malt()
print()
rat()
print()
cat()
print()
dog()
