# COMP 271: Assignment 5, Stacks and Queues

## Context

So far we have built stacks and queues on top of Python lists and linked lists. The ADT only promises *what* the operations do, not *how* the data is stored, so any structure that can hold items in order could do the job. In Part 1 you will test that claim with an unusual choice: the underlying data structure will be **a file**. In Part 2 you will use a queue to simulate a real line of people, this time with Python's built-in queue tool.

Follow the Programmer's Pact. As an exception, you may use more than one return statement when necessary.

## Rules

These rules apply to **Part 1**:

- You may not use the `seek()` method in this assignment.
- You may not use lists for this assignment.
- If your work requires additional classes, you may write them.
- You may not import any modules except for those already included in the codebase of the assignment or listed below:
  - `from __future__ import annotations`
- No sets or dictionaries may be used.
- If your work requires additional methods to support the development of the methods the assignment asks for, you may write them.

These rules apply to **Part 2**:

- The only import allowed is `from collections import deque`.
- The starter code copies `tickets` with `list(tickets)`. That list is allowed in Part 2. Do not use any other lists, sets, or dictionaries.

## Learning goals

- Show that an ADT's contract does not depend on its underlying data structure.
- Implement stack and queue operations using only file reads and writes.
- Reason about the cost of each operation when the data lives in a file.
- Use a queue to simulate a first-in, first-out process.

## Part 1: A stack and a queue stored in a file

For this assignment, you'll implement a stack and a queue object whose underlying data structure is ... a file!

The stack and queue you'll implement store strings, **one string per line**. The Abstract Data Types for your stack and queue are in the starter code at the end of this assignment. The contracts are the same as the ones we discussed in class:

- Queue: `enqueue`, `dequeue`, `peek`, `is_empty`, `size`.
- Stack: `push`, `pop`, `peek`, `is_empty`, `size`.

### The two classes

Define two classes in `file_stack_queue.py`:

1. `FileStack`, which inherits from `StackADT`.
2. `FileQueue`, which inherits from `QueueADT`.

Each constructor takes one argument, `path: str`, the name of the file that will hold the items. The constructor **creates the file, or empties it if it already exists**, so every new stack or queue starts empty.

### How the file is organized

Each item is stored as one line: the string followed by a newline character `"\n"`.

| Structure | Where items are added | Where items are removed |
|---|---|---|
| `FileStack` | `push` adds a new **last** line (the top). | `pop` removes the **last** line. |
| `FileQueue` | `enqueue` adds a new **last** line (the rear). | `dequeue` removes the **first** line (the front). |

After `push("first")`, `push("second")`, `push("third")`, the file `stack.txt` contains:

```
first
second
third
```

Open your files in a text editor while you test. You should be able to see the stack or queue at any moment.

### The file is the only storage

The file must be the **only** place your items live. The only instance variable your classes need is the file path. Do not keep the items, or a count of them, in instance variables. Every method must get its answer by reading the file, and every change must be written to the file.

### Requirements for each operation

- `push(item)` / `enqueue(item)`: store `item` as a new last line.
  - Raise `TypeError` if `item` is not a string.
  - Raise `ValueError` if `item` contains a newline, because it would then take up two lines.
  - The empty string `""` is a valid item. It is stored as an empty line.
- `pop()` / `dequeue()`: remove the item at the top (stack) or front (queue) from the file and return it **without** its trailing newline. Raise `IndexError` if the structure is empty.
- `peek()`: return the item at the top (stack) or front (queue) without removing it, again without the newline. The file must not change. Raise `IndexError` if the structure is empty.
- `is_empty()`: return `True` if the file contains no items.
- `size()`: return the number of items in the file.

### Working with files: what you need

You can open a file in one of three modes. Always use a `with` block, so the file is closed for you.

| Code | Meaning |
|---|---|
| `with open(path, "w") as file:` | Write mode. Creates the file, or **erases** everything already in it. |
| `with open(path, "a") as file:` | Append mode. Anything you write goes to the **end** of the file. |
| `with open(path, "r") as file:` | Read mode. Reading starts at the beginning of the file. |
| `file.write(text)` | Writes the string `text`. It does not add a newline for you. |
| `file.readline()` | Returns the next line, including its `"\n"`. Returns `""` when there are no lines left. |
| `file.read()` | Returns everything from the current position to the end, as one string. |
| `for line in file:` | Visits the lines one at a time. Each `line` ends with `"\n"`. |

Things to think about:

- A file can't remove a line from its beginning or middle in place. To remove an item, you will have to **write the file again** with that item left out. Plan what you need to read before you reopen the file in `"w"` mode, since that mode erases it.
- You may not collect the lines in a list. Think about what other type can hold several lines of text at once.
- An empty line `"\n"` is a real item (the empty string), so `is_empty()` must not treat it as "no item."

### Part 1 scenario

Write a `main()` function **below your class definitions** in `file_stack_queue.py`. Copy the starter below, then complete the `TODO` section.

```python
def main() -> None:
    """Run a short scenario that uses the file stack and file queue."""
    stack = FileStack("stack.txt")
    for word in ("first", "second", "third"):
        stack.push(word)
    print("Stack size:", stack.size())
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())
    print("Stack pop:", stack.pop())
    print("Stack size:", stack.size())
    print()

    queue = FileQueue("queue.txt")
    for word in ("first", "second", "third"):
        queue.enqueue(word)
    print("Queue size:", queue.size())
    print("Queue peek:", queue.peek())
    print("Queue dequeue:", queue.dequeue())
    print("Queue dequeue:", queue.dequeue())
    print("Queue size:", queue.size())
    print()

    # A rejected request raises an exception. Catching it lets the scenario
    # report the problem and continue.
    try:
        FileStack("empty_stack.txt").pop()
        print("ERROR: pop from an empty stack was accepted")
    except IndexError as error:
        print("Empty pop rejected:", error)

    # TODO: Following the pattern above, show that each request below is
    # rejected with the stated exception, printing one line per case:
    #   (a) dequeue from an empty queue                       -> IndexError
    #   (b) peek at an empty stack and at an empty queue      -> IndexError
    #   (c) push a string that contains a newline             -> ValueError
    #   (d) enqueue a value that is not a string, such as 42  -> TypeError
    #   (e) creating StackADT() directly                      -> TypeError
    # Then show that the empty string "" can be pushed and popped back.


if __name__ == "__main__":
    main()
```

When your implementation is correct, the first part of the output is:

```
Stack size: 3
Stack peek: third
Stack pop: third
Stack pop: second
Stack size: 1

Queue size: 3
Queue peek: first
Queue dequeue: first
Queue dequeue: second
Queue size: 1
```

After the run, `stack.txt` contains only `first` and `queue.txt` contains only `third`. A line starting with `ERROR:` means a rule in Part 1 is not enforced.

## Part 2: Time needed to buy tickets

People are standing in line to buy concert tickets. `tickets[i]` is the number of tickets person `i` wants to buy. Person 0 is at the front of the line.

The ticket booth works like this:

1. The person at the front buys **one** ticket. This takes **1 second**.
2. If they still need more tickets, they go to the **back** of the line.
3. If they have all their tickets, they leave the line.

Write a function `time_to_buy(tickets, k)` that returns the number of seconds until person `k` has all their tickets.

### Using `deque` as a queue

Python's built-in queue tool is `deque` (from `collections`), short for "double-ended queue." It can add and remove at both ends, so in this assignment you will use **only** the methods that make it behave as a queue:

| Queue operation | `deque` method | End used |
|---|---|---|
| enqueue (join the back) | `line.append(x)` | right |
| dequeue (leave the front) | `line.popleft()` | left |
| size | `len(line)` | |

`append` adds on the right, so the person who has waited longest is always on the left. That is why dequeue is `popleft()`. The method `pop()` would remove from the right, the newest person, and turn the line into a stack. Do not use `pop()`, `appendleft()`, or indexing.

### Starter code

Save this in `tickets.py` and complete it:

```python
from collections import deque


def time_to_buy(tickets, k):
    """Return the seconds until person k finishes buying tickets."""
    remaining = list(tickets)  # copy so the input is not changed
    line = deque()
    pass
```

### Example 1

```
Input:  tickets = [2, 3, 2], k = 2
Output: 6
```

Each row shows the line and the tickets each person still needs, written as `P#(left)`.

| Second | Buys a ticket | Line after (front to back) |
|---|---|---|
| start | | P0(2) P1(3) P2(2) |
| 1 | P0 | P1(3) P2(2) P0(1) |
| 2 | P1 | P2(2) P0(1) P1(2) |
| 3 | P2 | P0(1) P1(2) P2(1) |
| 4 | P0, done, leaves | P1(2) P2(1) |
| 5 | P1 | P2(1) P1(1) |
| 6 | P2, done | P2 is finished, so return 6 |

### Example 2

```
Input:  tickets = [5, 1, 1, 1], k = 0
Output: 8
```

### Constraints

- `1 <= len(tickets) <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < len(tickets)`
- Do not change the `tickets` list that is passed in. Update `remaining` instead.

### Hint

Put each person's **index** in the line, not their ticket count. Use the index to look up and update how many tickets that person still needs in `remaining`.

## Design reflection

In a short response, answer:

- For `FileStack` and `FileQueue`, what is the cost (Big-O, in terms of the number of items *n*) of each operation? Which operations are cheap, and why are the others expensive?
- The stack and the queue both add at the end of the file. Why is that a good choice for both? What would happen to `push` if the top of the stack were the **first** line instead?
- Your `FileStack` and `FileQueue` satisfy the same ADTs as the list and linked-list versions from class. Give one situation where storing a stack or queue in a file would be useful, despite the cost.
- In Part 2, why is `deque` a better choice than a list for the line? (Recall `ListQueue` from lecture.)

## Submission

Submit on Sakai:

- `file_stack_queue.py`, containing the ADTs, `FileStack`, `FileQueue`, and your completed `main()`;
- `tickets.py`, containing `time_to_buy()`;
- `reflection.pdf`, containing your design reflection in PDF format.

Your program must run with Python's standard library alone, using only the allowed imports. Use meaningful names, docstrings for classes and methods, comments, named constants instead of magic values, and type annotations for method parameters and return values.

## Starter code: the ADTs

Place these at the top of `file_stack_queue.py`. Do not change them.

```python
from __future__ import annotations

from abc import ABC, abstractmethod


class StackADT(ABC):
    """A last-in, first-out collection of strings."""

    @abstractmethod
    def push(self, item: str) -> None:
        """Add item to the top of the stack."""

    @abstractmethod
    def pop(self) -> str:
        """Remove and return the top item; raise IndexError if empty."""

    @abstractmethod
    def peek(self) -> str:
        """Return the top item without removing it; IndexError if empty."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the stack has no items."""

    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the stack."""


class QueueADT(ABC):
    """A first-in, first-out collection of strings."""

    @abstractmethod
    def enqueue(self, item: str) -> None:
        """Add item to the rear of the queue."""

    @abstractmethod
    def dequeue(self) -> str:
        """Remove and return the front item; raise IndexError if empty."""

    @abstractmethod
    def peek(self) -> str:
        """Return the front item without removing it; IndexError if empty."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the queue has no items."""

    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the queue."""
```
