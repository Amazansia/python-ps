import sys

"""
다섯알이 연속적으로 놓이면 이긴거
여섯알 이상이 연속적으로 놓이면 아님
검은색이 이겼으면 1, 흰색이 이겼으면 2
승부결정 안났으면 0
결정됐으면 가장 왼쪽의 바둑알 번호출력
가로 세로 주대각선 부대각선 각각 찾아야할듯
찾아서 서로소집합 번호 붙여주면? 아니 굳이...
검은돌 번호는 홀수 / 흰돌 번호는 짝수

"""
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]
visited = [[False for _ in range(19)] for _ in range(19)]

answer = [100, 100, 0]
isOver6 = False


def horizontalSearch(x):
    global answer
    for i in range(19):
        for j in range(19):
            for k in range(6):
                temp = answer
                if not (j + k < 19 and arr[i][j + k] == x and not visited[i][j + k]):
                    break
                if k == 4:
                    answer = min(answer, [i, j, x])
                if k == 5:
                    for t in range(5):
                        visited[i][j + t] = True
                    answer = temp


def verticalSearch(x):
    global answer
    for i in range(19):
        for j in range(19):
            for k in range(6):
                temp = answer
                if not (j + k < 19 and arr[j + k][i] == x and not visited[j + k][i]):
                    break
                if k == 4:
                    answer = min(answer, [i, j, x])
                if k == 5:
                    for t in range(5):
                        visited[j + t][i] = True
                    answer = temp


def main_diagonal(x):
    global answer
    for i in range(19):
        for j in range(19):
            for k in range(6):
                temp = answer
                if not (j + k < 19 and i + k < 19 and arr[i + k][j + k] == x and not visited[i + k][j + k]):
                    break
                if k == 4:
                    answer = min(answer, [i, j, x])
                if k == 5:
                    for t in range(5):
                        visited[i + t][j + t] = True

                    answer = temp


def sub_diagonal(x):
    global answer
    for i in range(19):
        for j in range(19):
            # if i > 0 and arr[i-1][j+1]
            for k in range(6):
                temp = answer
                # i+k i-k
                if not (i + k < 19 and j - k > 0 and arr[i + k][j - k] == x and not visited[i + k][j - k]):
                    break
                if k == 4:
                    answer = min(answer, [i + 4, j - 4, x])
                if k == 5:
                    for t in range(5):
                        visited[i + t][j - t] = True
                    answer = temp


horizontalSearch(1)
visited = [[False for _ in range(19)] for _ in range(19)]
horizontalSearch(2)
visited = [[False for _ in range(19)] for _ in range(19)]

verticalSearch(1)
visited = [[False for _ in range(19)] for _ in range(19)]

verticalSearch(2)
visited = [[False for _ in range(19)] for _ in range(19)]

main_diagonal(1)
visited = [[False for _ in range(19)] for _ in range(19)]

main_diagonal(2)
visited = [[False for _ in range(19)] for _ in range(19)]

sub_diagonal(1)
visited = [[False for _ in range(19)] for _ in range(19)]

sub_diagonal(2)

if answer[0] == 100:
    print(0)
    exit()
print(answer[2])
print(answer[0] + 1, answer[1] + 1)
