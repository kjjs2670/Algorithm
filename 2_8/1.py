N, M = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]
temp = 0

for i in lst:
    temp = temp + i
    arr.append(temp)

for i in range(M):
    a,b = map(int, input().split())
    print(arr[b]-arr[a-1])