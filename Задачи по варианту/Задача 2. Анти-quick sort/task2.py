import time, tracemalloc, sys

def qsort (left, right):
	key = a [(left + right) // 2]
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
		qsort(left, j)
	if i < right:
		qsort(i, right)

sys.setrecursionlimit(5000)
tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f1.readline())
a = list(map(int, f1.readline().split()))
qsort(0, n-1)
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
