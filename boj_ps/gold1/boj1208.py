import sys

"""
N개의 정수로 이루어진 수열
크기가 양수(1~N)인 부분수열 중 수열의 합이 S가 되는 경우의 수
부분수열
중간에 뛰어넘는 숫자가 있어도 됨
흠...
개어렵
최대길이 N
길이 1짜리
2짜리
...40짜리까지 있음
개많은데
길이 1짜리는 40C1
2짜리는 40C2
길이 3짜리는 40C3...
...40C40까지
비트마스킹 안되고
순서대로...
투포인터 안되고


"""

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
