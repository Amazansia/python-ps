import sys

"""
N이 주어졌을 때 달팽이 모양으로 N*N에 채우기
N: 홀수인 자연수 3~999
999*999 -> 1000000 : 완탐가능...구현
초기 진행방향 상, 한칸 올라가고 멈춤

"""
input = sys.stdin.readline

N = int(input())
num = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
# 상 하 좌 우
goto = [1, 1, 2, 2]
answer = [0, 0]

i = 1
x = int(N / 2)
y = int(N / 2)

while i <= (N * N):
    # 위
    for p in range(goto[0]):
        arr[x][y] = i
        if i == N * N:
            break
        if i == num:
            answer[0] = x
            answer[1] = y
        i += 1
        x -= 1

    # 오른쪽
    for p in range(goto[1]):
        arr[x][y] = i
        if i == N * N:
            break
        if i == num:
            answer[0] = x
            answer[1] = y
        i += 1
        y += 1

    # 아래
    for p in range(goto[2]):
        arr[x][y] = i
        if i == N * N:
            break
        if i == num:
            answer[0] = x
            answer[1] = y
        i += 1
        x += 1

    # 오른쪽
    for p in range(goto[3]):
        arr[x][y] = i
        if i == N * N:
            break
        if i == num:
            answer[0] = x
            answer[1] = y
        i += 1
        y -= 1

    if i == N * N:
        break

    goto = [i + 2 for i in goto]

for i in arr:
    print(*i)

print(answer[0] + 1, answer[1] + 1)
