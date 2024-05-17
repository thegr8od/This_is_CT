row = ['a','b','c','d','e','f','g','h']
col =[1,2,3,4,5,6,7,8]

cmd = list(input())
x = row.index(cmd[0])
y = col.index(int(cmd[1]))

dx = [-2,-2,-1,1,2,2,-1,1]
dy = [-1,1,2,2,1,-1,-2,-2]

ans = 0

for i in range(8):
    nx = x+ dx[i]
    ny = y+ dy[i]
    if 0<= nx < 8 and 0<= ny< 8:
        ans += 1
        
print(ans)