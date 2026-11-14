# Quiz 3 Study Guide

Dr. Ennaoui

**Monday, Nov 23, remotely on Sakai. 12 questions: multiple choice and short answer. 50 minutes.**

## On the quiz

- Short answers ask you to **read** code (trace what it does or prints), **explain** it, **correct** it (find and fix the bug), or **modify** it.
- Main focus of the quiz: hash tables and sorting. Give every time/space cost with O( ).

## Testing ([Testing slides](https://sakai.luc.edu/access/content/group/COMP_271_002_2440_1266/Slides/Testing_assert_and_unittest.pdf), Week 9)

- **assert.** `assert condition, message` checks that the condition is True: if it is, nothing happens; if not, it raises `AssertionError` with the message and the program stops. It is a statement and returns no value. The first failing assert stops the run, and `assert(x, "msg")` is a tuple, always True, so it never fails.
- **unittest.** Python's built-in testing framework: it runs every test and reports each one. A test class inherits from `unittest.TestCase`; every test method's name starts with `test` (any other method never runs); `setUp` runs before each test, `tearDown` after.
- **Assertion methods.** `self.assertEqual(a, b)`, `self.assertTrue(x)`, `self.assertFalse(x)`, `self.assertIsNone(x)`, `self.assertIn(a, b)`, and `with self.assertRaises(Error):`, which passes only if the block raises that error.
- **Running.** `unittest.main()` under `if __name__ == "__main__":`, or `python -m unittest test_file.py`. Read the report: `.` passed, `F` failure (an assertion was false), `E` error (the code crashed), then `OK` or `FAILED`.
- **What to test.** Preconditions (bad input is rejected), postconditions (the return value and the new state), edge cases (empty, one item, duplicates, first and last position, absent target), and normal cases, written as Arrange, Act, Assert. Passing tests do not prove there are no bugs.

## Hash tables ([Hashing slides](https://sakai.luc.edu/access/content/group/COMP_271_002_2440_1266/Slides/Week10_Hashing_Intro.pdf), Weeks 12  and  13)

- **Hash table = array of N slots + hash function.** To insert or search a (key, value) pair, compute the key's hash value and go to the slot at that index: O(1) on average.
- **Good hash functions** are deterministic, spread keys evenly, and run in O(1).
- **Convert, then compress.** Convert turns a key into an integer: `sum_hash` adds the `ord` codes, so all anagrams collide ("cat" and "act" are both 312); `poly_hash` weights each character by its position with `total = total * 31 + ord(ch)` ("cat": 99, 3166, 98262). Compress gives a slot from 0 to N - 1 with `k % N` (41 % 11 = 8). A prime N spreads keys that share a pattern: 10, 20, 30, 40, 50 all land in slot 0 with N = 10, but in 10, 9, 8, 7, 6 with N = 11.
- **Collisions are inevitable.** Pigeonhole principle: more keys than slots puts two keys in one slot. Birthday paradox: 23 keys in 365 slots collide more often than not, so collisions come early, long before the table is full.
- **Separate chaining.** Each slot holds a chain. Insert: the hash picks one chain; replace the value if the key is there, else append the pair. Search: scan only that chain, return `None` if the key is missing. Delete: remove the pair from its chain. Cost O(1 + n/N), O(n) if every key shares one chain; needs extra memory for the chains; n/N can pass 1.
- **Open addressing.** One key per slot, no extra memory. When the home slot is taken, probe other slots, wrapping from N - 1 to 0:
  - **Linear probing:** h, h+1, h+2, ... Watch for primary clustering (keys with different homes pile into one run, and runs keep growing). Very cache friendly (it checks neighbouring slots).
  - **Quadratic probing:** h, h+1, h+4, h+9, ... Watch for secondary clustering (keys with the same home try the same slots). The jumps can skip free slots, so it may refuse an insert even with room available; keep N prime and the table under half full.
  - **Double hashing:** h, h+s, h+2s, ... where s = h2(k) is each key's own step (given on the quiz). A step of 0 never leaves home. It may refuse an insert even with room available if s shares a factor with N; a prime N lets any step reach every slot.
- **Insert, search, delete under probing.** Insert follows the probes to the key (replace) or to the first empty slot. A search hit stops at the key; a miss walks on to an empty slot. Count the slots checked, home slot and ending empty slot included. Delete puts a tombstone, not an empty slot: searches walk past it and inserts may reuse it; emptying the slot would cut the probe path, so later searches would miss keys.
- **Example.** N = 11, linear probing, insert 22, 33, 5, 44, 16, 13: they land in slots 0, 1, 5, 2, 6, 3. A search for 55 checks slots 0, 1, 2, 3, 4: 5 slots.
- **Load factor** α = n/N (keys stored over slots). Under chaining it is the average chain length, can pass 1, and the cost is about 1 + α. Under open addressing α ≤ 1, and the cost stays small at low α but explodes as α nears 1. A higher α means longer chains and longer runs.
- **Rehashing.** Grow when α passes a limit (near 1 for chaining, about 0.7 for linear probing): allocate about twice the slots, ideally prime (11 becomes 23), and reinsert every key, since k % 23 differs from k % 11. One resize costs O(n), but the average insert stays O(1) amortized. Rehashing also clears out tombstones.

## Searching ([Searching slides](https://sakai.luc.edu/access/content/group/COMP_271_002_2440_1266/Slides/Searching.pdf), Week 10)

- **Linear search.** Works on any list: check items one by one. O(n) (O(1) if the target is first).
- **Binary search.** Sorted list only. Compare the middle of `[low, high]` to the target: equal, found; smaller, `low = mid + 1`; bigger, `high = mid - 1`; `low > high`, not found (return -1). O(log n), since each step halves the range. Trace low, high and mid at each step.
- **Iterative vs recursive.** Iterative: a `while low <= high` loop, O(1) extra space. Recursive: base cases are an empty range and a found target, then one recursive call with the new bounds; O(log n) call stack. Common bugs: no `return` on the recursive call's result; `low = mid` instead of `mid + 1`.

## Sorting ([Sorting slides](https://sakai.luc.edu/access/content/group/COMP_271_002_2440_1266/Slides/COMP271_Sorting%20_1_.pdf), Week 11)

- **Bubble sort.** Swap neighbours that are out of order; each pass moves the largest remaining item to the end; stop after a pass with no swaps. O(n²) worst case, O(n) on sorted input. \[4, 1, 3, 2\]: pass 1 gives \[1, 3, 2, 4\], pass 2 gives \[1, 2, 3, 4\], pass 3 has no swaps, so stop.
- **Insertion sort.** Take the next item (the key), shift bigger items in the sorted part one slot right, and drop the key into the opening. One shift per out-of-order pair (\[3, 6, 2, 8, 1\] needs 6). O(n²) on reversed input, O(n) on sorted input.
- **Merge sort.** Split in half until pieces have one item, then merge pairs with two pointers (copy the smaller front item; `<=` keeps equal items in order). O(n log n) on every input (log n levels, O(n) work per level), O(n) extra space; T(n) = 2T(n/2) + cn.

## Be able to tell apart

- **assert vs unittest:** stops at the first false condition, or runs every test and reports each.
- **Failure vs error:** an assertion was false, or the code crashed.
- **sum\_hash vs poly\_hash:** order is ignored, so anagrams collide, or each position has its own weight.
- **Separate chaining vs open addressing:** a chain per slot (extra memory, α can pass 1), or one key per slot (no extra memory, α ≤ 1).
- **Hit vs miss under probing:** stops at the key, or walks on to an empty slot.
- **Linear vs quadratic vs double hashing:** h +1, +2, +3; h +1, +4, +9; or a step set by each key.
- **Primary vs secondary clustering:** keys with different homes pile into one run, or keys with the same home try the same slots.
- **Empty slot vs tombstone:** ends a search, or the search keeps going.
- **Linear vs binary search:** any list in O(n), or a sorted list in O(log n).
- **Insertion vs merge sort on sorted input:** O(n), or still O(n log n).

## Not on the quiz

- Earlier material on its own (linked lists, stacks, queues, recursion); it can appear only inside questions on the topics above.
- Anything after hashing: heaps, priority queues...
- Selection sort, quicksort, bucket sort.
- Big Theta and Big Omega (use O( ) only).
- Aspects of these topics not listed here, such as how Python's `dict` stores keys.
