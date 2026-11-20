
# COMP 271 Final Exam Study Guide

## About the final

**Friday, December 11, 9:00 to 11:00 am, Cuneo Hall 218.**

The final is not a giant exam on every slide. It checks that you truly own the ideas you have already practiced this semester: if you could solve it in a quiz or an assignment, you are on the right track.

## How to study

- For each topic below, read the "Make sure you can" list and test yourself **without notes**. If a point feels shaky, go back to the material listed under **Revisit**.
- Rework problems you got wrong before, not only the ones you got right. Your past feedback is your best map.
- Trace code by hand: draw the boxes, nodes, slots or call stack after every line.
- Give every cost with O( ), and be ready to explain *why* in one sentence.
- Write code in course style (the Programmer's Pact): type hints, a one-line docstring, named constants, no break/continue.

---

## 1. Recursion and time cost

A recursive function solves a problem by calling itself on a smaller version of it, and time cost tells us how the work grows with n.

### Make sure you can

- Point to the base case, the recursive case, and the progress toward the base case in any recursive function. Say what happens without a base case (RecursionError).
- Trace factorial(4) or sum_to(4) on the call stack: calls wind up, then return values unwind in LIFO order.
- Write a short recursive function yourself, like is_palindrome(text) from class.
- Count the steps of a loop in the worst case and drop constants: 3n + 2 is O(n).
- Rank growth rates: O(1) < O(log n) < O(n) < O(n log n) < O(n²), and say how each grows when n doubles.

**Revisit:** the Recursion slides and recursive.py; the recursive binary search in Assignment 7.

---

## 2. Arrays and linked lists

An array jumps straight to any slot but must shift items to insert or delete; a linked list rewires references but must walk to find anything.

### Make sure you can

- Compute an array slot's address: start + i × slot_size (start 2000, 8-byte slots, i = 3 gives 2024). Don't forget the slot size.
- Explain why a dynamic array's append is amortized O(1) even though a resize copies everything (O(n)).
- Write the traversal loop from memory: start at the head, current = current.next, stop at None.
- Insert after a node in the right order: link the new node to the rest **first**, then link the current node to it.
- Handle the edge cases: an empty list, removing the head, removing the tail or the only node, and updating the size.

**Revisit:** Quiz 2 (the array and linked-list questions, especially the bug fixes); the TrainLine code; the LinkedLookupTable in Assignment 6.

---

## 3. The Sequence/List ADT

An ADT is the promise (what each operation does); a data structure is one way to keep it. Same promise, different cost.

### Make sure you can

- Tell an ADT from a data structure. If a description mentions slots, nodes, next or memory, it is a data structure.
- Explain why ListADT() raises TypeError (you can't create an abstract class, or a subclass that skips an abstract method).
- Write add_unique, remove_first, remove_all, index_of and index_of_all without using in on a list.
- Build one method on another, e.g. contains returns self.index_of(item) != NOT_FOUND.
- Fill in this table and explain each cell:

| Operation | Array | Linked list |
|---|---|---|
| get(i) | O(1) | O(n) |
| Add at front | O(n) | O(1) |
| Add at end | O(1) amortized | O(n), O(1) with a tail |
| contains / index_of | O(n) | O(n) |

**Revisit:** Assignment 2 (the record methods); Assignment 6 (the same contract on a list and on a linked list); the ADT questions in Quiz 2.

---

## 4. Stacks and queues

A stack is LIFO (it reverses order); a queue is FIFO (it keeps order). Every operation should be O(1) if you pick the right end.

### Make sure you can

- Trace a sequence of push/pop or enqueue/dequeue calls and give what is on top or in front.
- Explain why the top is the right end of a Python list, or the head of a linked chain, and what goes wrong with the other end. Changing the end changes the **cost**, not the LIFO behavior.
- In ArrayStack push, move the top up **before** writing the item.
- In a CircularQueue, find the next free slot with (front + size) % capacity and the newest item with (front + size - 1) % capacity. Explain why it keeps a size counter.
- Handle the LinkedQueue edge cases: enqueue on an empty queue sets both front and rear; dequeuing the last item resets rear to None.
- Explain why ListQueue's dequeue with pop(0) is O(n), and why deque with append/popleft fixes it.
- Use a stack to check balanced symbols like ({[]}).

**Revisit:** Quiz 2 (the stack and queue traces and bug fixes); Assignment 5 (the file stack and queue, and the ticket line); the balanced symbols exercise.

---

## 5. Software contracts and unit testing

A contract says what a method needs (preconditions) and what it promises (postconditions); tests check those promises one sentence at a time.

### Make sure you can

- Read a docstring and name its preconditions, postconditions and invariants.
- Predict what an assert does, and spot why assert(x, "msg") never fails (it is a tuple, always true).
- Write a unittest.TestCase class: method names start with test, setUp gives each test a fresh object, and each test follows Arrange, Act, Assert.
- Test an error with with self.assertRaises(KeyError):.
- Read a report: . passed, F failure (an assertion was false), E error (the code crashed).
- List the edge cases worth testing: empty, one item, duplicates, first and last position, a missing key. Test only through the ADT's methods, never private attributes.

**Revisit:** Assignment 6 (the test suite written from the contract); the testing questions in Quiz 3.

---

## 6. Searching and sorting

Binary search is O(log n) but needs a sorted list; merge sort is O(n log n) on every input, while bubble and insertion sort are O(n²) at worst but O(n) on sorted input.

### Make sure you can

- Trace binary search with low, high and mid at each step, for a target that is found and one that is missing.
- Write binary search both iteratively and recursively, and fix the classic bugs: a missing return on the recursive call, low = mid instead of mid + 1.
- Show the list after each bubble sort pass, and explain the early exit when a pass makes no swaps.
- Count the shifts insertion sort makes (one per out-of-order pair).
- Merge two sorted lists with two pointers, and explain why merge sort needs O(n) extra space.
- Choose an algorithm for a situation, e.g. a list that is already almost sorted.

**Revisit:** Assignment 7 (modified bubble sort, the missing number with linear and binary search); the searching and sorting questions in Quiz 3.

---

## 7. Hashing

A hash table turns a key into a slot index, so insert and search are O(1) on average; the hard part is handling collisions.

### Make sure you can

- Compute sum_hash and poly_hash for a short string, then compress with k % N. Explain why anagrams collide under sum_hash and why a prime N spreads keys better.
- Insert keys with separate chaining, and say what search and delete scan.
- Place keys with linear, quadratic and double-hashing probes, and count the slots a search checks (home slot and ending empty slot included).
- Explain why delete leaves a tombstone, not an empty slot, and what search and insert do when they meet one.
- Compute the load factor n/N, say how it affects each method, and describe rehashing (about twice the slots, ideally prime, every key reinserted).
- Name primary vs. secondary clustering, and explain why quadratic probing can fail even with free slots.
- Connect it to Python: dict and set are hash tables, which is why in on them is fast.

**Revisit:** the hashing questions in Quiz 3; Assignment 8 (tombstones and the probing experiment); the hashing slides.

---

## 8. Priority queues and heaps

A priority queue always hands back the most urgent item; a binary heap stored in an array does that with O(log n) insert and remove and an O(1) peek.

### Make sure you can

- List the Priority Queue ADT operations and say how it differs from a regular queue.
- State the two heap rules: a complete tree (filled left to right) and the heap order (each parent at least as urgent as its children).
- Move between tree and array: children of index i are at 2i + 1 and 2i + 2; the parent is at (i - 1) // 2.
- Insert by hand: add at the end, then swap upward. Remove by hand: move the last item to the root, then swap downward with the more urgent child.
- Explain the O(log n) cost (the height of the tree), and compare with a sorted or unsorted list as a priority queue.

**Revisit:** the heap slides and the insertion and deletion examples done in class.

---

## Not on the final

These won't be tested on their own, though you still need basic classes to write the code above.

- The programming refresher: fundamentals, the refactoring case study, nested loops and pattern generation.
- OOP essentials as a topic: public vs. private members, special methods, class vs. instance variables, class and static methods, constants vs. magic values, inheritance and abstraction.
- Quicksort.
- Binary Search Trees.
