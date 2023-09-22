import sys

"""
파이썬 ㅎ
100000 * 20
2000000
2백만
느낌싸한데
25%에서 메모리초과
애너그램 개수 10만개...
10까지는 괜찮은데 20이라 메모리가 터지는듯
dfs로 대충다만들고 sort함때려주면될듯
dfs로 안될듯
교환?
같은것끼리 교환하지 말고

"""
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
for _ in range(N):
    nstr = sorted(list(map(str, input().strip())))
    visited = {}
    answer = []

    for i in nstr:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1


    def backtracking(cnt):
        if cnt == len(nstr):
            print("".join(answer) + "\n")
            return
        for i in visited:
            if visited[i]:
                visited[i] -= 1
                answer.append(i)
                backtracking(cnt + 1)
                visited[i] += 1
                answer.pop()


    backtracking(0)
