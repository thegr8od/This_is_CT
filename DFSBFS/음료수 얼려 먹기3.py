graph = []

n,m = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dfs(nx,ny)       
    return True
        
cnt = 0
for i in range(n):
    for j in range(m):
            if graph[i][j] == 0:
                if dfs(i,j) == True:
                    cnt += 1
print(cnt)

    
                 