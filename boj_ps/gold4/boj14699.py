import sys

input = sys.stdin.readline
"""
각각의 쉼터에서 출발해서 산을 오를 때 최대 몇 개의 쉼터를 방문할 수 있는지 구하여라...

N개의 쉼터, M개의 길
임의의 쉼터에서 등산 시작
더 높은 쉼터로 향하는 길들 중 하나를 골라서 그 길로 이동한다
더 높은 쉼터로 향하는 길이 없다면 등산을 마친다
쉼터 수 N 5000, 길의 수 100000
임의의 두 쉼터를 연결하는 경로가 여러 개 존재할 수 있으나 양 끝점이 같은 쉼터인 길은 없다
"""

N, M = map(int, input().split(" "))

arr = [0] + list(map(int, input().split(" ")))

heights = []

for i in range(1, N + 1):
    heights.append((arr[i], i))

ways = [[] for _ in range(N + 1)]

for i in range(M):
    s, e = map(int, input().split(" "))
    # 2 -> 1 순 정렬
    if arr[s] < arr[e]:
        ways[e].append(s)
    else:
        ways[s].append(e)

dp = [1] * (N + 1)
visited = [False] * (N + 1)

heights.sort(reverse=True)

for i in heights:
    node_num = i[1]
    for way in ways[node_num]:
        dp[way] = max(dp[way], 1 + dp[node_num])
for i in range(1, N + 1):
    print(dp[i])
