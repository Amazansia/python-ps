import sys

input = sys.stdin.readline

"""
11명의 선수를 각 포지션에 배치
능력치가 0인 포지션에 배치될 수 없다
모든 포지션의 선수를 채웠을 때 능력치의 합의 최댓값을 출력
최대 5^11?
"""

C = int(input())


def dfs(mat, pos, cnt, s):
    global answer
    if cnt == 11:
        answer = max(answer, s)
        return

    for i in range(len(mat[cnt])):
        # 능력이 없음
        if mat[cnt][i] == 0: continue
        # 이미 배치된 포지션
        if pos[i] != -1: continue
        pos[i] = cnt
        dfs(mat, pos, cnt + 1, s + mat[cnt][i])
        pos[i] = -1


for tc in range(C):
    arr = [[0 for _ in range(11)] for _ in range(11)]
    for i in range(11):
        arr[i] = list(map(int, input().split()))

    answer = 0
    # 포지션 저장: position[i] = j -> i번째 포지션에는 j번째 선수가 배치됨
    position = [-1 for _ in range(11)]
    dfs(arr, position, 0, 0)
    print(answer)
