# Assignment 8 – Hashing: Open Addressing

## Specifications and Requirements

- Follow the **Programmer's Pact**.
- Do not use dictionaries or sets.
- You may import `random` and `string` to generate test data.
- You may use `matplotlib` to generate your graph. Alternatively, you may use Excel, Google Sheets, or another spreadsheet tool.
- You may add helper methods to the provided `ProbingHashTable` class if needed.
- Start from the provided `week11_starter_updated.py`. Rename your completed file `week11.py`.

## Part 1 – Implement Deletion Using Tombstones

The provided `ProbingHashTable` class supports insertion using linear and quadratic probing. Your first task is to extend it to support deletion.

1. Define a **tombstone marker** to distinguish deleted positions from positions that have never been occupied.
2. Implement the following method:

   ```python
   def remove(self, value: str) -> bool:
       """Remove value if found and return True; otherwise return False."""
   ```

3. Update `insert()` so that deleted positions can be reused when inserting new values, without creating duplicate entries. The provided method returns `(inserted, probes)`, where `inserted` is `True` only when a new entry was added, and `probes` lists the indices checked.
4. Update `contains()` so that searching continues past tombstones.
5. Make sure `_size` and `load_factor()` count only active entries, not tombstones.

Test your implementation with both linear and quadratic probing, including cases involving collisions, deletions, and subsequent insertions.

## Part 2 – Measuring Probing Performance

You will now use the hash table to experimentally compare **linear probing** and **quadratic probing**.

Your goal is to measure how the average number of probes required for insertion changes as the table fills up.

### Instructions

1. Choose a fixed prime number as the table capacity.
2. Generate random strings and insert them into an initially empty hash table.
3. After each successful insertion, record:
   - The load factor after insertion.
   - The number of probes performed, using the `probes` list returned by `insert()`.
4. Repeat the experiment over multiple trials, using a fresh empty table each time.
5. Calculate the average number of probes for each load factor.
6. Perform the experiment separately for linear and quadratic probing.

**Important:** Quadratic probing may fail to insert a value even when empty positions remain. Record failed attempts separately. You may try another random string, but stop after a reasonable number of consecutive failures to avoid an infinite loop. Use the `inserted` Boolean returned by `insert()` to distinguish successful new insertions from failed attempts or duplicate values.

### Generate a graph

Create one graph comparing both probing methods:

- **X-axis:** Load factor (from 0 to 1).
- **Y-axis:** Average number of probes per successful insertion.
- **Two curves:** Linear probing and quadratic probing.

Include a title, labeled axes, and a legend.

You may generate the graph using **Python with Matplotlib**, or export your results to **Excel, Google Sheets, or another spreadsheet tool**.

If you choose Python, see **Appendix A** for installation instructions and a simple plotting example.

## Part 3 – Analyze Your Results

In a short discussion, answer the following questions:

1. How does the average number of probes change as the load factor increases?
2. How do linear and quadratic probing compare at low and high load factors?
3. Does quadratic probing begin to fail before the table is full? What did you observe?
4. Why are tombstones necessary for deletion in open addressing? How might accumulating tombstones affect performance?

## What to Submit

- `week11.py` – Your updated hash table implementation and experimental code.
- `week11.png` (or PDF/JPG) – Your graph comparing linear and quadratic probing.
- `week11.txt` – Your brief discussion of the results.

---

# Appendix A – Generating Graphs with Python

Python provides a plotting library called **Matplotlib** that allows you to generate graphs directly from your code.

Matplotlib is not part of Python's standard library, so you may need to install it first.

### Step 1 – Install Matplotlib

Open a terminal (or the terminal in your IDE) and run:

```bash
python -m pip install matplotlib
```

On some computers, you may need to use `python3` instead of `python`.

You only need to install the library once per Python environment.

### Step 2 – Import Matplotlib

At the beginning of your Python file, add:

```python
import matplotlib.pyplot as plt
```

### Step 3 – Generate a simple graph

Here is an example using sample data. These values are illustrative and are **not** actual experimental results.

```python
import matplotlib.pyplot as plt

load_factors = [0.2, 0.4, 0.6, 0.8]

linear = [1.1, 1.5, 2.3, 4.5]
quadratic = [1.1, 1.3, 1.8, 2.7]

# Plot both curves
plt.plot(load_factors, linear, label="Linear Probing")
plt.plot(load_factors, quadratic, label="Quadratic Probing")

# Add labels and title
plt.xlabel("Load Factor")
plt.ylabel("Average Probes per Insertion")
plt.title("Linear vs Quadratic Probing")

# Display the legend and grid
plt.legend()
plt.grid(True)

# Save the graph as an image
plt.savefig("week11.png")

# Display the graph
plt.show()
```

### Step 4 – Use your experimental results

Replace the sample lists with the load factors and average probe counts obtained from your simulation.

The `plt.savefig("week11.png")` instruction saves the graph as an image that you can submit.

### Additional resources

- [Official Matplotlib installation guide](https://matplotlib.org/stable/install/index.html)
- [Official Matplotlib Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Python documentation – Installing Python Modules](https://docs.python.org/3/installing/index.html)

**Note:** Using Matplotlib is optional. You may instead create your graph in Excel or Google Sheets using the same experimental data.
