import sys

"""
30 50 72
72%30 -> 12

"""
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    x = N % H
    y = N // H + 1
    if x == 0:
        x = H
        y -= 1
    print(x * 100 + y)
