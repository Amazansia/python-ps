import sys
from collections import Counter

"""
파일 확장자별 정리 및 개수세기
확장자 사전순 정리
"""
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    temp = input().strip().split('.')
    arr.append(temp[1])

t = Counter(arr)
cnt = sorted(Counter(arr))
for i in range(len(cnt)):
    print(cnt[i], t[cnt[i]])
