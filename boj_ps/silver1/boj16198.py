import sys

"""
에너지 양의 최댓값 구하기
first&last는 고를 수 없다
x번째 에너지 구슬을 제거하면 x-1 * x+1만큼의 에너지를 모을 수 있다
구슬 번호를 다시 매긴다
"""
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

visited = [False] * N
answer = 0


def getEnergy(idx, visited):
    left = 0
    right = 0
    for i in range(idx - 1, -1, -1):
        if not visited[i]:
            left = i
            break
    for i in range(idx, N):
        if not visited[i]:
            right = i
            break

    # print(left, right)

    return arr[left] * arr[right]


def check(visited):
    for i in range(1, N - 1):
        if not visited[i]:
            return False
    return True


def recursive(sum, visited):
    global answer
    if check(visited):
        answer = max(answer, sum)
        return

    for i in range(1, N - 1):
        if not visited[i]:
            visited[i] = True
            recursive(sum + getEnergy(i, visited), visited)
            visited[i] = False


recursive(0, visited)
print(answer)
