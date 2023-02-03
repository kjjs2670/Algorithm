# 피자 나눠 먹기 (1)
def solution(n):
    answer = n//7 + bool(n%7)
    return answer