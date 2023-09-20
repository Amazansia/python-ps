"""
독수리타법
해당 문자열을 출력하는 데 걸리는 시간의 최솟값...
자음은 왼손, 모음은 오른손으로 입력
"""
import sys

input = sys.stdin.readline

keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
# 왼손 0, 오른손 1
leftright = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 1, 1]]


def get_coordinate(char):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            if char == keyboard[i][j]:
                return [i, j]


left, right = input().split()
l = get_coordinate(left)
r = get_coordinate(right)
input_str = input()

answer = 0

for idx in range(len(input_str) - 1):
    i = input_str[idx]
    coordinate = get_coordinate(i)
    # print(coordinate)
    if leftright[coordinate[0]][coordinate[1]] == 0:
        answer += abs(coordinate[0] - l[0])
        answer += abs(coordinate[1] - l[1])
        answer += 1
        l = coordinate
    else:
        answer += abs(coordinate[0] - r[0])
        answer += abs(coordinate[1] - r[1])
        answer += 1
        r = coordinate

print(answer)
