import math
import sys
from itertools import combinations

"""
왼쪽에서부터 자리수가?감소?할?때?
왼쪽에서부터 자리수가 감소
왼쪽에서부터...

줄어드는 수...?
N번째로 작은 줄어드는 수를 출력하는 프로그램
가장 작은 줄어드는 수가 1번째...
뭔소리
19번째로 작은 줄어드는 수가 42
50만번째로 작은 줄어드는 수 -> 없음?왜?
0 1 2 3 4 5 6 7 8 9 -> 10
10 20 21 30 31 32 40 41 42...

210
3210
43210...
가장 작은 줄어드는 수가 1번째 작은 줄어드는 수
1백만까지 N으로 돌면 가능
NlogN까지 ㄱㅊ
십진법...
98765 43210 까지가 최대수
흠
dp[i][j]: 자릿수 i면서 j로 시작하는 D.num의 개수
7자릿수, 8로 시작하는 d.num
0부터 j-1의 수 중 6개를 뽑는 경우의 수와 동일
j개의 수 중 i-1개를 뽑는 경우의 수
jCi-1
작은 순으로 정렬하므로
dp까지도 필요없을듯
그냥 for를 i: 1~10, j:0~9까지 돌리면서 조합 개수를 더해보고
N보다 작으면 continue, N과 같을 경우 return, N보다 클 경우 stop
[0] ~ [9]의 수 중 자릿수만큼의 개수를 뽑는 경우의 수
앞자리가 0일 때를 제외하고

"""
input = sys.stdin.readline

N = int(input())

idx = 0

# 한자릿수 수들 9 ~ 0
base = [str(num) for num in range(9, -1, -1)]

# 자릿수마다 돌리기: 2~10
for i in range(1, 11, 1):
    lst = sorted(list(combinations(base, i)))
    for now in lst:
        idx += 1
        if N == idx:
            print("".join(now))
            exit()

print(-1)
