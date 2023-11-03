import sys
import math
from itertools import combinations

input = sys.stdin.readline
"""
몸무게 합이 소수가 되도록

"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = set()


def isPrime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for i in combinations(arr, M):
    if isPrime(sum(i)):
        answer.add(sum(i))
answer = list(answer)
answer.sort()
if answer:
    print(*answer)
else:
    print(-1)
