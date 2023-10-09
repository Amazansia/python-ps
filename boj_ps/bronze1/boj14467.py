import sys

"""
같은 번호의 소가 위치를 바꾼 것이 몇 번인가?
-1 : 초기값, 관찰x
"""
input = sys.stdin.readline
N = int(input())

arr = [-1] * (N + 1)
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    if arr[a] != -1 and arr[a] != b:
        answer += 1
    arr[a] = b

print(answer)
