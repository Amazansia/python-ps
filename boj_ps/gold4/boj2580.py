import sys

input = sys.stdin.readline

sudoku = [0 for _ in range(9) for _ in range(9)]

for i in range(9):
    sudoku[i] = list(map(int, input().strip().split()))


def isokay(x, y, now):
    # print("isokay check")
    # print(x, y, now)
    # 가로세로 체크
    for i in range(9):
        if now == sudoku[x][i] or now == sudoku[i][y]:
            return False
    # 네모네모 체크
    dx = x // 3
    dy = y // 3
    for i in range(3):
        for j in range(3):
            if now == sudoku[i + dx * 3][j + dy * 3]:
                return False
    return True


def bt(x, y):
    if y == 9:
        x += 1
        y = 0
    if x > 8:
        for i in range(9):
            print(*sudoku[i])

        # for i in range(9):
        #     for j in range(9):
        #         print(sudoku[i][j], end=' ')
        #     print()
        exit()

    if sudoku[x][y] != 0:
        bt(x, y + 1)
        return

    for i in range(1, 10):
        if isokay(x, y, i):
            # print(x, y, i)
            sudoku[x][y] = i
            bt(x, y + 1)
            sudoku[x][y] = 0


bt(0, 0)
