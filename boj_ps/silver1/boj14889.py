import sys

"""
능력치 차이를 최소로...
......
모든 조합을 다 체크하기는 힘들듯
팀에 속하냐/속하지않느냐
최대 20C10 / 2


"""
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 10000000


def calculateStartLink(visited):
    s = 0
    l = 0

    for i in range(N):
        if visited[i]:
            for j in range(N):
                if visited[j]:
                    s += arr[i][j]
        else:
            for j in range(N):
                if not visited[j]:
                    l += arr[i][j]

    return abs(s - l)


# 현재 팀원 번호, 스타트팀 팀원 배열[N]
def recursive(now, start, size):
    global answer
    if size == N // 2:
        answer = min(answer, calculateStartLink(start))
        return
    for i in range(now, N):
        if not start[now]:
            start[now] = True
            recursive(i, start, size + 1)
            start[now] = False


recursive(0, [False] * N, 0)
print(answer)
