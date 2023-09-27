import sys
from collections import deque

"""
모든 지점에 대해 목표지점까지의 최소거리
가로세로로만 움직일 수 있다
목표지점은 2
"""
input = sys.stdin.readline

N, M = map(int, input().split())

dxdy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
goal = [0, 0]
geo = [list(map(int, input().split())) for _ in range(N)]
answer = [[1000001 for _ in range(M)] for _ in range(N)]

for i in range(N):
    if 2 in geo[i]:
        goal = [i, geo[i].index(2)]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    answer[x][y] = 0

    while q:
        i, j = q.popleft()

        for d in dxdy:
            dx = i + d[0]
            dy = j + d[1]
            # dx, dy 범위 내 and 갈수있는길 and 첫도착인지 체크
            if 0 <= dx < N and 0 <= dy < M and geo[dx][dy] == 1 and answer[dx][dy] == 1000001:
                q.append([dx, dy])
                answer[dx][dy] = answer[i][j] + 1


bfs(goal[0], goal[1])

for i in range(N):
    for j in range(M):
        if geo[i][j] == 0:
            answer[i][j] = 0
        if answer[i][j] == 1000001:
            answer[i][j] = -1

for i in range(N):
    print(*answer[i])
