paper = [[0]* 100 for i in range(100)]      # 도화지 크기
n = int(input())
for i in range(n):
    a, b = map(int, input().split())    # 색종이 크기
    for j in range(a, a+10):
        for k in range(b, b+10):
            paper[j][k] = 1     # 색종이 범위에 1 값 넣기

answer = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            answer += 1     # 범위가 1인 값 카운트 하기
print(answer)