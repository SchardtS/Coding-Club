from SortAlgs import *

# Read the data
with open("2023_12_18_SortingAlgorithms/christmas_gifts.txt", "r") as f:
    lines = f.readlines()

# Split the data into two lists
gift, priority = zip(*[line.strip().rsplit(" ", 1) for line in lines])
gift = list(gift)
priority = list(map(int, priority))

# Test the sorting algorithms
gift1, priority1 = naive_sort(gift[:50], priority[:50])
gift2, priority2 = merge_sort(gift[:50], priority[:50])
gift3, priority3 = count_sort(gift[:50], priority[:50])

print(gift1 == gift2 == gift3, priority1 == priority2 == priority3)

# Time the sorting algorithms for the first 1000 gifts
import timeit
N = 10000
print("Naive sort:", timeit.timeit("naive_sort(gift[:N], priority[:N])", globals=globals(), number=1))
print("Merge sort:", timeit.timeit("merge_sort(gift[:N], priority[:N])", globals=globals(), number=1))
print("Count sort:", timeit.timeit("count_sort(gift[:N], priority[:N])", globals=globals(), number=1))