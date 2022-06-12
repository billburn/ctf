#!/usr/bin/env python3

#Solution is from John Hammond => https://www.youtube.com/watch?v=37xo7KQVl8c&list=PL1H1sBF1VAKUbRWMCzEBi61Z_7um7V5Sd&index=28

with open("message.txt", 'r') as f:
	contents = f.read()

#print(contents)

for i in range(0, len(contents), 3):
	chunk = contents[i : i + 3]
	#print(chunk)
	a, b, c = chunk
	print(c + a + b, end="")
