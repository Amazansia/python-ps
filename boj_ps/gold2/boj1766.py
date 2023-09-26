import heapq
import sys
from collections import deque

"""
N개의 문제로 되어 있는 문제집
난이도순 출제
1번이 제일 쉽고 N번이 제일 어려움
N개 모두 풀어야함
먼저푸는게 좋은 문제가 있으면 반드시 그걸 먼저 풀어야함
가능하면 쉬운 문제부터
문제갯수 10만개
문제수 3.2만...
유니온파인드
아니면 pq
pq에 pq를 넣을수가잇나
안될듯 pq에 pq에 pq........를 넣어야할지도
유파인듯
list로 받고
유파 싹 돌려
그리고 그거 정렬해서 출력
위상정렬아녀?
"""
input = sys.stdin.readline

N, M = map(int, input().split())
# good[i]: i번 문제보다 먼저 푸는 게 좋은 문제들 리스트
good = [[] for _ in range(N + 1)]
degree = [0 for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # A번 문제는 B번 문제보다 먼저 푸는 것이 좋다
    good[a].append(b)
    degree[b] += 1


def ts():
    res = []
    pq = []
    # 진입차수가 0인 정점을 최소 힙에 삽입
    for i in range(1, N + 1):
        if degree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        now = heapq.heappop(pq)
        res.append(now)
        for i in good[now]:
            degree[i] -= 1
            if degree[i] == 0:
                heapq.heappush(pq, i)

    for i in res:
        print(i, end=' ')


ts()
