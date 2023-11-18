import sys

input = sys.stdin.readline
"""
부품은 1~10^6까지의 정수로 표현된다
부품 i가 속한 로봇은 robot(i)
서로 다른 로봇은 공통 부품을 가지지 않는다
서로 다른 부품 2개를 말하고, 두 부품은 같은 로봇의 부품이라는 정보를 알려준다.
부품 i에 대해서, 지금까지 알아낸 robot(i)의 부품이 몇 개냐고 물어본다.
지금까지 알아낸 해당 로봇의 부품 개수를 출력한다
N은 최대 10^6
disjoint set?

"""

N = int(input())

for _ in range(N):
    command = input().split(" ")
