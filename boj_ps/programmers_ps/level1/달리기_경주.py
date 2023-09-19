def solution(players, callings):
    dic = dict()

    # dict에 이름, 순위로 넣어놓기
    for i in range(len(players)):
        dic[players[i]] = i

    def swap(call):
        now = dic[call]
        front = players[now - 1]
        players[now - 1] = call
        players[now] = front
        dic[call] = now - 1
        dic[front] = now

    for call in callings:
        swap(call)

    return players
