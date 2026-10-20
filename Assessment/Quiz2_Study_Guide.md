# COMP 271 Quiz 2 Study Guide: Lists, Stacks & Queues


## About the quiz

The quiz covers: Arrays, Linked Lists, ADTs, Stacks and Queues. It is a 45-minute Sakai quiz with two kinds of questions.

- **Multiple choice:** concepts, vocabulary, and Big-O costs.
- **Reading code:** explain what a short piece of code does or prints, or find and fix the bug.

**How to study:** for each structure, know (1) the rule it follows, (2) its operations, (3) what each one costs, and (4) the edge cases (empty, full, one item). Practice tracing code by hand: draw the boxes or nodes after every line.

## 1. Abstract Data Types (ADTs)

An **ADT** describes a kind of data by its operations and what each one promises, without saying how the data is stored. A **data structure** is one concrete way to keep those promises.

|  | ADT (the menu) | Data structure (the kitchen) |
| --- | --- | --- |
| Answers | What can it do? | How is it built? |
| Talks about | Operations and promises | Slots, nodes, references, memory |
| In Python | Abstract class (`ABC`, `@abstractmethod`) | Concrete subclass |
| Examples | ListADT, StackADT, QueueADT | ArrayList, LinkedList, ArrayStack, LinkedQueue, Python's list |

- **Kitchen test:** if a description mentions slots, nodes, `next`, or memory, it is a data structure, not an ADT.
- You **can't instantiate** an abstract class: `ListADT()` raises `TypeError`. A subclass that forgets even one abstract method can't be created either.
- A method can be written once in the ADT using other promises, e.g. `contains` returns `self.index_of(item) != NOT_FOUND`.
- Same promise, different cost: `get(i)` is O(1) in ArrayList (jump) but O(n) in LinkedList (walk).
- Python's `list` is a **data structure** (dynamic array) that keeps the list ADT's promises.


## 2. Arrays

An array is a fixed number of equal-sized slots, side by side in memory. Each slot has an index 0, 1, 2, … and the capacity is fixed when the array is created.

- **Access is O(1)** because the computer calculates the address: `address = start + i × slot_size` (e.g. 2000 + 3 × 8 = 2024).
- **Arrays can't have holes.** Deleting or inserting anywhere but the end means shifting items: O(n).
- **Insert in the middle:** shift from the end first, or you overwrite items.
- **Full array:** a true array can't grow. Python's list allocates a bigger array, copies everything, then adds. That one call is O(n), but on average `append` is **amortized O(1)**.
- A Python list is a **dynamic array**.

| Operation | Python | Cost |
| --- | --- | --- |
| Access / modify | `a[i]`, `a[i] = x` | O(1) |
| Delete at end | `a.pop()` | O(1) |
| Delete elsewhere | `a.pop(i)`, `del a[i]`, `a.remove(x)` | O(n) |
| Add at end | `a.append(x)` | O(1) amortized |
| Add elsewhere | `a.insert(i, x)` | O(n) |

**Rule of thumb:** anything that shifts or copies items is O(n); anything that just jumps is O(1).

## 3. Linked lists

A linked list is a chain of **nodes**. Each node holds `data` and `next` (a reference to the next node). The list only remembers the **head**; the last node's `next` is `None`. Nodes can live anywhere in memory: no capacity, no shifting.

```python
class _Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
```

**Traversal (the core skill):** start at the head, step with `current = current.next`, stop when `current is None`.

```python
current = self.__head
while current is not None:
    print(current.data)
    current = current.next
```

**Key operations:**

- `add_first`: `self.__head = _Node(name, self.__head)` then `size += 1`. **O(1)**.
- `add_last`: walk until `current.next is None`, then hook on the new node. **O(n)** (empty list: the new node becomes the head).
- `insert_after(current)`: `current.next = _Node(name, current.next)`. **Order matters:** new node points to the rest first, then current points to the new node. Do it backwards and you lose the rest of the list.
- `get(i)`: walk `i` steps from the head. **O(n)** (array: O(1)).
- `remove`: walk with `previous` trailing `current`, then `previous.next = current.next`. If `previous is None`, it's the head: `self.__head = current.next`.

**Common bugs:** forgetting to update `__size`; forgetting the empty-list or head case; calling `.data` on `None` (`AttributeError`).


## 4. Stacks (LIFO)

A stack is **Last In, First Out**: items enter and leave at one end, the **top**. Push A, B, C and you pop C, B, A (a stack **reverses** order).

**Stack ADT:** `push(item)`, `pop()`, `peek()`, `is_empty()`, `size()`. No `get(i)` or `insert(i, x)`: only the top is reachable. `pop()`/`peek()` on an empty stack raise `IndexError`.

**Uses:** undo (Ctrl+Z), browser Back button, bracket matching, function call stack (recursion), expression evaluation, backtracking.

|  | ListStack | ArrayStack | LinkedStack |
| --- | --- | --- | --- |
| Storage | Python list | `[None] * capacity` | chain of nodes |
| Top is at | right end (`[-1]`) | index `__top` (-1 = empty) | head node |
| push / pop / peek | O(1) (push amortized) | O(1) | O(1) |
| Can be full? | no | yes (`OverflowError`) | no |

**Why these ends?** Using the left end of a list as the top would make push/pop O(n) (shifting). Using the tail of a chain would need a walk to find the node before it.

```python
# ArrayStack push: move the top up, then fill
if self.__top == self.__capacity - 1:
    raise OverflowError(FULL_STACK)
self.__top += 1
self.__data[self.__top] = item

# LinkedStack pop
item = self.__top.data
self.__top = self.__top.next
self.__size -= 1
```

In ArrayStack `pop`, the slot is set to `None` so the popped object can be garbage-collected. Size is `__top + 1`.

## 5. Queues (FIFO)

A queue is **First In, First Out**: items join at the **rear** and leave from the **front**. Enqueue A, B, C and you dequeue A, B, C (a queue **preserves** order).

**Queue ADT:** `enqueue(item)`, `dequeue()`, `peek()`, `is_empty()`, `size()`. No cutting in line, no leaving from the middle. `dequeue()`/`peek()` on an empty queue raise `IndexError`.

**Uses:** print queue, keyboard buffer, CPU scheduling, messaging, web server requests, breadth-first search.

|  | ListQueue | CircularQueue | LinkedQueue |
| --- | --- | --- | --- |
| Storage | Python list | `[None] * capacity` (ring) | chain of nodes |
| Front / rear | index 0 / right end | `__front` / computed | head / tail (`__front`, `__rear`) |
| enqueue | O(1) amortized | O(1) | O(1) |
| dequeue | **O(n)** (`pop(0)` shifts) | O(1) | O(1) |
| Can be full? | no | yes | no |

**CircularQueue** moves the front, not the items. `%` wraps an index past the end back to 0.

```python
# enqueue
rear = (self.__front + self.__size) % self.__capacity
self.__data[rear] = item
self.__size += 1

# dequeue
item = self.__data[self.__front]
self.__data[self.__front] = None
self.__front = (self.__front + 1) % self.__capacity
self.__size -= 1
```

It keeps `__size` because with only front and rear indexes, full and empty look the same.

**LinkedQueue edge cases:** enqueue on an empty queue sets **both** `__front` and `__rear` to the new node. Dequeuing the last item must also set `__rear = None`.

**In practice:** use `collections.deque` (`append`, `popleft`), which is O(1) at both ends.

## 6. Big-O cheat sheet: array vs. linked list

| Operation | Array (Python list) | Linked list | Why |
| --- | --- | --- | --- |
| Get by index | O(1) | O(n) | Arrays calculate; lists walk |
| Add at front | O(n) | O(1) | Arrays shift; lists rewire the head |
| Add at end | O(1) amortized | O(n) | List walks to the tail (unless it keeps a tail reference) |
| Insert after a node you hold | O(n) | O(1) | Arrays shift; lists rewire two links |
| Search (contains) | O(n) | O(n) | Both check items one by one |
| Length | O(1) | O(1) | Both keep a counter |

Neither one wins everywhere. Every stack and queue operation is O(1), **except** ListQueue's `dequeue`, which is O(n).

## 7. Practice multiple choice

Try each one before reading the answer.

1. Why is `a[i]` O(1) for an array?
   - A) Python caches every item  B) The address is calculated as start + i × slot\_size  C) It searches from index 0  D) Arrays are sorted
   - **Answer: B**
2. What does `scores.insert(0, x)` cost on a list of n items?
   - A) O(1)  B) O(log n)  C) O(n)  D) O(n²)
   - **Answer: C** (every item shifts right)
3. In a linked list, what does the last node's `next` hold?
   - A) The head  B) 0  C) `None`  D) Itself
   - **Answer: C**
4. Which is an **ADT**, not a data structure?
   - A) A chain of nodes with `next`  B) Python's list  C) "Put items in, take the newest one out first"  D) ArrayList
   - **Answer: C** (behavior only: the Stack ADT)
5. Push 1, 2, 3 onto a stack, then pop twice. What is on top?
   - A) 1  B) 2  C) 3  D) Empty
   - **Answer: A**
6. Enqueue 1, 2, 3, then dequeue once. What does `peek()` return?
   - A) 1  B) 2  C) 3  D) Error
   - **Answer: B**
7. Which queue kitchen has an O(n) dequeue?
   - A) ListQueue  B) CircularQueue  C) LinkedQueue  D) None of them
   - **Answer: A** (`pop(0)` shifts every item)
8. A CircularQueue has capacity 5, `__front = 3`, `__size = 4`. Where does the next enqueue go?
   - A) Index 7  B) Index 2  C) Index 4  D) It is full
   - **Answer: B** ((3 + 4) % 5 = 2)
9. Why does LinkedStack use the **head** as the top?
   - A) Push and pop change one reference: O(1)  B) It saves memory  C) The tail can't hold data  D) No reason
   - **Answer: A**
10. What happens with `lst = ListADT()` when ListADT is an abstract class?
    - A) An empty list is made  B) `TypeError`  C) `None` is returned  D) `IndexError`
    - **Answer: B**
11. Which application needs a **queue**, not a stack?
    - A) Undo  B) Back button  C) Bracket matching  D) Print jobs
    - **Answer: D**
12. Python's list `append` is usually O(1) but sometimes O(n). The average is called…
    - A) worst case  B) amortized O(1)  C) O(log n)  D) constant overflow
    - **Answer: B**

## 8. Practice reading code

### Part A: What does it print? What does it do?

**A1.** What is printed?

```python
stack = []
stack.append(4)
stack.append(7)
stack.append(1)
stack.pop()
stack.append(9)
print(stack[-1], len(stack))
```

**Answer:** `9 3`. The 1 is popped (LIFO), then 9 becomes the new top.

**A2.** What does the traversal print, and what did the last line do?

```python
a = _Node("A")
b = _Node("B")
c = _Node("C")
a.next = b
b.next = c
a.next = c
```

**Answer:** `A -> C -> None`. The last line bypasses B, so B is removed from the chain (nothing reaches it anymore).

**A3.** Explain what this function does and give its Big-O.

```python
def mystery(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
```

**Answer:** It walks the whole linked list and returns the number of nodes. O(n).

**A4.** A bracket checker pushes every opener and pops on every closer. What is on the stack after reading `"({["`?

**Answer:** `(`, `{`, `[` with `[` on top. The next closer must be `]`.

### Part B: Find and fix the bug

**B1.** `insert_after` loses the rest of the list.

```python
new_node = _Node(name)
current.next = new_node
new_node.next = current.next
```

**Bug:** wrong order. After line 2, `current.next` is already `new_node`, so `new_node` points to itself and the old rest of the list is lost. **Fix:** link the new node to the rest first: `new_node.next = current.next`, then `current.next = new_node` (or one line: `current.next = _Node(name, current.next)`).

**B2.** ArrayStack `push`:

```python
def push(self, item):
    if self.__top == self.__capacity - 1:
        raise OverflowError(FULL_STACK)
    self.__data[self.__top] = item
    self.__top += 1
```

**Bug:** writes before moving the top. On an empty stack `__top` is -1, so the item lands in the last slot; after that, each push overwrites the current top. **Fix:** swap the two lines: `self.__top += 1` first, then `self.__data[self.__top] = item`.

**B3.** ListQueue `dequeue`:

```python
def dequeue(self):
    if self.is_empty():
        raise IndexError(EMPTY_QUEUE)
    return self.__data.pop()
```

**Bug:** `pop()` removes the **rear** (last in), so this behaves like a stack (LIFO). **Fix:** `return self.__data.pop(0)` to remove the front (FIFO).

**B4.** LinkedQueue `enqueue`:

```python
def enqueue(self, item):
    node = _Node(item)
    self.__rear.next = node
    self.__rear = node
    self.__size += 1
```

**Bug:** no empty-queue case. When the queue is empty, `__rear` is `None`, so `self.__rear.next` raises `AttributeError`. **Fix:** `if self.is_empty(): self.__front = node`, `else: self.__rear.next = node`, then `self.__rear = node`.

**B5.** CircularQueue `dequeue`:

```python
item = self.__data[self.__front]
self.__data[self.__front] = None
self.__front += 1
self.__size -= 1
return item
```

**Bug:** `__front` never wraps around, so it runs past the last slot (`IndexError`). **Fix:** `self.__front = (self.__front + 1) % self.__capacity`.

**B6.** LinkedList `remove` crashes when removing the first item.

```python
previous.next = current.next
self.__size -= 1
```

**Bug:** when the match is the head, `previous` is `None`. **Fix:** `if previous is None: self.__head = current.next`, `else: previous.next = current.next`.
