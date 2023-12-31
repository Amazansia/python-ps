import sys

input = sys.stdin.readline

N = int(input())
MOD = 10007
dp = [[0 for _ in range(10)] for _ in range(N + 1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

answer = 0
for i in range(10):
    answer = (answer + dp[N][i]) % MOD

print(answer)
