import sys

"""
다섯알이 연속적으로 놓이면 이긴거
여섯알 이상이 연속적으로 놓이면 아님
검은색이 이겼으면 1, 흰색이 이겼으면 2
승부결정 안났으면 0
결정됐으면 가장 왼쪽의 바둑알 번호출력
가로 세로 주대각선 부대각선 각각 찾아야할듯
찾아서 서로소집합 번호 붙여주면? 아니 굳이...
앞뒤만 봐주면 될듯
검은돌 번호는 홀수 / 흰돌 번호는 짝수

"""
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]
# j, i, x
answer = [100, 100, 0]


def min(x, y):
    if x[0] > y[0]:
        return y
    if x[0] == y[0] and x[1] > y[1]:
        return y
    return x


def horizontalSearch(x):
    global answer
    for i in range(19):
        for j in range(19):
            # 앞 체크
            if j > 0 and arr[i][j - 1] == x:
                continue
            for k in range(5):
                if j + k >= 19 or arr[i][j + k] != x:
                    break
                if k == 4:
                    # 뒤 체크
                    # 뒷칸이 존재한다면 x가 아니어야 함
                    if (j + 5 < 19 and arr[i][j + 5] != x) or (j + 5 == 19):
                        answer = min(answer, [j, i, x])


def verticalSearch(x):
    global answer
    for i in range(19):
        for j in range(19):
            # 앞 체크
            if i > 0 and arr[i - 1][j] == x:
                continue
            for k in range(5):
                if i + k >= 19 or arr[i + k][j] != x:
                    break
                if k == 4:
                    if (i + 5 < 19 and arr[i + 5][j] != x) or i + 5 == 19:
                        answer = min(answer, [j, i, x])


def main_diagonal(x):
    global answer
    for i in range(19):
        for j in range(19):
            # 앞 체크...하지만 앞이 없을 수도 있다
            if i > 0 and j > 0 and arr[i - 1][j - 1] == x:
                continue
            for k in range(5):
                if j + k >= 19 or i + k >= 19 or arr[i + k][j + k] != x:
                    break
                if k == 4:
                    if (i + 5 < 19 and j + 5 < 19 and arr[i + k + 1][j + k + 1] != x) or (i + 5 == 19 and j + 5 == 19):
                        answer = min(answer, [j, i, x])


def sub_diagonal(x):
    global answer
    for i in range(19):
        for j in range(19):
            # 앞 체크
            if i > 0 and j + 1 < 19 and arr[i - 1][j + 1] == x:
                continue
            for k in range(5):
                if i + k >= 19 or j - k < 0 or arr[i + k][j - k] != x:
                    break
                if k == 4:
                    if (i + 5 < 19 and j - 5 >= 0 and arr[i + 5][j - 5] != x) or i + 5 >= 19 or j - 5 < 0:
                        answer = min(answer, [j - 4, i + 4, x])


horizontalSearch(1)
horizontalSearch(2)
verticalSearch(1)
verticalSearch(2)
main_diagonal(1)
main_diagonal(2)
sub_diagonal(1)
sub_diagonal(2)

if answer[0] == 100:
    print(0)
    exit()
print(answer[2])
print(answer[1] + 1, answer[0] + 1)
