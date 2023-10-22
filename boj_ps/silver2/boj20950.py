import sys

"""
N개의 물감과 곰두리색이 주어졌을 때 곰두리색과 문두리색의 차이를 구하시오
7개의 물감까지만 혼합 가능하고, 단독으로 사용할 수 없다.
새로운 R값은 모든 R값의 평균
"""

input = sys.stdin.readline

arr = []

N = int(input())
for i in range(N):
    arr.append(list(map(int, input().split())))
goal = list(map(int, input().split()))

min_value = 1000000000


def mixing(idx, total, visited):
    global min_value
    if total > 7:
        return
    # now = arr[idx]
    # min_value = min(min_value, abs(now[0] - goal[0]) + abs(now[1] - goal[1]) + abs(now[2] - goal[2]))
    if total >= 2:
        # 모든 순회에서 min_value 갱신
        total_R = 0
        total_G = 0
        total_B = 0
        for i in range(N):
            if visited[i]:
                total_R += arr[i][0]
                total_G += arr[i][1]
                total_B += arr[i][2]
        R = total_R // total
        G = total_G // total
        B = total_B // total
        min_value = min(min_value, abs(R - goal[0]) + abs(G - goal[1]) + abs(B - goal[2]))
        # print(R, G, B, total)
        # print(*visited)
        # print(min_value)
    if idx == N:
        return
        # 이번 idx의 물감을 섞지 않고 다음 재귀로 넘어감
    mixing(idx + 1, total, visited)
    # 이번 idx의 물감을 섞음
    visited[idx] = True
    mixing(idx + 1, total + 1, visited)
    visited[idx] = False


mixing(0, 0, [False for _ in range(N)])
print(min_value)
