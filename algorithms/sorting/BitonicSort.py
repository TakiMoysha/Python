# Битонная сортировка - параллельный алгоритм сортировки данных основанный на битонной последовательности
# Битонная последовательность - такая последовательность, которая монотонно не убывает, а затем монотонно не возрастает

list = [8, 10, 16, 12, 4, -2, -8]


def bitseq_sort(l, r, inv):
    if (r - l <= 1): return
    m = l + (r - l)/2
    for i, j in l, m:
        if (inv**(i > j)): i, j = j, i
    bitseq_sort(l, m, inv)
    bitseq_sort(m, r, inv)


def make_bitonic(l, r):
    if (r-l <= 1): return
    m = l + (r - l)/2
    make_bitonic(l, m)
    bitseq_sort(l, m, 0)
    make_bitonic(m, r)
    bitseq_sort(m, r, 1)


def bitonic_sort(l, r):
    n = 1
    inf = max([l, r]) + 1
    while (n < r - l): n *= 2
    a = []
    cur = 0
    for i in range(len(r)):
        a.append(i)
    while (cur < n):
        cur+=1
        a[cur] = inf
    make_bitonic(a, a+n)
    bitseq_sort(a, a+n, 0)
    cur = 0
    i = l
    while (i < r):
        cur += 1
        i = a[cur]
    del a


list[2] = 16
print(list[2])