import heapq
import sys

"""
사전 순으로 가장 앞에 오는 문자열을 순서대로 출력하기
문자열 앞뒤중간에 다 붙을수도 있다...
visited 만들어서 true인 문자 순서대로 붙여서 출력하기?
문자열 길이 최대 100
아니면 인덱스?
2개기준으로 정렬인듯
A, 2
C, 3
O, 1
Z, 4
같은 문자가 여러 번 나타날 때는 앞에서부터 정렬
안되네
구간에서 젤 작은것부터 체크하기
"""
input = sys.stdin.readline
string = list(input().rstrip())

visited = [False] * len(string)


def recursive(l, r):
    idx = -1
    min_value = 'a'
    # 구간에서 젤 작은거 체크
    for i in range(l, r):
        if not visited[i] and min_value > string[i]:
            min_value = string[i]
            idx = i
    if min_value == 'a' and idx == -1:
        return
    visited[idx] = True

    for i in range(len(string)):
        if visited[i]:
            print(str(string[i]), end='')
    print()

    recursive(idx + 1, r)
    recursive(l, idx)


recursive(0, len(string))
