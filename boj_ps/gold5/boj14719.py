import sys

"""
빗물...
dp?
는아니고
left mids right
left와 right보다 mids들이 모두 작아야 성립
min(left, right) - mid 하면 각 칸의 빗물이 나온다
시복 N^3까지 가능
"""
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))


# left가 될 수 있는 기준: 오른쪽 값들이 전부 left보다 작다. 같은 순간 stop
# right의 기준: 왼쪽 값들이 전부 right보다 작다. 혹은 left와 같은 순간 stop

def getMaxRight(idx):
    right = idx + 1

    for i in range(idx + 1, W):
        if i == idx + 1:
            continue
        max_value = max(arr[idx + 1:i])
        if max_value <= arr[idx] and max_value <= arr[i]:
            right = i

    return right


answer = 0
left = 0
right = 0

while left < W:
    right = getMaxRight(left)
    if left == right:
        left += 1
        continue
    elif left < right:
        for i in range(left + 1, right):
            answer += (max(0, min(arr[left], arr[right]) - arr[i]))
        left = right

print(answer)
