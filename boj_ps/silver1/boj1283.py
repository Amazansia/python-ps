import sys

"""
위에서부터 차례대로 각 옵션에 단축키를 의미하는 대표 알파벳 지정

"""

input = sys.stdin.readline
N = int(input())
isUsed = [False] * 26

arr = [""] * N
for i in range(N):
    arr[i] = input().rstrip()


def firstOneSet(string):
    splitlist = string.split()
    for now in range(len(splitlist)):
        s = splitlist[now][0]
        if s.isalpha() and not isUsed[ord(s.lower()) - ord('a')]:
            isUsed[ord(s.lower()) - ord('a')] = True
            temp = list(splitlist[now])
            temp.insert(0, "[")
            temp.insert(2, "]")
            splitlist[now] = "".join(temp)
            arr[idx] = " ".join(splitlist)
            return True


def allOneSet(string):
    for i in range(len(string)):
        if string[i].isalpha() and not isUsed[ord(string[i].lower()) - ord('a')]:
            # print(i)
            isUsed[ord(string[i].lower()) - ord('a')] = True
            temp = list(string)
            if i == 0:
                temp.insert(0, "[")
            else:
                temp.insert(i, "[")
            temp.insert(i + 2, "]")
            arr[idx] = "".join(temp)
            # print("".join(temp))
            return


for idx in range(N):
    if not firstOneSet(arr[idx]):
        allOneSet(arr[idx])

# print(*isUsed)
for string in arr:
    print(string)
