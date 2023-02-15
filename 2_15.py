import sys
input = sys.stdin.readline

N = int(input())
count = 0
lst = list(map(int, input().split()))
lst.sort()

for k in range(N):
    K = lst[k]
    st = 0
    ed = N-1
    while st<ed:
        if lst[st]+lst[ed] == K :
            if st!= k and ed!=k:
                count += 1
                break
            elif st == k:
                st += 1
            elif ed == k:
                ed -= 1
        elif lst[st]+lst[ed] < K:
            st += 1
        else:
            ed -= 1