import random

f1 = open("input.txt", "w")
n = int(input())
for i in range(n):
	f1.write(str(random.randint(0, 1000)))
	if i != n - 1:
		f1.write(",")
