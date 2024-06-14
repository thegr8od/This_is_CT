n,m = map(int,input().split())
data = list(map(int, input().split()))

def binary_search(start,end):
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in data:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result
            
print(binary_search(0,max(data)))