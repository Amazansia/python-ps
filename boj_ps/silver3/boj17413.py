import sys

"""
단어만 뒤집기
공백은 그대로 두고 단어만 뒤집어서 출력한다
태그는 빼고
"""
input = sys.stdin.readline
print = sys.stdout.write

string = input().strip() + ' '
stack = []
answer = ''

isTag = False

for i in string:
    if i == '<':
        isTag = True
        for _ in range(len(stack)):
            answer += stack.pop()
    stack.append(i)

    if i == '>':
        isTag = False
        for _ in range(len(stack)):
            answer += stack.pop(0)

    if i == ' ' and not isTag:
        stack.pop()
        for _ in range(len(stack)):
            answer += stack.pop()
        answer += ' '

print(answer)
