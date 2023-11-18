import sys

input = sys.stdin.readline

string = input().strip()

if "::" in string:
    s = string.split("::")
    front = 0
    for st in s[0].split(":"):
        if len(st) != 0: front += 1
    back = 0
    for st in s[1].split(":"):
        if len(st) != 0: back += 1

    shorten = 8 - front - back
    o4 = ["0000"] * shorten
    newst = ":".join(o4)
    if front != 0:
        newst = ":" + newst
    if back != 0:
        newst = newst + ":"
    string = string.replace("::", newst)

arr = string.split(":")

answer = []

for s in arr:
    word = s
    if len(s) != 4:
        word = ("0" * (4 - len(s))) + s
    answer.append(word)

print(":".join(answer))
