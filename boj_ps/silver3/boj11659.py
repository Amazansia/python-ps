import sys

"""
1000 * 100000 -> 100 000 000
dp
"""
input = sys.stdin.readline
N, M = map(int, input().strip().split())
arr = [0] + list(map(int, input().strip().split()))
dp = [0] * (N + 1)
dp[0] = arr[0]
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + arr[i]
for _ in range(M):
    s, e = map(int, input().strip().split())
    print(dp[e] - dp[s - 1])
