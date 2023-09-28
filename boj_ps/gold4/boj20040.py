import sys

"""
선플레이어가 홀수차례
후플레이어가 짝수차례
0~N-1까지 고유번호를 가진 평면의 점 N개가 주어지며, 이 중 어느 세 점도 일직선 위에 놓이지 않는다.
이미 그린 다른 선분과 교차는 가능
처음으로 "사이클"이 완성되는 순간 게임 종료
플로이드워셜, 다익스트라, 마지막하나...음수사이클 판정이 가능한...
벨만포드 알고리즘
어느 세 점도 일직선 위에 놓이지 않는다...
점 개수 50만
간선갯수 100만
uf를 이용한 그래프판단
"""
input = sys.stdin.readline

N, M = map(int, input().split())

parents = [i for i in range(N)]

edges = [[] for _ in range(N)]


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


answer = 0


def union(a, b, i):
    global answer
    parentA = find(a)
    parentB = find(b)

    if parentA == parentB:
        answer = i + 1
        return

    if parentA > parentB:
        parents[parentA] = parentB
    else:
        parents[parentB] = parentA


for i in range(M):
    s, e = map(int, input().split())
    if answer == 0:
        union(s, e, i)

print(answer)
