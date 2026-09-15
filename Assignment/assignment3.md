# COMP 271 Programming Assignment: Modular Integers and RSA

## Overview

Most arithmetic that we use every day takes place on the ordinary number line. Adding two positive integers produces a larger integer, and the numbers continue without returning to the beginning. Some systems, however, behave cyclically.

A familiar example is a 12-hour clock. If it is 10 o’clock now, five hours later it will be 3 o’clock:

$$
10 + 5 \equiv 3 \pmod{12}
$$

The value wraps around after reaching 12. This is an example of **modular arithmetic**. In arithmetic modulo \(n\), every integer is represented by its remainder after division by \(n\). For example, when working modulo 12:

$$
17 \equiv 5 \pmod{12}
$$

The integers `5`, `17`, `29`, and `-7` all represent the same value modulo 12.

In this assignment, you will create a `ModularInteger` class to represent a value in a modular number system. Each object will contain:

* A **value**, stored in normalized form
* A **modulus**, which determines when values wrap around

For example:

```python
ModularInteger(17, 12)
```

represents \(17 \pmod{12}\), but it should internally store the normalized value `5`. A normalized value al
