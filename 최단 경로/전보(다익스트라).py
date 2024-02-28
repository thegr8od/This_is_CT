import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m ,c = map(int, input().split())

graph = [[] for i in range(n+1)]

distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))
    #a에서 b로가는 비용이 c라는 의미


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)


cnt = 0
cnt2 = 0 

for k in range(1, n+1):
    if distance[k] != INF:
        cnt += 1
        cnt2 = max(cnt2, distance[k])


print(cnt -1, cnt2)
