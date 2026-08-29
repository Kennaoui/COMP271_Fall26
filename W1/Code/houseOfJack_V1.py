PREFIX = "This is"

HOUSE_TAIL = "the house that Jack built."
MALT_TAIL = "the malt that lay in " + HOUSE_TAIL
RAT_TAIL = "the rat that ate\n" + MALT_TAIL
CAT_TAIL = "the cat \nThat killed " + RAT_TAIL
DOG_TAIL = "the dog that worried " + CAT_TAIL
COW_TAIL = "the cow with the crumpled horn \nThat tossed " + DOG_TAIL

def house_verse():
    print("This is", HOUSE_TAIL)

def malt_verse():
    print("This is", MALT_TAIL)

def rat_verse():
    print("This is", RAT_TAIL)

def cat_verse():
    print("This is", CAT_TAIL)

def dog_verse():
    print("This is", DOG_TAIL)

def cow_verse():
    print("This is", COW_TAIL)

def main():
    house_verse()
    print()
    malt_verse()
    print()
    rat_verse()
    print()
    cat_verse()
    print()
    dog_verse()
    print()
    cow_verse()


main()
