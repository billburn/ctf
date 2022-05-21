# Solution

1. Created a python script (./script.py) to help with the modulus 37
2. I iterated over the file, performing a calculation to identify the new value
3. I printed the new value and matched the data to the key (manually)

```
#!/usr/bin/env python3

mod_value = 37

with open('message.txt') as message:
    for line in message:
        data = line.split()
        for i in data:
            new_data = int(i) % mod_value
            print(new_data)
```

## Flag
```
picoCTF{R0UND_N_R0UND_79C18FB3}
```