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

start = 0
end = 0
answer = 0


def isContinuous(q, start):
    for i in range(len(q)):
        if start <= q[i][2] + 1:
            return True
    return False


# 조건을 만족하는 가장 첫번째 일정
def getIdx(q, start):
    for i in range(len(q)):
        if start > q[i][2]:
            return i
    return -1


# q?
while pq:
    now = heapq.heappop(pq)

    start = now[0]
    end = now[2]
    q_max_size = 1
    q = [now]
    # 마지막 end일정 체크
    last_end = end

    # 연속가능
    while pq and isContinuous(q, pq[0][0]):
        next = heapq.heappop(pq)
        # 연속된 일정
        idx = getIdx(q, next[0])
        if idx != -1:
            q[idx][2] = next[2]

        # q에 쌓이는 일정
        else:
            q.append(next)

        last_end = max(last_end, next[2])
        q_max_size = max(q_max_size, len(q))

    answer += (last_end - start + 1) * q_max_size

print(answer)
