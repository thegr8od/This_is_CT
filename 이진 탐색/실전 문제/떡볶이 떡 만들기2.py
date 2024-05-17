n,m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

def binary_search(start,end):
    target = 0
    while start<=end:
        mid = (start + end) // 2
        cnt = 0
        for i in data:
            if i > mid:
                cnt += (i-mid)
        if cnt == m:
            target = mid
            return target
        elif cnt > m:
            target = mid
            start = mid + 1
        else:
            end = mid - 1     
    return target

print(binary_search(0,max(data)))
                
        