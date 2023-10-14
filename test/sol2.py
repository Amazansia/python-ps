"""
특정 초의 비밀번호를 알고 싶다.
새로운 비밀번호 = (a*이전비밀번호 + b) mod 10000
비밀번호는 k초마다 새로운 비밀번호로 바뀐다
k는 100까지
a, b 10000까지
times는 10000까지
times는 오름차순으로 정리되어 있다
dp로 모든 주기의 비밀번호 계산하고 해당 times에 맞는 비번 result에 넣어주면 될듯
cycle의 최대길이 10000
"""


def solution(k, a, b, init_password, times):
    answer = []
    cycle = [0] * (times[len(times) - 1] // k + 1)
    cycle[0] = int(init_password)

    for i in range(1, len(cycle)):
        cycle[i] = (a * cycle[i - 1] + b) % 10000

    for time in times:
        t = int(time) // k
        answer.append("{:0>4}".format(str(cycle[t])))

    return answer


print(solution(30, 25, 13, "0001", [0, 29, 30, 119, 120]))
