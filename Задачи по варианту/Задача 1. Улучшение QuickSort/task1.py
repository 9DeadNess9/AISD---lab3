import time, tracemalloc, random

def qSortgood(a):
	if len(a) <= 1:
		return a
	pivot = a[random.randint(0, len(a) - 1)]
	l = [x for x in a if x < pivot]
	r = [x for x in a if x > pivot]
	mid = [x for x in a if x == pivot]
	return qSortgood(l) + mid + qSortgood(r)

def qSortbad(left, right):
	key = a[random.randint(0, len(a) - 1)]
	i = left
	j = right
	while i <= j:
		while a[i] < key: # first while
			i += 1
		while a[j] > key : # second while
			j -= 1
		if i <= j :
			a[i], a[j] = a[j], a[i]
			i += 1
			j -= 1

	if left < j:
		qSortbad(left, j)
	if i < right:
		qSortbad(i, right)

f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = list(map(int, f1.readline().split()))
tracemalloc.start()
s = input("Which?: ")
if s == "bad":
	t_start = time.perf_counter()
	a = qSortbad(0, n - 1)
elif s == "good":
	t_start = time.perf_counter()
	a = qSortgood(a)
else:
	print("idk which sort")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
for x in a:
	f2.write(str(x) + " ")
