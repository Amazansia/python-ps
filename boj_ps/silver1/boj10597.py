import sys

"""
1부터 N까지의 수로 이루어진 순열...그러니까 1부터 N까지의 수가 모두 하나씩 들어있다
모든 수는 10진수
공백으로 분리되어 있다
자릿수로 대강 알 수 있을듯
1~9 -> 1
10~50 -> 2
자릿수 1부터 9까지는 한자리수로 이루어진 순열
11부터는 maxNum m이라고 하면
len = 9 + (m-9)*2
(l - 9)/2 + 9 = m 
"""
input = sys.stdin.readline

arr = list(input().strip())

N = len(arr)
if len(arr) > 10:
    N = (len(arr) - 9) // 2 + 9


# 한칸 가거나 두칸 가거나...
def recursive(idx, visited, answer):
    # print(*answer)
    if N == len(answer):
        print(*answer)
        exit()
    if idx >= len(arr):
        return
    # if idx >= len(arr):

    # 0으로 시작할 경우 잘못 쌓아온거
    if arr[idx] == "0": return
    # 한자리
    one = int(arr[idx])
    if one <= N and not visited[one]:
        visited[one] = True
        answer.append(one)
        recursive(idx + 1, visited, answer)
        visited[one] = False
        answer.pop()

    # 두자리
    if idx + 1 < len(arr):
        two = int(arr[idx]) * 10 + int(arr[idx + 1])
        if two <= N and not visited[two]:
            visited[two] = True
            answer.append(two)
            recursive(idx + 2, visited, answer)
            visited[two] = False
            answer.pop()


visited = [False] * (N + 1)
visited[0] = True
recursive(0, visited, [])
