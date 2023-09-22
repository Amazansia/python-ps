import sys
from collections import deque

"""
위상정렬인듯
위상정렬 몰?루
w 기준으로 건물번호가 0이 될 때까지 탐색해보기
되나?
노드 1천에 엣지 10만
비용은 int범위 이내
depth 기준으로 생각해야할듯
모든 건물이 건설 가능하도록 주어진다...
depth 1: 
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
1 -> 2,3 -> 4
역순으로 저장한다면
list[4] = [2, 3]
list[3] = [1]
list[2] = [1]
list[1] = []
각 depth에서 max값을 저장하면 될듯...
depth가 진행될 때마다 세워야 하는 조건경로의 수가 늘어남
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
depth 0: 4 -> 3, 2, 1
3 -> 2, 1
2 -> 1
1 -> 2 -> 3 -> 4
100000 -> 99999 -> 99997 -> 99994
1
4 3
5 5 5 5
1 2
2 3
1 3
4
"""
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    order_list = [[] for _ in range(N + 1)]
    num_parent = [0] * (N + 1)
    for _ in range(K):
        s, e = map(int, input().split())
        order_list[s].append(e)
        num_parent[e] += 1
    end = int(input())

    q = deque()

    for i in range(1, N + 1):
        if num_parent[i] == 0:
            q.append(i)
            num_parent[i] -= 1

    init_level = 0
    time_list = [0] * (N + 1)

    for v in q:
        time_list[v] = build_time[v]

    while q:
        now = q.popleft()

        if now == end:
            break

        for nb in order_list[now]:
            time_list[nb] = max(time_list[nb], time_list[now] + build_time[nb])
            num_parent[nb] -= 1
        for i in range(1, N + 1):
            if num_parent[i] == 0:
                q.append(i)
                num_parent[i] -= 1
    print(time_list[end])
