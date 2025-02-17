# 백준 문제

# 문제 번호: 1260
# 문제 제목: DFS와 BFS
# 난이도(solved.ac 기준): Silver 2
# 시간 제한: 2 초
# 메모리 제한: 128 MB

# v1 - 2025.02.05(시간: 68 ms, 메모리: 34.86 MB)
from sys import stdin
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    print(v, end=' ')

    while queue:
        node = queue.popleft()

        for i in sorted(graph[node]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                print(i, end=' ')  

n, m, v = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)