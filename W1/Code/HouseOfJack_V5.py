PREFIX = "This is the"
SUFFIX = "house that Jack built."

ITEMS = ["", "malt", "rat", "cat", "dog"]
ACTIONS = ["", "lay", "ate", "killed", "worried"]


def first_stanza():
    # The very first stanza is special: it uses SUFFIX directly.
    print(f"{PREFIX} {SUFFIX}\n")


def other_stanzas():
    # Build each “item that action ...” string from the inside out.
    # Example:
    #   malt -> "malt that lay in the house that Jack built."
    #   rat  -> "rat that ate the malt that lay in the house that Jack built."
    prev = f"{SUFFIX}"  # what comes after "in the" for malt, and gets nested thereafter

    for i in range(1, len(ITEMS)):
        if i == 1:
            # malt is the only one that says "lay in the ..."
            current = f"{ITEMS[i]} that {ACTIONS[i]} in the {prev}"
        else:
            # everything else says "... the <previous phrase>"
            current = f"{ITEMS[i]} that {ACTIONS[i]} the {prev}"

        print(f"{PREFIX} {current}\n")
        prev = current


first_stanza()
other_stanzas()
