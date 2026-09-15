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

[
n=pq=61\times53=3233
]

### Informative: How Are These Values Chosen?

This explanation is provided for context only. You are **not** required to generate RSA keys or prove why RSA works.

In real RSA, (p) and (q) are two different, very large prime numbers selected using a secure random process. They must remain secret. Their product (n=pq) becomes part of both the public and private keys. RSA relies partly on the fact that multiplying two large prime numbers is easy, while recovering them from their product is computationally difficult.

RSA also calculates:

[
\phi(n)=(p-1)(q-1)=3120
]

Think of (\phi(n)) as a number used to connect the public exponent (e) to the private exponent (d). The value (e) is chosen to be coprime with (\phi(n)), and (d) is chosen so that:

[
ed\equiv1\pmod{\phi(n)}
]

In this example:

[
17\times2753\equiv1\pmod{3120}
]

This relationship allows an operation performed using (e) to be reversed using (d). Therefore, `17` is used to encrypt a value, while `2753` is used to recover it.

The small primes `61` and `53` are provided to make the example easy to test. Real RSA uses much larger primes and additional security measures.

> **Curious to learn more?** The optional chapter [RSA — ](https://joyofcryptography.com/rsa/)[*The Joy of Cryptography*](https://joyofcryptography.com/rsa/) explains the modular arithmetic behind RSA, how the keys are constructed, and why encryption and decryption reverse one another. It includes definitions, examples, and mathematical proofs. This reading is provided only for further exploration and is not required for the assignment.

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

[
\text{encrypted}=\text{message}^{e}\bmod n
]

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

[
\text{decrypted}=\text{encrypted}^{d}\bmod n
]

Implement a class method named `decrypt()` that receives an encrypted `ModularInteger`, applies this formula, and returns the recovered character as a `str`.

Your method must use:

* The `**` operator defined by `ModularInteger` to perform the decryption
* `chr()` to convert the recovered integer into a character
* `cls.D` and `cls.N` to access the RSA class constants

Raise a `ValueError` if the encrypted object’s modulus is different from `N`.

### Part D: Testing the RSA Class

Before testing encryption, use `ModularInteger.are_coprime()` to verify that `RSAEncryptor.E` and `RSAEncryptor.PHI` are coprime. Also verify that:

[
(\text{E}\times\text{D})\bmod\text{PHI}=1
]

Then test the RSA class with at least three different letters (hint: you do not need to create an `RSAEncryptor` object)

For each letter:

1. Display the original letter and its integer value.
2. Encrypt the letter using `encrypt()`.
3. Display the normalized value of the encrypted `ModularInteger`.
4. Decrypt it using `decrypt()`.
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
