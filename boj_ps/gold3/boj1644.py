import math
import sys

"""
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들...
"연속된"
그렇게 나타낼 수 있는 경우의 수를 구하여라.
소수들 400만까지 구해놓고? 투포인터로 경우의 수를 구하면...
"소수의 합"
2 3 5 7 11 13 17 19 23 29 31 37 ...
N은 400만까지 들어옴
맞는듯
"""
input = sys.stdin.readline

N = int(input())

arr = [True for _ in range(N + 1)]
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(N + 1) + 1)):
    if arr[i]:
        for j in range(i + i, N + 1, i):
            arr[j] = False

primenums = [i for i in range(1, N + 1) if arr[i]]

left = 0
right = 0

answer = 0
s = 2
# print(*primenums)
while left <= right < len(primenums):
    if s == N:
        s -= primenums[left]
        left += 1
        answer += 1
    elif s > N:
        s -= primenums[left]
        left += 1
    else:
        right += 1
        if right >= len(primenums):
            break
        s += primenums[right]

print(answer)
