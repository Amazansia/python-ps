"""
1~N까지 번호가 적힌
가장 멀리 떨어진 노드의 갯수는?
다익스트라; start 지점에서부터 모든 다른 정점까지의 최단경로 탐색
"""
import heapq


def solution(n, edge):
    # 0번 노드에서 각 노드까지의 거리
    dis_arr = [100000] * n
    dis_arr[0] = 0

    edges = [[] for _ in range(n)]

    for e in edge:
        edges[e[0] - 1].append((e[1] - 1, 1))
        edges[e[1] - 1].append((e[0] - 1, 1))

    pq = []
    # dis, num 순서로 튜플 만들기
    heapq.heappush(pq, (0, 0))

    while pq:
        dis, now = heapq.heappop(pq)
        if dis_arr[now] < dis:
            continue
        for i in edges[now]:

            if dis + i[1] < dis_arr[i[0]]:
                dis_arr[i[0]] = dis + i[1]
                heapq.heappush(pq, (dis + i[1], i[0]))

    max_dis = max(dis_arr)

    answer = dis_arr.count(max_dis)

    return answer
