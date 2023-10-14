"""
R은 1~1 000 000
N -> 100까지, 100*100 -> 10000
백만에 1만...
10 000 000 000
100억
시뮬/bf는 시초임
시계방향으로 4방향 돌릴 수 있으므로 0, 90, 180, 270 총 4가지 방향으로만 결과가 나온다
"""


def solution(matrix, r):
    N = len(matrix)
    answer = [[matrix[i][j] for j in range(N)] for i in range(N)]

    def rotateArr():
        arr = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                arr[j][N - 1 - i] = answer[i][j]
        return arr

    for _ in range(r % 4):
        answer = rotateArr()

    return answer
