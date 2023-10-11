import sys

"""
로마 숫자를 N개 사용해서 만들 수 있는 서로 다른 수의 개수
"""
input = sys.stdin.readline

N = int(input())

arr = [1, 5, 10, 50]

answer = set()


# 4개의 수 중 N개를 뽑는 경우의 수... 순서 상관없이
# 항상 정렬되었다고 가정하고

def calculateSum(now, count, order):
    if count == N:
        answer.add(now)
        return

    for i in range(len(arr)):
        if order > i: continue
        calculateSum(now + arr[i], count + 1, i)


calculateSum(0, 0, 0)
print(len(answer))
