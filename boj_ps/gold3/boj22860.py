import sys
from collections import defaultdict

"""
파일 종류는 같은 파일이 여러 개 있을 경우 하나로 계산
파일의 총 개수는 하나로 계산하지 않는다
쿼리가 주어지면 파일의 종류의 개수와 파일 총개수 출력
파일과 폴더 이름은 동일할 수 있다...하아
"""
input = sys.stdin.readline

N, M = map(int, input().split())

folders = defaultdict(list)
info = defaultdict(tuple)

for _ in range(N + M):
    parent, child, isFolder = tuple(input().split())
    folders[parent].append((child, int(isFolder)))


def dfs(cur_path):
    file_cnt = 0
    file_set = set()

    cur = cur_path.split('/')[-1]
    for name, isFolder in folders[cur]:
        if isFolder:
            child_file_set, child_file_cnt = dfs(cur_path + '/' + name)
            file_cnt += child_file_cnt

            file_set = file_set.union(child_file_set)
        else:
            file_set.add(name)
            file_cnt += 1
    info[cur_path] = (len(file_set), file_cnt)
    return file_set, file_cnt


dfs('main')
Q = int(input())
for _ in range(Q):
    dir_name = input().rstrip()
    print(*info[dir_name])
