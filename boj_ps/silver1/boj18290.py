import sys

"""
칸 k개를 선택
선택한 칸에 들어있는 수를 모두 더했을 때의 최댓값
선택한 두 칸이 인접(상하좌우)하면 안된다
N, M 최대 10 -> 100
K도 최대 100
"""
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

coordinates = [[0] * 3 for _ in range(N * M)]
idx = 0
for i in range(N):
    for j in range(M):
        coordinates[idx] = [arr[i][j], i, j]
        idx += 1

coordinates.sort(reverse=True)

dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def isOkay(visited, i):
    for ii in range(len(coordinates)):
        if visited[ii]:
            for dd in dxdy:
                dx = coordinates[ii][1] + dd[0]
                dy = coordinates[ii][2] + dd[1]
                if coordinates[i][1] == dx and coordinates[i][2] == dy:
                    return False

    return True


answer = -10000 * 101


def recursive(now, count, total, visited):
    global answer
    if count == K:
        answer = max(answer, total)
        return

    for i in range(now, len(coordinates)):
        if not visited[i] and isOkay(visited, i):
            visited[i] = True
            recursive(i, count + 1, total + coordinates[i][0], visited)
            visited[i] = False


recursive(0, 0, 0, [False] * len(coordinates))
print(answer)
