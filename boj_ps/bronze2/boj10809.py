import sys

input = sys.stdin.readline
s = input().strip()
arr = [-1] * 26
for i in range(len(s)):
    if arr[ord(s[i]) - ord('a')] == -1:
        arr[ord(s[i]) - ord('a')] = i

print(*arr)
