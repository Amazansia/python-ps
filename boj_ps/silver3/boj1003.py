import sys

"""
0과 1이 각각 몇 번 출력되는지 구하여라...
dfs로 함수 호출했을 때 0과 1을 구하는 방법
0 -> 0
1 -> 1
2 -> 0, 1
3 -> 2, 1 -> 0, 1, 1
4 -> 3, 2 -> 3 -> 0, 1, 1 & 2 -> 0, 1 -> 2, 3
dp

"""
input = sys.stdin.readline

T = int(input())

# [0의 호출횟수, 1의 호출횟수]
dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]

for i in range(3, 41):
    dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])
