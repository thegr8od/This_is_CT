n,m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

low = []    
for row in data:
    low.append(min(row))
    
print(max(low))
    