# COMP 271 Assignment 3: Modular Integers and RSA

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

represents \(17 \pmod{12}\), but it should internally store the normalized value `5`. A normalized value always satisfies:

$$
0 \leq \text{value} < \text{modulus}
$$

You will use encapsulation to protect the state of each object and dunder methods to make modular integers behave like numerical values:

```python
a = ModularInteger(17, 12)
b = ModularInteger(8, 12)

print(a)       # 5 (mod 12)
print(a + b)   # 1 (mod 12)
print(a * b)   # 4 (mod 12)
```

Because the modulus is part of the number system, arithmetic will be allowed only between objects that use the same modulus.

Finally, you will apply your class to a simplified demonstration of RSA public-key encryption. This will introduce you to an important application of modular arithmetic while giving you additional practice designing and using classes.

> The RSA portion of this assignment is an educational demonstration only. It is not suitable for protecting real information.

## General Requirements

* Include accurate type annotations for all methods.
* Include a class docstring and a docstring for every method.
* Keep the instance attributes encapsulated as instructed.
* Do not access name-mangled attributes directly from outside their class.
* Methods that perform arithmetic must return new objects rather than modifying their operands.
* Include testing code that demonstrates every required behavior.
* Comment your tests.

## Question 1: Defining the `ModularInteger` Class

Create a class named `ModularInteger` with the following attributes:

* `value`: the normalized integer value
* `modulus`: the modulus of the number system; it must be greater than `1`

Use **name mangling** to encapsulate these instance attributes. Their names inside the class should therefore begin with two underscores.

Define the `__init__()` method so that it:

1. Receives an integer `value` and an integer `modulus`.
2. Raises a `ValueError` if `modulus` is invalid.
3. Stores the modulus in the corresponding encapsulated instance attribute.
4. Normalizes `value` and stores the result in the corresponding encapsulated instance attribute.

For example, both objects below should internally store a normalized value of `5` and a modulus of `12`:

```python
a = ModularInteger(17, 12)
b = ModularInteger(-7, 12)
```

## Question 2: Providing Controlled Access

Keep `value` and `modulus` encapsulated, but provide read-only access to them.

Define two properties:

* `value` returns the normalized value.
* `modulus` returns the modulus.

Use the `@property` decorator so that they can be accessed as follows:

```python
a = ModularInteger(17, 12)

print(a.value)      # 5
print(a.modulus)    # 12
```

Do not define setter methods. Once a `ModularInteger` object has been created, its value and modulus should not be modified directly.

## Question 3: String Representation

Implement the `__str__()` method so that it returns the modular integer in the form `"value (mod modulus)"`.

Example:

```python
a = ModularInteger(17, 12)

print(a)       # 5 (mod 12)
print(str(a))  # 5 (mod 12)
```

The method must use the normalized value stored in the object.

## Question 4: Equality

Implement the `__eq__()` method to determine whether two `ModularInteger` objects are equal.

Two modular integers are equal only when they have:

* The same normalized value
* The same modulus

If `other` is not a `ModularInteger`, return `NotImplemented`.

Examples:

```python
a = ModularInteger(17, 12)
b = ModularInteger(5, 12)
c = ModularInteger(5, 7)

print(a == b)  # True
print(a == c)  # False
print(a == 5)  # False
```

## Question 5: Arithmetic Operations

Implement the following dunder methods:

* `__add__()` to add two `ModularInteger` objects using `+`
* `__mul__()` to multiply two `ModularInteger` objects using `*`
* `__pow__()` to raise a `ModularInteger` to a power using `**`

Addition and multiplication are allowed only when both operands have the same modulus. If their moduli differ, raise a `ValueError`.

For exponentiation, the exponent must be a nonnegative integer. Otherwise, raise a `ValueError`.

Every operation must return a new `ModularInteger` object without modifying the original operand or operands.

Example:

```python
a = ModularInteger(10, 12)
b = ModularInteger(7, 12)

print(a + b)   # 5 (mod 12)
print(a * b)   # 10 (mod 12)
print(a ** 3)  # 4 (mod 12)
```

These results correspond to:

$$
(10 + 7) \bmod 12 = 5
$$

$$
(10 \times 7) \bmod 12 = 10
$$

$$
10^3 \bmod 12 = 4
$$

## Question 6: A Class Variable and an Alternative Constructor

Define a class variable named `CLOCK_MODULUS` with the value `12`.

Then define a class method named `from_clock()` that receives an integer representing an hour and creates a `ModularInteger` using `CLOCK_MODULUS` as its modulus.

The class method must use `cls` to create and return the object rather than referring to `ModularInteger` directly.

Example:

```python
morning = ModularInteger.from_clock(9)
afternoon = ModularInteger.from_clock(15)

print(morning)    # 9 (mod 12)
print(afternoon)  # 3 (mod 12)
```

## Question 7: Testing Relative Primality

Define a static method named `are_coprime()` that receives two integers and returns `True` when their greatest common divisor is `1`. Otherwise, it returns `False`.

Because this operation does not depend on a particular object or on the class itself, implement it as a static method. You may use `math.gcd()`.

Examples:

```python
print(ModularInteger.are_coprime(8, 15))   # True
print(ModularInteger.are_coprime(12, 18))  # False
```

> **Note:** Two integers are **relatively prime**, or **coprime**, when their only common positive divisor is `1`. This property plays an important role in modular arithmetic and public-key cryptography.

## Question 8: An Object-Oriented RSA Demonstration

RSA is a public-key encryption system based on modular arithmetic. It uses a **public key** to encrypt information and a **private key** to decrypt it.

For this simplified example, use:

```python
p = 61
q = 53
e = 17
d = 2753
```

The modulus used during encryption and decryption is:

$$
n=pq=61\times53=3233
$$

### Informative: How Are These Values Chosen?

This explanation is provided for context only. You are **not** required to generate RSA keys or prove why RSA works.

In real RSA, \(p\) and \(q\) are two different, very large prime numbers selected using a secure random process. They must remain secret. Their product \(n=pq\) becomes part of both the public and private keys. RSA relies partly on the fact that multiplying two large prime numbers is easy, while recovering them from their product is computationally difficult.

RSA also calculates:

$$
\phi(n)=(p-1)(q-1)=3120
$$

Think of \(\phi(n)\) as a number used to connect the public exponent \(e\) to the private exponent \(d\). The value \(e\) is chosen to be coprime with \(\phi(n)\), and \(d\) is chosen so that:

$$
ed\equiv1\pmod{\phi(n)}
$$

In this example:

$$
17\times2753\equiv1\pmod{3120}
$$

This relationship allows an operation performed using \(e\) to be reversed using \(d\). Therefore, `17` is used to encrypt a value, while `2753` is used to recover it.

The small primes `61` and `53` are provided to make the example easy to test. Real RSA uses much larger primes and additional security measures.

> **Curious to learn more?** The optional chapter [RSA — *The Joy of Cryptography*](https://joyofcryptography.com/rsa/) explains the modular arithmetic behind RSA, how the keys are constructed, and why encryption and decryption reverse one another. It includes definitions, examples, and mathematical proofs. This reading is provided only for further exploration and is not required for the assignment.

### Part A: The `RSAEncryptor` Class

Create a class named `RSAEncryptor` to represent the fixed educational RSA system described above.

Define the following class constants:

* `P`, with the value `61`
* `Q`, with the value `53`
* `E`, with the value `17`
* `D`, with the value `2753`
* `N`, calculated as `P * Q`
* `PHI`, calculated as `(P - 1) * (Q - 1)`

The uppercase names indicate that these values are intended to remain constant.

The class does not need a constructor or any instance attributes. Its encryption and decryption operations will use the shared class constants directly.

### Part B: Encrypting a Letter

RSA encrypts the integer representation of a message using:

$$
\text{encrypted}=\text{message}^{e}\bmod n
$$

Implement a class method named `encrypt()` that receives a string containing one character, applies this formula, and returns the encrypted value as a `ModularInteger` object.

Your method must use:

* `ord()` to obtain the character’s integer representation
* The `ModularInteger` class to represent the message
* The `**` operator defined by `ModularInteger` to perform the encryption
* `cls.E` and `cls.N` to access the RSA class constants

Raise a `ValueError` if:

* The provided string does not contain exactly one character.
* The character’s integer representation is greater than or equal to `N`, because RSA can recover the original value only when it is smaller than the modulus.

### Part C: Decrypting a Value

RSA decrypts an encrypted value using:

$$
\text{decrypted}=\text{encrypted}^{d}\bmod n
$$

Implement a class method named `decrypt()` that receives an encrypted `ModularInteger`, applies this formula, and returns the recovered character as a `str`.

Your method must use:

* The `**` operator defined by `ModularInteger` to perform the decryption
* `chr()` to convert the recovered integer into a character
* `cls.D` and `cls.N` to access the RSA class constants

Raise a `ValueError` if the encrypted object’s modulus is different from `N`.

### Part D: Testing the RSA Class

Before testing encryption, use `ModularInteger.are_coprime()` to verify that `RSAEncryptor.E` and `RSAEncryptor.PHI` are coprime.

Also verify that:

$$
(\text{E}\times\text{D})\bmod\text{PHI}=1
$$

Then test the RSA class with at least three different letters.

> **Hint:** You do not need to create an `RSAEncryptor` object.

For each letter:

1. Display the original letter and its integer value.
2. Encrypt the letter using `RSAEncryptor.encrypt()`.
3. Display the normalized value of the encrypted `ModularInteger`.
4. Decrypt it using `RSAEncryptor.decrypt()`.
5. Display the recovered letter.
6. Verify that the recovered letter matches the original letter.

Testing the letter `"A"` should demonstrate:

```text
Original letter: A
Original value: 65
Encrypted value: 2790
Recovered letter: A
```

## Submission

Submit one Python file containing:

* The completed `ModularInteger` class
* The completed `RSAEncryptor` class
* Your commented testing code for all required behaviors

Your file must run without syntax or runtime errors.
