import sys
import bisect as bi

"""
이거 파이썬으로 되기는하는거...?
"""
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
INF = int(1e10)
LIS = [INF] * N
ans = [0] * N

for i, x in enumerate(arr):
    idx = bi.bisect_left(LIS, x)
    LIS[idx] = x
    ans[i] = idx

result = []
end = max(ans)

for i in range(N - 1, -1, -1):
    if ans[i] == end:
        result.append(arr[i])
        end -= 1

print(len(result))
print(*result[::-1], sep=' ')
