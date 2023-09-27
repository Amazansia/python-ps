import sys

"""
카드 N개
셔플 D번
그럼 원래 카드는 어떻게 되어 있었는지?
N 10000
K 1000
각 수는 100000를 넘지 않는다 
Di번째 카드를 i번째로 가져오는
4 3 1 2 5
D1번째 카드를 1번째로 가져오는
4번째 카드를 1번째로 가져오는
3번째 카드를 2번째로 가져오는
1번째 카드를 3번째로 가져오는
2번째 카드를 4번째로 가져오는
5번째 카드를 5번째로 가져오는

result[i] = original[suffle[i]]
1번째 카드 = original[4 - 1]
2번째 카드 = original[3 - 1]
result[i - 1] == original[suffle_arr[i] - 1]
그럼 original[i]는


되돌리려면 
1번째를 4번째로
2번째를 3번째로
3번째를 1번째로
뒤에서부터 해야함
...
ㅇㅋ

"""
input = sys.stdin.readline
N, K = map(int, input().split())

result_arr = list(map(int, input().split()))
suffle_arr = list(map(int, input().split()))

for _ in range(K):
    t = [0] * N
    for i in range(N):
        t[suffle_arr[i] - 1] = result_arr[i]
    result_arr = t
print(*result_arr)
