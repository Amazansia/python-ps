import math
import sys

input = sys.stdin.readline

"""
a 이상 b 이하의 팰린드롬이면서 소수인 수 모두 구하기
증가순
최대 8자리의 팰린드롬 수 모두 구하기
a의 자릿수부터 b의 자릿수까지 모두 구하고 ab 사이에 있는지 체크하고 출력하면 될듯
n자릿수의 팰린드롬이면서 소수인 수:
모든 팰린드롬 다 구하기
if n%2==0
n//2
"""
a, b = map(int, input().split())

answer = set()


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def calculateNum(digit, now, num):
    # print(num)
    if now == digit // 2 + 1:
        num_int = int("".join(map(str, num)))
        if isPrime(num_int):
            answer.add(num_int)
        return

    for i in range(0, 10):
        if now == 0 and i == 0:
            continue
        num[now] = i
        num[digit - now - 1] = i
        calculateNum(digit, now + 1, num)
        num[now] = 0
        num[digit - now - 1] = 0


for digit in range(len(str(a)), len(str(b)) + 1):
    # 1, 2, 3
    calculateNum(digit, 0, [0] * digit)

answer = list(answer)
answer.sort()
for i in answer:
    if i in range(a, b + 1):
        print(i)
print(-1)
