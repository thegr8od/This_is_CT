def binary_search(data,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    return False        

n = int(input())
data = list(map(int, input().split()))

m = int(input())
data2 = list(map(int,input().split()))

for i in data2:
    if binary_search(data,i,0,n-1) == True:
        print("yes",end = ' ')
    else:
        print("no", end=' ')
        