import heapq
import sys

"""
일정 갯수/각 일정의 시작날짜, 종료날짜가 주어질 때 수현이가 자르는 코팅지의 면적을 구하시오
연속된 일자에 일정이 하나 이상 있다면 일정이 연속되었다고 한다
연속된 일정은 하나의 직사각형에 포함되어야 한다
연속된 일정에 딱 맞게 코팅지를 오린다
연속일정...
정렬하고

"""
input = sys.stdin.readline

N = int(input())
pq = []

for i in range(N):
    s, e = map(int, input().split())
    # 시작날짜, 일정기간, 마지막날
    heapq.heappush(pq, [s, e - s + 1, e])

idx = 0
start = 0
end = 0
answer = 0

# q?
while pq:
    now = heapq.heappop(pq)

    start = now[0]
    end = now[1]
    q_max_size = 0
    q = []
    # 마지막 end일정 체크
    last_end = end
    # 연속으로 이어지는 일정이 있는 경우
    # next[0] == end + 1 or next[0] <= last_end
    #
    # end + 1 == next[0],
    while pq and pq[0][0] == end + 1 or pq[0][0] <= last_end:
        next = heapq.heappop(pq)
        # 연속된 일정
        if pq[0][0] == end + 1:

        elif pq[0][0] <= last_end:

        last_end = next[1]

    answer += (last_end - start + 1) * q_max_size

print(answer)
