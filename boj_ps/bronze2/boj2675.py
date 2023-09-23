import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    for i in range(len(S.strip())):
        print(S[i] * R)
    print('\n')
