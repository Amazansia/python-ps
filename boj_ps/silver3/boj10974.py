import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
arr = [i for i in range(1, N + 1)]

for i in permutations(arr, N):
    print(*i)
