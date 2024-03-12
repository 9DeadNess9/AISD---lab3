import random

f1 = open("input.txt", "w")
n = int(input())
for i in range(n):
	f1.write(str(random.randint(1, 1000000000)) + " ")
