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

# 부모노드 저장
parent = [i for i in range(1000000)]
# 부모노드 기준으로 정답 저장
answer = dict()


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a <= parent_b:
        parent[b] = parent_a
    else:
        parent[a] = parent_b


def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a


def queryArr(a):
    sum = 0
    for i in range
    return


for _ in range(N):
    command = input().split(" ")
    if command[0] == "I":
        union(int(command[1]), int(command[2]))
    else:
        print(queryArr(int(command[1])))
