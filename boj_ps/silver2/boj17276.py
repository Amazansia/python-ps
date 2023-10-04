import sys

"""
45도 연산 최대 7번 적용...
괜찮지않을까?
45도연산 함수 만들어놓고 여러번 적용시키면 될듯
걍 구현
주대각선=좌상->우하로 가는 대각선
부대각선=우상->좌하로 가는 대각선

"""
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    if D < 0:
        D += 360


    def rotateArr():
        main_diagonal = [arr[i][i] for i in range(N)]
        sub_diagonal = [arr[i][N - 1 - i] for i in range(N)]
        sub_diagonal.reverse()
        horizontal = [arr[N // 2][i] for i in range(N)]
        vertical = [arr[i][N // 2] for i in range(N)]

        for i in range(N):
            # 주대각선을 중앙열로
            arr[i][N // 2] = main_diagonal[i]
            # 가운데열을 부대각선으로
            arr[i][N - 1 - i] = vertical[i]
            # 부대각선을 가운데행으로
            arr[N // 2][i] = sub_diagonal[i]
            # 중앙행을 주대각선으로
            arr[i][i] = horizontal[i]


    for _ in range((D // 45) % 8):
        rotateArr()

    for i in range(N):
        print(*arr[i])
