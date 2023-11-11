import sys

"""
유성이 떨어진 후의 사진을 복구하기
x:유성의 일부
#:땅의 일부
.:공기
모든 유성 조각은 연결되어 있따
땅 또한 연결되어 있다

"""
input = sys.stdin.readline

R, S = map(int, input().split())

pic = ["" for _ in range(R)]

for i in range(R):
    pic[i] = input()


def getAirHeight(j):
    ground = 0
    meteor = 0
    for i in range(R):
        if pic[i][j] == 'X':
            meteor = i + 1
        if pic[i][j] == '#':
            ground = i
            break
    if meteor != 0 and ground != 0:
        return ground - meteor
    else:
        return 3000


def getMaxMove():
    move = 3000
    for i in range(S):
        move = min(move, getAirHeight(i))
    return move


def printModifiedPic():
    move = getMaxMove()
    newPic = [['.' for _ in range(S)] for _ in range(R)]
    for i in range(R):
        for j in range(S):
            if pic[i][j] == 'X':
                newPic[i + move][j] = 'X'
            elif pic[i][j] == '#':
                newPic[i][j] = '#'

    for i in range(R):
        print("".join(newPic[i]))


printModifiedPic()
