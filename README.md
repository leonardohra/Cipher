# Cipher
Working with several algorithms for encryption and decryption

## ASCII Cipher
Given a numeral system, it converts each character to its decimal number in ASCII and converts this number to the base given.

Example:

"Test"

"54657374" -> 56 = T, 65 = e,  73 = s, 74 = t

## Base 64
It will convert a given text to binary, and separate in chunks of 6 bits in groups of 24 bits, completing with padding characters, and convert these values to a character, using an specific table.

Example:

"Test"

T -> 01010100

e -> 01100101

s -> 01110011

t -> 01110100

______________________________________________

01010100011001010111001101110100

010101|000110|010101|110011| (24 bits)

011101|[0000]00|++++++|++++++| (12 bits + 12 bits for padding characters, the 0's before '00' are implicit)

______________________________________________

010101 -> 21 -> V

000110 -> 6 -> G

010101 -> 21 -> V

110011 -> 51 -> z

011101 -> 29 -> d

[0000]00 -> 0 -> A 

++++++ -> =

++++++ -> =

Result:

VGVzdA==

## Shift Cipher

Given a number n, each character c will become the character of position c + n.

Example:

"Test", 10

T + 10 = **T**, U, V, W, X, Y, Z, A, B, C, **D**

e + 10 = **e**, f, g, h, i, j, k, l, m, n, **o**

s + 10 = **s**, t, u, v, w, x, y, z, a, b, **c**

t + 10 = **t**, u, v, w, x, y, z, a, b, c, **d**

Result:

Dodc

## Vigenère shift

Given a keyword key, each letter of this keyword will be used to encrypt each letter of the text as a Shift Cipher. If the word is bigger than the key, after using all characters in key, comes back to the first.

Example:

"Test", "key"

T - k (10) = D

e - e (4) = i

s - y (24) = q

t - k (10) = d

## Usage
Please refer to main.py to see usages
