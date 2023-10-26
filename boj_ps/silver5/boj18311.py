import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
rev_arr = list(reversed(arr))

lst = arr + rev_arr

idx = 0
while K >= 0:
    # print(K, idx)
    K -= lst[idx]
    idx += 1

# print(idx)
# 1 2 3 4 5
# 10 9 8 7 6
if idx + 1 >= N:
    idx = (N * 2 + 1) - idx

print(idx)
