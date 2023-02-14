import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))
lst.sort()
count = 0
start = 0
end = N-1

while start<end:
    if lst[start]+lst[end] < M: 
        # 현재 합이 N보다 작다면 start를 1 증가
        start += 1
    elif lst[start]+lst[end] > M:
        # 현재 합이 N보다 크다면 end를 1 감소
        end -= 1
    else:
        # 현재 합이 N과 같다면 카운트를 증가하고 양쪽 포인터를 모두 이동
        count += 1
        start += 1
        end -= 1

print(count)
