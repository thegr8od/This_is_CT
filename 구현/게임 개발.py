n,m = map(int, input().split())
a,b,d = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [0,1,0,-1]
dy = [-1,0,1,0]

if m != 0:
    angle = 4-m
else:
    angle = 0

visited = [[False]*m for _ in range(n)]
cnt = 0

def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
       dirr = angle+i
       if dirr > 3:
           dirr = (dirr) % 4
       nx = x + dx[dirr]
       ny = y + dy[dirr]
       if 0<=nx<n and 0<=ny<n:
           if visited[nx][ny] == False and graph[nx][ny] == 0:
               dfs(nx,ny)
               return
    
    return

dfs(a,b)

print(cnt)        