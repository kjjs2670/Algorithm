# do it! 002 평균 구하기
n = int(input())
lst = list(map(int, input().split()))
maxv = max(lst)
summ = sum(lst)
print(summ/maxv/int(n)*100)