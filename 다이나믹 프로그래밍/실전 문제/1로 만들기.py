d = [0] * 30001

d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 1

n = int(input())
for i in range(6,n+1):
    if i % 5 == 0:
        d[i] = min(d[i//5] + 1,d[i-1] + 1)
    if i % 3 == 0:
        d[i] = min(d[i//3] + 1, d[i-1] + 1)
    if i % 2 == 0:
        d[i] = min(d[i//2] + 1,d[i-1] + 1)
    else:
        d[i] = d[i-1] + 1

print(d)
print(d[n])