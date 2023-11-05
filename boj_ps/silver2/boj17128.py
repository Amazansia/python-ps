import sys

"""
품질점수...
둘러앉은 소에 대해 연속한 네마리 소들의 품질 점수를 곱한 값을 모두 더한다
Q번에 걸쳐 i번째 소를 선택하고, Ai가 적힌 스티커를 떼어내고, -Ai로 바꾼다.
그럼 Q번에 걸쳐 S를 다시 계산해야 한다...
N은 20만
Q도 20만
...?
"""

input = sys.stdin.readline

N, Q = map(int, input().split())
scores = list(map(int, input().split()))
arrQ = list(map(int, input().split()))

# dp[i]: i부터 연속하는 네 마리 소들의 품질 점수. i=1일 때, A1*A2*A3*A4
dp = [1] * N

for i in range(N):
    for j in range(4):
        idx = i + j
        if idx >= N:
            idx -= N
        dp[i] *= scores[idx]

answer = sum(dp)
# print(answer)
# i일 때, dp[]
for i in arrQ:
    for j in range(4):
        idx = i - 1 - j
        if idx < 0:
            idx += N
        dp[idx] *= -1
        answer += dp[idx] * 2
    print(answer)
