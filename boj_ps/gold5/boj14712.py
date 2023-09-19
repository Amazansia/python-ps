import sys

"""
2x2 사각형을 이루지 않는 모든 배치의 가짓수
뭔솔...
아하
전체 가짓수에서 빼주면?

2^(N*M) - answer
2x2, 3x3, 4x4...
모두 포함하므로
2x2가 "존재하는" 모든 가짓수를 세주면 될듯
안될듯
맥스값으로 2^625을 계산해야함
dp
이탐 아니고
디피가 맞는데분명
점화식이...
dp[0][i] = 2
dp[i][0] = 2
안될듯
dfs로 풀어보자
0,0/0,1
1,0/1,1
1,1에서 2x2사각형이 존재하지 않는 개수를 answer에 저장하는 dfs함수...

"""
input = sys.stdin.readline

N, M = map(int, input().split())

# booleanArray
arr = [[False] * (M + 1) for _ in range(N + 1)]
cnt = 0


def dfs(depth):
    global cnt
    if depth == N * M:
        cnt += 1
        return

    x = depth // M + 1
    y = depth % M + 1

    if not (arr[x - 1][y] & arr[x][y - 1] & arr[x - 1][y - 1]):
        arr[x][y] = True
        dfs(depth + 1)
        arr[x][y] = False
    dfs(depth + 1)


dfs(0)
print(cnt)
