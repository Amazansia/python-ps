import sys

"""
500에서 스타트, 하루 지날 때마다 K만큼 감소
하루에 1개씩 키트를 사용해서 중량을 증가시킬 수 있음
N일동안 한 번씩만 사용 가능
1~N일차까지 모든 기간동안 중량이 500보다 작아지면 안됨
"""
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


def recursive(day, now, visited):
    global answer
    if now < 500:
        return
    if day == N:
        answer += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recursive(day + 1, now - K + arr[i], visited)
            visited[i] = False


recursive(0, 500, [False] * N)
print(answer)
