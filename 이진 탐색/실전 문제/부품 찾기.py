def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
data2 = list(map(int, input().split()))

for i in data2:
    target = i
    result = binary_search(data, target, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
