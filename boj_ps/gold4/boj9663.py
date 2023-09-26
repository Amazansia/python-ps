import sys

input = sys.stdin.readline

N = int(input())

arr = [-1] * N
answer = 0


def check(x, y):
    for i in range(x):
        if arr[i] == y or abs(arr[i] - y) == abs(i - x):
            return False
    return True


def bt(x):
    global answer
    if x == N:
        answer += 1
        return

    for i in range(N):
        if check(x, i):
            arr[x] = i
            bt(x + 1)
            arr[x] = -1


bt(0)
print(answer)
