import sys

input = sys.stdin.readline


def check(string):
    idx = 0
    s = set()
    while idx < len(string):
        if string[idx] not in s:
            now = string[idx]
            s.add(now)
            while idx < len(string) and now == string[idx]:
                idx += 1
            continue
        else:
            return False
    return True


N = int(input())

answer = 0

for _ in range(N):
    if check(input()):
        answer += 1

print(answer)
