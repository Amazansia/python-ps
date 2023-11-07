import sys

"""
모든 가능한 비밀번호의 개수를 출력하라
arr 기준으로 nPm 해서 자리 뽑아놓고
n-m만큼의 수의 개수 출력하면...
겹쳐서 문젠가?
겹치는듯
겹치는거 일일이 빼기에는 좀...
"""
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list()
if M != 0:
    arr = list(map(int, input().split()))


def isOkay(s):
    for i in arr:
        if not str(i) in s:
            return False
    return True


answer = 0


def recursive(now):
    global answer
    if len(now) == N:
        if isOkay(now):
            answer += 1
        return

    for i in range(10):
        recursive(now + str(i))


recursive("")
print(answer)
