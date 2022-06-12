# Solution

1. Wget or download the python script
2. Looking at the python code, we have some encoding and some payloads that need to be decoded
3. I simply stepped through code, line by line, in the terminal, and printed the plaintext (plain) after it was decided to get the flag

## Decoded plaintext
```
Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> from cryptography.fernet import Fernet
>>> payload = b'gAAAAABiMD04m0Z6CohVV7ozdwHqtgc2__CuAFGG8rWhZBTL0lhfzp-mhu9LYNMnMQMGO-7tEwy3DJ2Y8yjogvzyojFETwN9YEIPXTnO9F1QnkPypWTgjISGve4gcSerJMs694oKcIdKHuVaSxOg1MMNs5k9iPaBIPU7xOKQqCyhnf_f4yUvLdMcer38BqRptocJNvKlyWN8h7ikoWL0zlssxd8OJyPujMz78HZaefvUouvq6LDtPVqRBJFPgSJYf1nHpHKFa1O0zJ6UpTe6ba3PPAxCVXutNg=='
>>> key_str = 'correctstaplecorrectstaplecorrec'
>>> key_base64 = base64.b64encode(key_str.encode())
>>> f = Fernet(key_base64)
>>> print(f)
<cryptography.fernet.Fernet object at 0x7f42c2203d60>
>>> plain = f.decrypt(payload)
>>> print(plain)
b"\npw = input('What\\'s the password? ')\n\nif pw == 'batteryhorse':\n  print('picoCTF{175_chr157m45_5274ff21}')\nelse:\n  print('That password is incorrect.')\n\n"
```

## Flag
```
picoCTF{175_chr157m45_5274ff21}
```

