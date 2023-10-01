import sys

"""
1~G까지의 번호
P개의 비행기가 순서대로 도착하는데
i번째 비행기를 1번부터 Gi번째 게이트중 하나에 영구적으로 도킹
도킹할 수 없다면 스탑
1번부터 Gi번째 게이트...
G=4, P=3, arr=[4,1,1]
1번째 비행기: 4번에 도킹가능
2번째 비행기: 1번에 도킹가능
3번째 비행기: 도킹불가, break

G=4, P=6, arr=[2,2,3,3,4,4]
1 -> 2번에 도킹가능
2 -> 1번에 도킹가능
3 -> 3번에 도킹가능
break

그리디하게 한다면...
g에 도킹가능하다면 도킹
g-1, g-2, g-3...


G 1~100000
P 1~100000
nlogn까지 가능...
이분탐색?
"""
input = sys.stdin.readline

G = int(input())
P = int(input())
arr = list(int(input()) for _ in range(P))

visited = [False] * (G + 1)
last_visited = [i for i in range(G + 1)]

answer = 0


def get_biggest_gate_num(num):
    for i in range(last_visited[num], 0, -1):
        if not visited[i]:
            return i
    return -1


for plane in arr:
    gate_num = get_biggest_gate_num(plane)
    if gate_num != -1:
        visited[gate_num] = True
        last_visited[plane] = gate_num
        answer += 1
    else:
        break

print(answer)
