def sort(arr):
    if len(arr) <= 1:
        return arr
    median = arr[len(arr) // 2]
    left = [x for x in arr if x < median]
    middle = [x for x in arr if x == median]
    right = [x for x in arr if x > median]
    return sort(left) + middle + sort(right)

print(sort([61,2,5,12,6,1]))
# 1 2 5 6 12 61
