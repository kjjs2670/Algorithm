from collections import deque
N, L = map(int, input().split())
q = deque()     # 데이터를 담을 덱 자료구조
now = list(map(int, input().split()))   # 주어진 숫자 데이터를 가지는 리스트

for i in range(N):
    while q and q[-1][0] > now[i]:
        q.pop() 
        # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
    q.append((now(i), i))   # 덱의 마지막 위치에 현재 값 저장
    if q[0][1] <= i-L:     # 범위에서 벗어난 값은 덱에서 제거
        q.popleft
    print(q[0][0], end=' ') # 덱의 1번째 데이터 출력

