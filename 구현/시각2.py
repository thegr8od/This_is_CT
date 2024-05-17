n = int(input())
cnt = (n+1) * 3600
for i in range(n+1):
    for h in range(60):
        for m in range(60):
            if '3' not in str(i) + str(h) + str(m):
                cnt -= 1 
                
print(cnt)