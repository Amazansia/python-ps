import sys

"""
배열을 반시계 방향으로 돌려보자...
ㅎ

"""
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


def rotateArr():
    # start와 end, 좌상과 우하를 구하면 대충 어디부터 어디까지 돌아가는지 알 수 있음
    start = [0, 0]
    end = [N - 1, M - 1]
    # 더 돌릴 수 없으면 stop
    while start[0] < end[0] and start[1] < end[1]:
        # up
        start_to_end = arr[start[0]][start[1]:end[1] + 1]
        # print(*start_to_end)
        # right
        for i in range(start[0] + 1, end[0] + 1):
            start_to_end.append(arr[i][end[1]])
        # print(*start_to_end)
        # down(역)
        for i in range(end[1] - 1, start[1] - 1, -1):
            start_to_end.append(arr[end[0]][i])
        # print(*start_to_end)
        # left(역)
        for i in range(end[0] - 1, start[0], -1):
            start_to_end.append(arr[i][start[1]])
        # print(*start_to_end)

        idx = 1

        for i in range(start[1], end[1] + 1):
            arr[start[0]][i] = start_to_end[idx]
            idx += 1
        # for i in range(N):
        #     print(arr[i], sep=' ')
        # print()

        for i in range(start[0] + 1, end[0] + 1):
            if not 0 <= i < N: break
            arr[i][end[1]] = start_to_end[idx]
            idx += 1
        # for i in range(N):
        #     print(arr[i], sep=' ')
        # print(idx)

        for i in range(end[1] - 1, start[1] - 1, -1):
            if not 0 <= i < M or idx >= len(start_to_end): break
            arr[end[0]][i] = start_to_end[idx]
            idx += 1
        # for i in range(N):
        #     print(arr[i], sep=' ')
        # print()

        for i in range(end[0] - 1, start[0] + 1, -1):
            arr[i][start[1]] = start_to_end[idx]
            idx += 1
        # for i in range(N):
        #     print(arr[i], sep=' ')
        # print()

        arr[start[0] + 1][start[1]] = start_to_end[0]
        start = [start[0] + 1, start[1] + 1]
        end = [end[0] - 1, end[1] - 1]


for _ in range(R):
    rotateArr()
for i in range(N):
    print(*arr[i])
