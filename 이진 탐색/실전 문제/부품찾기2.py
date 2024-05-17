n = int(input())
data = list(map(int, input().split()))
d = int(input())
req = list(map(int,input().split()))

data.sort()

def binary_search(target,data,start,end):
    while start <= end:
        mid = (start+end) //2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            mid = end - 1
        else:
            mid = start + 1
    return False

for i in req:
    if binary_search(i,data,0,n-1) == True:
        print("yes", end=' ')
    else:
        print("no",end=' ')
        