import sys
from collections import deque

"""
배추흰지렁이...
배추흰지렁이 한마리당 최대 상하좌우중앙 총 다섯칸의 배추를 보호할 수 있다
그게아니고
나눠진 칸이 몇갠지 보면 되는듯
아하
"""
input = sys.stdin.readline
dxdy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    bat = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        bat[x][y] = 1
    cnt = 0


    def bfs(x, y):

        q = deque()
        visited[x][y] = True
        q.append((x, y))

        while q:
            now = q.popleft()
            visited[now[0]][now[1]] = True

            for d in dxdy:
                dx = now[0] + d[0]
                dy = now[1] + d[1]
                if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and bat[dx][dy] == 1:
                    # visited[dx][dy] = True
                    q.append((dx, dy))


    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    print(cnt)
