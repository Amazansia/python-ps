import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    word = input().strip()
    chararr = list(word)
    i = len(word) - 1
    while i > 0 and chararr[i - 1] >= chararr[i]:
        i -= 1
    if i <= 0:
        print("".join(chararr))
        continue
    j = len(chararr) - 1
    while chararr[j] <= chararr[i - 1]:
        j -= 1
    chararr[i - 1], chararr[j] = chararr[j], chararr[i - 1]
    print("".join(chararr[:i] + chararr[i:][::-1]))
