# naive sorting algorithm O(n^2)
def naive_sort(values, keys):
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if keys[i] > keys[j]:
                keys[i], keys[j] = keys[j], keys[i]
                values[i], values[j] = values[j], values[i]
    return values, keys

# Merge sort O(n log n)
def merge_sort(values, keys):
    if len(values) <= 1:
        return values, keys

    mid = len(values) // 2
    left_values, left_keys = merge_sort(values[:mid], keys[:mid])
    right_values, right_keys = merge_sort(values[mid:], keys[mid:])

    return merge(left_values, left_keys, right_values, right_keys)

def merge(left_values, left_keys, right_values, right_keys):
    merged_values = []
    merged_keys = []

    while left_values and right_values:
        if left_keys[0] < right_keys[0]:
            merged_values.append(left_values.pop(0))
            merged_keys.append(left_keys.pop(0))
        else:
            merged_values.append(right_values.pop(0))
            merged_keys.append(right_keys.pop(0))

    merged_values += left_values + right_values
    merged_keys += left_keys + right_keys

    return merged_values, merged_keys

# Counting sort O(n + k), k = max(values) ==> O(n) or O(k)
#def count_sort2(values, keys):
#    max_val = max(keys)
#    counts = [0] * (max_val + 1)
#
#    for val in keys:
#        counts[val] += 1
#
#    sorted_keys = []
#    for i in range(len(counts)):
#        sorted_keys += [i] * counts[i]
#
#    return sorted_keys

def count_sort(values, keys):
    max_num = max(keys)
    counts_keys = [[] for _ in range(max_num + 1)]
    counts_values = [[] for _ in range(max_num + 1)]

    for value, key in zip(values, keys):
        counts_keys[key].append(key)
        counts_values[key].append(value)

    sorted_keys = []
    sorted_values = []
    for key, value in zip(counts_keys, counts_values):
        sorted_keys += key
        sorted_values += value

    return sorted_values, sorted_keys