n, m, k = map(int, input().split())

lst = []
lst = list(map(int, input().split()))

lst.sort(reverse=True)

sum = 0 

while True:
    for i in range(k):
        if m == 0:
            break
        sum += lst[0]
        m -= 1
    if m == 0:
        break
    sum += lst[1]
    m -=1



print(sum)



