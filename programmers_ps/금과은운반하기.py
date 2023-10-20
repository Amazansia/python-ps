"""
i번 도시에는 금과 은, 트럭 한 대가 있다.
새 도시를 짓는 건설 장소와 i번 도시만 왕복가능
편도로 t[i]시간, 최대 w[i]만큼의 광물 운반가능
각 도시의 트럭을 최적으로 운행했을 때, 건설비용을 모두 조달하기 위한 가장 빠른 시간을 구하시오...
도시 개수가 10만...?
금과 은을 나눠서?
시간당 가장 많은 광물을 조달할 수 있는 도시부터 계산할까요...
dp와 그리디?
시간당 가장 많은 광물...w/t로 정렬하고
dp로 n시간에 조달 가능한 광물의 합을 저장해서
10의 9승...백퍼 이진탐색
정답이 되는 시간을 이진탐색의 대상으로 두고
완탐으로 해당 시간 안에 광물을 조달할 수 있는지 여부만 체크하기
조달할 수 있다면 낮춰보고 안되면 올리고
최대로 낮출 수 있는 시간을 리턴
"""


def solution(a, b, g, s, w, t):
    answer = 4 * 10 ** 14
    l = 0
    r = 4 * 10 ** 14

    while l <= r:
        mid = (l + r) // 2
        gold = 0
        silver = 0
        add = 0
        for i in range(len(t)):
            now_g = g[i]
            now_s = s[i]
            now_w = w[i]
            now_t = t[i]
            move_cnt = mid // (now_t * 2)
            if mid % (now_t * 2) >= now_t:
                move_cnt += 1
            gold += min(now_g, move_cnt * now_w)
            silver += min(now_s, move_cnt * now_w)
            add += min(now_g + now_s, move_cnt * now_w)
        if gold >= a and silver >= b and add >= a + b:
            r = mid - 1
            answer = min(answer, mid)
        else:
            l = mid + 1

    return answer
