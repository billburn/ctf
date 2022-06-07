# Solution

1. Download the image file
2. Gunzip the .gz file and you are left with disk.img
3. Run mmls -B disk.img and you are presented with some data
4. Connect to the access checker program located here: nc saturn.picoctf.net 52279
5. Input the size of the Linux partion and the flag is returned

## Output from the mmls command
```
└─$ mmls disk.img -B                                                                           │
DOS Partition Table                                                                            │
Offset Sector: 0                                                                               │
Units are in 512-byte sectors                                                                  │
                                                                                               │
      Slot      Start        End          Length       Size    Description                     │
000:  Meta      0000000000   0000000000   0000000001   0512B   Primary Table (#0)              │
001:  -------   0000000000   0000002047   0000002048   1024K   Unallocated                     │
002:  000:000   0000002048   0000204799   0000202752   0099M   Linux (0x83)
```

## Flag
```
picoCTF{mm15_f7w!} 
```

