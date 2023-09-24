import sys

"""
부메랑을 만들고 싶다
4가지 모양의 부메랑
중심이 되는 칸은 강도 영향을 2배로 받는다
14 5 3 -> 22
18 4 2 -> 24
46
나무는 안써도 됨
n m 둘다 5가 최대
dfs 완탐인듯
"""
input = sys.stdin.readline

N, M = map(int, input().strip().split())

wood = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    wood[i] = list(map(int, input().strip().split()))

# 모양 저장, 중앙 (0, 0) 기준
boomerang = [[-1, 0, 0, -1],
             [-1, 0, 0, 1],
             [0, -1, 1, 0],
             [0, 1, 1, 0]]

visited = [[False for _ in range(M)] for _ in range(N)]

answer = 0


def dfs(crd, s):
    global answer
    if crd == N * M:
        answer = max(answer, s)
        return

    x = crd // M
    y = crd % M

    if not visited[x][y]:
        for i in range(4):
            dx1, dy1, dx2, dy2 = boomerang[i]
            dx1 += x
            dy1 += y
            dx2 += x
            dy2 += y

            if 0 <= dx1 < N and 0 <= dx2 < N and 0 <= dy1 < M and 0 <= dy2 < M and not visited[dx1][dy1] and not \
                    visited[dx2][dy2]:
                visited[dx1][dy1] = visited[dx2][dy2] = visited[x][y] = True
                dfs(crd + 1, s + wood[x][y] * 2 + wood[dx1][dy1] + wood[dx2][dy2])
                visited[dx1][dy1] = visited[dx2][dy2] = visited[x][y] = False
    dfs(crd + 1, s)


dfs(0, 0)
print(answer)
