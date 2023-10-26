import sys
from itertools import combinations

input = sys.stdin.readline


def lotto(string):
    arr = list(map(int, string.split()))
    lst = list(combinations(arr[1:], 6))
    for i in lst:
        print(*i)
    print()


string = input()
while string:
    lotto(string)
    string = input()
    if string[0] == '0':
        exit()
