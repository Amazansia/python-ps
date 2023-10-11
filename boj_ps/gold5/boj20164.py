import sys

"""
수의 각 자릿수중 >>>홀수의 개수<<<를 저장
수가 한 자리이면 종료
수가 두자리면 2개로 나눠서 합을 구해서 새로운 수로 생각
세자리 이상이면 임의의 위치에서 끊어서 3개로 분할, 더한 값을 새로운 수로 생각
홀수 개수의 최솟값&최댓값을 순서대로 공백으로 구분해서 출력
DFS로 최소&최대 저장해야할듯
"""

input = sys.stdin.readline
N = int(input())
min_value = 99999999
max_value = -1


def recursive(x, now):
    # print(x, now)
    global min_value
    global max_value
    result = 0
    str_x = str(x)

    # 홀수 개수 세기
    for i in str_x:
        if int(i) % 2 == 1:
            result += 1

    # 한 자리
    if len(str_x) == 1:
        min_value = min(min_value, now + result)
        max_value = max(max_value, now + result)
        return

        # 두 자리
    if len(str_x) == 2:
        recursive(int(str_x[0]) + int(str_x[1]), now + result)
        return

    # 3자리 이상
    if len(str_x) >= 3:
        # 3개로 분할하는 방법...
        # i: 0:i로 끊음
        #
        for i in range(1, len(str_x)):
            first = int(str_x[0:i])
            # print(first)
            # j: i:j로 끊음
            for j in range(i, len(str_x)):
                if not str_x[i:j]:
                    continue
                second = int(str_x[i:j])
                # print(second)
                # 마지막: j:-1로 끊기
                if not str_x[j:len(str_x)]:
                    continue
                third = int(str_x[j:len(str_x)])
                # print(first, second, third)
                # print(i, j)
                # 쪼갠 숫자가 모두 유효한 숫자라면
                recursive(first + second + third, now + result)


recursive(N, 0)
print(min_value, max_value)
