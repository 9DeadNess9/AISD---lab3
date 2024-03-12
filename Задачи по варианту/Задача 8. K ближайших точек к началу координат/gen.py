import random

f1 = open("input.txt", "w")
n = int(input())
out = int(input())
a = []
f1.write(str(n) + " " + str(out) + "\n")	
for i in range(n):
	x = random.randint(1, 100)
	y = random.randint(1, 100)
	f1.write(str(x) + " " + str(y) + "\n")
