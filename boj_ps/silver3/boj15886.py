import sys

"""
E칸 -> 한칸 오른쪽 ->
W칸 -> 한칸 왼쪽 <-
이동을 시작하는 위치와 관계없이 선물을 주고 싶다.
최소 몇 개의 칸 위에 선물을 놓으면 항상 선물을 가져가는가?
E를 기준으로 생각해보자
EEWWEW -> > > < < > <
><이 몇개 나오는가?
"""

input = sys.stdin.readline

N = int(input())
geo = input()

answer = 0

for i in range(N - 1):
    if geo[i] == 'E' and geo[i + 1] == 'W':
        answer += 1

print(answer)
