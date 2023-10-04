import sys

"""
123으로만 이뤄지는 수열
임의의 길이의 인접한 두 개의 부분 수열이 동일하면 나쁜 수열
길이가 N인 좋은 수열 중 가장 작은 수를 나타내는 수열....
N은 80까지
그리디?에 백트래킹일듯
"""
input = sys.stdin.readline

N = int(input())
answer = []


# 마지막에 next를 붙였을 때 나쁜 수열이 되는가를 판별
def check(arr, next):
    if len(arr) == 0:
        return True

    narr = [arr[i] for i in range(len(arr))]
    narr.append(next)
    narr.reverse()

    # 사이즈 i
    for i in range(1, len(narr)):
        if i + i > len(narr): break
        if narr[0:i] == narr[i:i + i]:
            return False

    return True


def bt(now, arr):
    if now == N:
        print("".join(map(str, arr)))
        exit()
    for i in range(1, 4):

        if check(arr, i):
            bt(now + 1, arr + [i])


bt(0, [])
