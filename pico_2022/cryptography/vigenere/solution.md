# Solution

1. Download the ciphertext
2. We are provided the key "CYLAB"
3. The quick solve, we can use CyberChef and simply get the answer
4. For a more involved solution, we use John Hammond's code, to decode the Vinegere cipher

## Code
```
#!/usr/bin/env python3
# Code sourced from John Hammond's Katana repo - https://github.com/JohnHammond/katana/tree/master/katana/units/crypto

import click
import string

click.clear()

#with open(b"cipher.txt", "r") as f_contents:
#        contents = f_contents.read()

#with open(b"key.txt", "r") as f_key:
#        challenge_key = f_key.read()

#print(contents)
#print(challenge_key)


def vigenere(plaintext, key):
    """
    Perform a vigenere cipher.
    :param plaintext: The plaintext message to use for the Vigenere cipher.
    :param key: The key to use for the Vigenere cipher.
    :return: The resulting ciphertext from the Vignere cipher operation
    """

    plaintext = plaintext.upper()
    key = bytes(key.upper(), "ascii")
    valid_chars = bytes(string.ascii_uppercase, "ascii")

    idx = 0
    ciphertext = ""

    for c in plaintext:
        if c not in valid_chars:
            ciphertext += chr(c)
        else:
            if key[idx] not in valid_chars:
                idx = (idx + 1) % len(key)
            v1 = c - ord("A")
            v2 = key[idx] - ord("A")
            ciphertext += chr(((v1 - v2) % 26) + ord("A"))
            idx = (idx + 1) % len(key)

    return ciphertext

ciphertext = b"rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_cc82272b}"
key = "CYLAB"

print(vigenere(ciphertext, key))

```

## Flag
```
PICOCTF{D0NT_US3_V1G3N3R3_C1PH3R_AE82272Q}
```
