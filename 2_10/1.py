# 나머지 합 구하기
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
lst = list(map(int, input().split()))
S=[0]*n
C=[0]*m
S[0] = lst[0]
answer = 0

for i in range(1,n):
    S[i]=S[i-1]+lst[i]

for i in range(n):
    remainder = S[i]%m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i]>1:
        answer += (C[i] * (C[i]-1)//2)

print(answer)