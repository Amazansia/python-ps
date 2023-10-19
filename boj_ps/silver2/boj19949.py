import sys

"""
정답이 될 수 있는 답 조합을 만들어놓고 마지막에 체크?
"""
input = sys.stdin.readline

arr = list(map(int, input().split()))

answer = [0] * 10
total = 0


def check(arr):
    if len(arr) < 3:
        return True
    if arr[-1] != arr[-2] and arr[-2] != arr[-3] and arr[-1] != arr[-3]:
        return True
    return False


def calculate(answer):
    count = 0
    for i in range(10):
        if arr[i] == answer[i]:
            count += 1

    return count


def dfs(idx, answer, count):
    global total
    # n개 문제가 남았는데 5점을 채우지 못하면 바로 return
    if count + 10 - idx < 5:
        return
    if idx == 10:
        if answer[idx - 1] == answer[idx - 2] and answer[idx - 3] == answer[idx - 1]:
            return
        elif count >= 5:
            total += 1
        return

    for i in range(1, 6):
        if idx >= 2 and answer[idx - 1] == answer[idx - 2] and i == answer[idx - 1]:
            continue
        answer[idx] = i
        if arr[idx] == i:
            dfs(idx + 1, answer, count + 1)
        else:
            dfs(idx + 1, answer, count)


dfs(0, answer, 0)
print(total)
