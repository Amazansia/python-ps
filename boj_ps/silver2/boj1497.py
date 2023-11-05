import sys
from itertools import combinations

"""
최대한 많은 곡을 연주하려고 할 때 필요한 기타의 최소 개수
최소의 기타로 모든 곡...을
연주 가능한 곡이 없으면 -1
조합으로...
10C1부터 10C10까지
"""
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list()
for i in range(N):
    string = input().split()
    arr.append(string[1])

minValue = 0
answer = -1


def value(now):
    visited = [False] * M
    for string in now:
        for idx in range(M):
            if string[idx] == 'Y':
                visited[idx] = True

    return visited.count(True)


for i in range(1, N + 1):
    for now in combinations(arr, i):
        # print(*now)
        # print(value(now))
        if value(now) > minValue:
            answer = i
            minValue = value(now)

print(answer)
