import time, tracemalloc, random

def qSortgood(a):
	if len(a) <= 1:
		return a
	pivot = a[random.randint(0, len(a) - 1)]
	l = [x for x in a if x > pivot]
	r = [x for x in a if x < pivot]
	mid = [x for x in a if x == pivot]
	return qSortgood(l) + mid + qSortgood(r)

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
citations = list(map(int, f1.readline().split(',')))
a = qSortgood(citations)
h = 0
for i, k in enumerate(a, 1):
	if i <= k:
		h = i
	else:
		break 
f2.write(str(h))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
