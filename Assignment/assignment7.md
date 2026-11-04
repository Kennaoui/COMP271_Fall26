# COMP 271: Assignment 7, Searching and Sorting Algorithms

## Exercise 1: Modified Bubble Sort (5)

In class, we studied an implementation of **Bubble Sort** that compares adjacent elements and moves the largest remaining element to the end of the list after each pass.

**Q1.** Modify the Bubble Sort implementation seen in class so that each pass moves the **smallest remaining element to the beginning** of the unsorted portion instead.

Keep the early-exit optimization: the algorithm should stop if a complete pass makes no swaps.

Add print statements in your Bubble Sort function to show the state of the list after each pass until it is sorted.

**Q2.** What are the best-case and worst-case time complexities of your modified implementation? Explain briefly. **Write your answer as comments directly below the function in your `.py` file.**

**Submission:** `bubble_sort.py`

---

## Exercise 2: Find the Missing Number (10)

You are given an **unsorted list of integers** that should contain every integer from `min_val` to `max_val`, except for **exactly one missing number**. There are no duplicates.

For example:

```python
numbers = [5, 2, 8, 1, 6, 3, 7]
min_val = 1
max_val = 8
```

The missing number is `4`.

**Q1. Linear Search**

Write a function that finds the missing number using a linear search. Do not sort the list.

```python
def find_missing_linear(numbers: list[int],
                        min_val: int, max_val: int) -> int:
```

**Q2. Binary Search**

Write another function that:

1. Sorts the list using Python's `.sort()` method.
2. Uses a **modified Binary Search** to find the missing number. Implement two versions: a recursive then an iterative implementation.

```python
def find_missing_binary_rec(numbers: list[int],
                        min_val: int, max_val: int) -> int:
```

```python
def find_missing_binary_iter(numbers: list[int]) -> int:
```

*Hint:* In a complete sorted list, what value should appear at index `i`? How can you use this information to decide which half to search?

---

## Exercise 3: Exploring Python's Sorting Algorithm (Reflection) (5)

Python's built-in `.sort()` method uses an algorithm based on **Timsort**.

Research Timsort and answer the following questions in your own words:

**Q1.** What is Timsort? Which sorting algorithms does it combine ideas from, how does it work, and what is its time complexity?

**Q2.** Consider the following list:

```python
numbers = [2, 5, 8, 11, 1, 4, 9, 12, 3, 6, 7, 10]
```

Notice the three already sorted sequences included in `numbers`.

Using a **simplified illustration of Timsort**, show how these runs can be merged step by step to obtain the fully sorted list.

You do not need to reproduce the exact behavior of Python's implementation (such as minimum run lengths or other optimizations). Focus on explaining how Timsort takes advantage of existing ordered sequences.
