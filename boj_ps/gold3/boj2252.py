import sys
from collections import deque

"""
위상정렬 또 너야?!
진입차수 저장해놓고...
큐에서 빼서...어쩌구
"""
input = sys.stdin.readline

N, M = map(int, input().split())

infos = [[] for _ in range(N + 1)]
# 진입차수: i로 들어오는 간선의 개수
indegree = [0] * (N + 1)
for i in range(M):
    A, B = map(int, input().split())
    # A -> B
    infos[A].append(B)
    indegree[B] += 1

q = deque()
result = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in infos[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end=' ')
