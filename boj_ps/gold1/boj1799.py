import sys

"""
비숍은 대각선 방향으로 움직일 수 있다
비숍은 B, 잡을 수 있는 다른 말은 O
서로가 서로를 잡을 수 없는 위치에 놓인 비숍의 최대 개수...
비숍을 놓을 수 있는 곳은 1, 없는 곳은 0
"""
input = sys.stdin.readline

N = int(input())

chess = [list(map(int, input().strip().split())) for _ in range(N)]
answer_white = 0
answer_black = 0

"""
대각선체크 어떻게해욧
x=4, y=3의 대각선체크...
0~N까지 더해주고 나머지연산 돌려주면?
x=2, y=2의 대각선체크
기울기 -1의 대각선체크: 
x-i,y-i
x+i,y+i
기울기 1의 대각선체크:
x-i,y+i
x+i,y-i

"""


# 비숍이 놓여지면 2
# x,y 대각선에 비숍이 있는지 체크하는 함수
def check(x, y):
    for i in range(N):
        if 0 <= x - i < N and 0 <= y - i < N:
            if chess[x - i][y - i] == 2:
                return False
        if 0 <= x + i < N and 0 <= y + i < N:
            if chess[x + i][y + i] == 2:
                return False
        if 0 <= x - i < N and 0 <= y + i < N:
            if chess[x - i][y + i] == 2:
                return False
        if 0 <= x + i < N and 0 <= y - i < N:
            if chess[x + i][y - i] == 2:
                return False
    return True


def bt_white(x, y, now):
    global answer_white
    if y >= N:
        x += 1
        if x % 2 == 0:
            y = 1
        else:
            y = 0
    if x == N:
        answer_white = max(answer_white, now)
        # if now == 7:
        #     for i in range(N):
        #         print(*chess[i])
        return

    if chess[x][y] == 1 and check(x, y):
        # print("check", x, y)
        chess[x][y] = 2
        bt_white(x, y + 2, now + 1)
        chess[x][y] = 1
    bt_white(x, y + 2, now)


def bt_black(x, y, now):
    global answer_black
    if y >= N:
        x += 1
        if x % 2 == 0:
            y = 0
        else:
            y = 1
    if x == N:
        answer_black = max(answer_black, now)
        # if now == 7:
        #     for i in range(N):
        #         print(*chess[i])
        return

    if chess[x][y] == 1 and check(x, y):
        # print("check", x, y)
        chess[x][y] = 2
        bt_black(x, y + 2, now + 1)
        chess[x][y] = 1
    bt_black(x, y + 2, now)


bt_white(0, 1, 0)
bt_black(0, 0, 0)

print(answer_white + answer_black)
# for i in range(N):
#     print(*chess[i])
