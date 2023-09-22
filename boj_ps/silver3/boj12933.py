import sys

"""
올바른 울음 소리...
q쓰면될듯
울음소리가 최대로 겹치는 타이밍에 오리가 몇마리인지 알면 된다
"""
input = sys.stdin.readline

str_ = input()

# q, qu, qua, quac, quack
answer = [0, 0, 0, 0, 0]

toInt = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

for h in range(len(str_) - 1):
    i = str_[h]
    it = toInt[i]
    if it == 0:
        answer[it] += 1
    elif answer[0] > 0 and it == 1:
        answer[0] -= 1
        answer[1] += 1
    elif answer[1] > 0 and it == 2:
        answer[1] -= 1
        answer[2] += 1
    elif answer[2] > 0 and it == 3:
        answer[2] -= 1
        answer[3] += 1
    elif answer[3] > 0 and it == 4:
        answer[4] = max(answer[4], answer[0] + answer[1] + answer[2] + answer[3])
        answer[3] -= 1
    else:
        answer[4] = -1
        break

if str_[-2] != 'k':
    answer[4] = -1
for i in range(4):
    if answer[i] != 0:
        answer[4] = -1
print(answer[4])
