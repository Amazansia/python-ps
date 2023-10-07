import sys

input = sys.stdin.readline


def check_win(x, y, color):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in directions:
        count = 1  # 현재 위치를 포함하므로 1로 초기화

        # 앞쪽 방향 검사
        i, j = x - dx, y - dy
        while i >= 0 and j >= 0 and arr[i][j] == color:
            count += 1
            i -= dx
            j -= dy

        # 뒤쪽 방향 검사
        i, j = x + dx, y + dy
        while i < 19 and j < 19 and arr[i][j] == color:
            count += 1
            i += dx
            j += dy

        # 승부 판정
        if count >= 5:
            return color

    return 0


arr = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            result = check_win(i, j, arr[i][j])
            if result != 0:
                print(result)
                print(i + 1, j + 1)
                exit()

print(0)
