import sys

input = sys.stdin.readline
"""
서로 다른 정수 배열이 주어지고, 또 다른 정수 K가 주어졌을 때 
배열의 서로 다른 두 개의 정수의 합이 K에 가장 가까운 두 정수를 구하시오
이렇게 가장 가까운 두 정수의 조합의 수를 계산하는 프로그램
"""
t = int(input())

for _ in range(t):
    n, k = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    arr.sort()

    left = 0
    right = n - 1
    answer_count = 0
    answer_value = arr[left] + arr[right]

    while left < right:
        # 근접값 갱신
        if abs(k - answer_value) > abs(k - (arr[left] + arr[right])):
            answer_value = arr[left] + arr[right]
            answer_count = 1
        # count++
        elif abs(k - answer_value) == abs(k - (arr[left] + arr[right])):
            answer_count += 1

        if k >= arr[left] + arr[right]:
            left += 1
        else:
            right -= 1

    print(answer_count)
