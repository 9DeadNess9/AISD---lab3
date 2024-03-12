import time, tracemalloc, random, math

def dist(xy):
	return math.sqrt(xy[0] ** 2 + xy[1] ** 2)

def qSortgood(a):
	if len(a) <= 1:
		return a
	pivotdist = dist(a[random.randint(0, len(a) - 1)])
	l = [x for x in a if dist(x) < pivotdist]
	r = [x for x in a if dist(x) > pivotdist]
	mid = [x for x in a if dist(x) == pivotdist]
	return qSortgood(l) + mid + qSortgood(r)

f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
tracemalloc.start()
t_start = time.perf_counter()
n, out = map(int, f1.readline().split())
a = []
for i in range(n):
	x, y = map(int, f1.readline().split())
	a.append((x, y))
a = qSortgood(a) 
for i in range(out):
	f2.write("[" + str(a[i][0]) + "," + str(a[i][1]) + "]")
	if i != out - 1:
		f2.write(",")
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
