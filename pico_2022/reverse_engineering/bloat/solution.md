# Solution

1. Download the python file and the encrypted flag
2. Analze the data that is in the files
3. Looking at the python file, we have the key in the "a" variable
4. Systematically, I went through each of the functions and decoded the sections, and modified the code with the decoded text
5. See example below
6. Using this technique, we learn the password is "happychance"
7. Run the python script with the password "happychance" to decrypt the flag "flag.txt.enc"


## Key
```
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
```

## Sample decode
```
def arg133(arg432):
  #if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
  if arg432 == "happychance":
    return True
  else:
#     print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
# a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
# a[81]+a[68]+a[66]+a[83])

    print("The password is incorrect")
```

## Flag
```
picoCTF{d30bfu5c4710n_f7w_b8062eec}
```
