import random

f1 = open("input.txt", "w")
s = int(input("1 - random, 2 - backwards, 3 - algorithm: "))
n = int(input())
a = []
f1.write(str(n) + "\n")
if s == 1:
	for i in range(n):
		f1.write(str(random.randint(1, 10000000)) + " ")
elif s == 2:
	for i in range(n):
		f1.write(str(n - i) + " ")
else:
	for i in range(1, n + 1):
		a.append(i)
	for i in range(2, n):
		a[i], a[i//2] = a[i//2], a[i]
	for x in a:
		f1.write(str(x) + " ")
