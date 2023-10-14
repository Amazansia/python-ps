"""
특정 이벤트가 발생하면 정해진 기능을 실행한다
주기마다 이벤트 발생 확인
한 주기에 최대 limit개의 이벤트만 처리할 수 있다
한 번 확인할 때 이벤트가 최대 "하나만" 발생하도록 주기 설정
만약 설정 가능한 주기가 여러 개 있다면, 그중 가장 긴 주기를 선택한다.
3, 7 ,8
4, 8, 12
8초에 이벤트가 발생한다면 8초가 아니라 9초부터 확인 가능하다

이벤트 개수는 1000
limit는 이벤트 개수보다 작다...
bf로 최대 limit부터 확인하면 될거같은데
"""


def solution(events, limit):
    # cycle이 주어졌을 때 모든 이벤트가 limit 내에 처리될 수 있으면 True, 아니면 False

    def everything_is_okay(cycle):
        last_event = events[-1]

        event_idx = 0

        # 각 주기마다 이전에 발생한 이벤트의 개수가 limit를 초과하면 return False
        for i in range(0, last_event + cycle, cycle):
            check = i
            l = 0
            while event_idx < len(events) and events[event_idx] < check:
                l += 1
                event_idx += 1
            if l > limit:
                return False

        return True

    for i in range(events[-1], 0, -1):
        if everything_is_okay(i):
            return i

    return 1


events = [i * 2 for i in range(1000)]

print(solution(events, 4))
