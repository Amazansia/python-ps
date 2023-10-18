import sys

"""
cctv는 감시할 수 있는 방향에 있는 칸 전체를 감시 가능하다
벽은 통과 불가능
cctv는 회전 가능
사각지대의 최소크기는?
1 - 4회전
2 - 2회전
3 - 4회전
4 - 4회전
5 - 회전x
"""
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

answer = N * M + 1

rotation = [0, 4, 2, 4, 4, 1]

# cctv_x, cctv_y, cctv_model, rotation_num
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctvs.append([i, j, arr[i][j], 0])


def getBlindSpots(arr, cctv):
    visited = [[False] * M for _ in range(N)]

    def right(x, y):
        for i in range(y, M):

            visited[x][i] = True
            if arr[x][i] == 6:
                break

    def down(x, y):
        for i in range(x, N):

            visited[i][y] = True
            if arr[i][y] == 6:
                break

    def left(x, y):
        for i in range(y, -1, -1):
            visited[x][i] = True
            if arr[x][i] == 6:
                break

    def up(x, y):
        for i in range(x, -1, -1):

            visited[i][y] = True
            if arr[i][y] == 6:
                break

    for tv in cctv:
        if tv[2] == 1:
            if tv[3] == 0:
                right(tv[0], tv[1])
            elif tv[3] == 1:
                down(tv[0], tv[1])
            elif tv[3] == 2:
                left(tv[0], tv[1])
            else:
                up(tv[0], tv[1])
        elif tv[2] == 2:
            if tv[3] == 0:
                left(tv[0], tv[1])
                right(tv[0], tv[1])
            else:
                up(tv[0], tv[1])
                down(tv[0], tv[1])
        elif tv[2] == 3:
            if tv[3] == 0:
                up(tv[0], tv[1])
                right(tv[0], tv[1])
            elif tv[3] == 1:
                right(tv[0], tv[1])
                down(tv[0], tv[1])
            elif tv[3] == 2:
                down(tv[0], tv[1])
                left(tv[0], tv[1])
            else:
                left(tv[0], tv[1])
                up(tv[0], tv[1])
        elif tv[2] == 4:
            if tv[3] == 0:
                left(tv[0], tv[1])
                up(tv[0], tv[1])
                right(tv[0], tv[1])
            elif tv[3] == 1:
                right(tv[0], tv[1])
                up(tv[0], tv[1])
                down(tv[0], tv[1])
            elif tv[3] == 2:
                down(tv[0], tv[1])
                left(tv[0], tv[1])
                right(tv[0], tv[1])
            else:
                left(tv[0], tv[1])
                up(tv[0], tv[1])
                down(tv[0], tv[1])
        else:
            left(tv[0], tv[1])
            right(tv[0], tv[1])
            up(tv[0], tv[1])
            down(tv[0], tv[1])

    answer = 0
    for i in range(N):
        for j in range(M):
            if (visited[i][j] and arr[i][j] == 0) or arr[i][j] != 0:
                answer += 1

    # if answer != 33:
    #     print(*cctv)
    #     for i in range(N):
    #         print(*visited[i])

    return N * M - answer


# 현재 cctv idx, cctv 정보
def dfs(cctv_idx, cctv):
    global answer
    if cctv_idx == len(cctvs):
        answer = min(answer, getBlindSpots(arr, cctv))
        return
    if cctv[cctv_idx][3] == rotation[cctv[cctv_idx][2]]:
        cctv[cctv_idx][3] = 0
        dfs(cctv_idx + 1, cctv)
        return

    # cctv_idx의 형태에 따라 다른 회전횟수로 dfs문 실행
    dfs(cctv_idx + 1, cctv)
    cctv[cctv_idx][3] += 1
    dfs(cctv_idx, cctv)


dfs(0, cctvs)
print(answer)
