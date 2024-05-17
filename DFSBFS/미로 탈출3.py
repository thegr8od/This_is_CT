from collections import deque

n,m = map(int, input().split())

graph = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]



for i in range(n):
    graph.append(list(map(int, input())))
    

def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[n-1][m-1]
    
print(bfs(0,0))