import sys
from bisect import bisect_right, bisect_left
from itertools import combinations

"""
N개의 정수로 이루어진 수열
크기가 양수(1~N)인 부분수열 중 수열의 합이 S가 되는 경우의 수
부분수열
중간에 뛰어넘는 숫자가 있어도 됨
최대길이 N...40짜리까지 있음
길이 1짜리는 40C1
2짜리는 40C2
길이 3짜리는 40C3...
...40C40까지
비트마스킹 안되고
투포인터 안되고
정렬해서 bt로 돌려야할듯
0 -> N으로 진행하면서 sum보다 커지는 순간 ret
백트래킹 안되는듯...최악을 히트하는 순간 정답이 2^40개로 나와버림
조합 갯수?
이탐이나 투포인터인데
answer: 정답 조합의 개수 
정답조합의 개수를 이탐한다고 생각해보자
그럼 정답 조합이 answer개인지, 작은지, 큰지를 확인해야함
2^N
항복
"""

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
left, right = arr[:N // 2], arr[N // 2:]
leftsum, rightsum = [], []


def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)


def getSum(arr, sumArr):
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumArr.append(sum(a))
    sumArr.sort()


getSum(left, leftsum)
getSum(right, rightsum)
answer = 0
for l in leftsum:
    find = S - l
    answer += getNum(rightsum, find)

answer += getNum(leftsum, S) + getNum(rightsum, S)

print(answer)
