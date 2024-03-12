import time, tracemalloc, random

def qSortgood(a):
	if len(a) <= 1:
		return a
	pivot = a[random.randint(0, len(a) - 1)]
	l = [x for x in a if x < pivot]
	r = [x for x in a if x > pivot]
	mid = [x for x in a if x == pivot]
	return qSortgood(l) + mid + qSortgood(r)

def scarecrow(k):
    if k == 1:
        return "YES"
    for i in range(n):
        c = 0
        j = 0
        while j < len(A[a[i][0]]):
            if abs(i - A[a[i][0]][j]) % k == 0:
                c += 1;
                A[a[i][0]].pop(j)
                
            j += 1;
        if (c == 0):
            return "NO"
    return "YES"

def checkSorted(a, n):
	for i in range(1, n):
		if a[i] < a[i - 1]:
			return False
	return True

tracemalloc.start()
t_start = time.perf_counter()
f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
n, k = map(int, f1.readline().split())
a = list(map(int, f1.readline().split()))
A = dict()
for i in range(n):
    a[i] = [int(a[i]), i]
    A[a[i][0]] = A.get(a[i][0],[])
    A[a[i][0]].append(a[i][1]);
a = qSortgood(a);
print(scarecrow(k))
print("Время работы: ", (time.perf_counter() - t_start))
print(tracemalloc.get_traced_memory())
