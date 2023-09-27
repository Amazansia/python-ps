import sys
from collections import deque

"""
연결 요소의 개수를 구하는 프로그램...?
연결요소가 뭔데 십덕아
연결요소
부분그래프라네요 아하
"""
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N + 1)

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def bfs(i):
    q = deque()
    visited[i] = True

    q.append(i)
    while q:
        now = q.popleft()
        for edge in edges[now]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)


count = 0

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)
