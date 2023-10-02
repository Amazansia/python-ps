"""
거쳐간 숫자의 합이 가장 큰 경우
오른쪽 또는 왼쪽으로만 이동가능
높이는 최대 500
걍 완탐해도될거같은데
1 보면
left = dp[i-1][j-1] + triangle[i][j]
"""


def solution(triangle):
    answer = 0

    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j > 0:
                from_left_parent = dp[i - 1][j - 1] + triangle[i][j]
            else:
                from_left_parent = 0
            if j == len(triangle[i]) - 1:
                from_right_parent = 0
            else:
                from_right_parent = dp[i - 1][j] + triangle[i][j]
            dp[i][j] = max(from_left_parent, from_right_parent)

    i = len(triangle) - 1
    for j in range(len(triangle[i])):
        answer = max(answer, dp[i][j])

    return answer
