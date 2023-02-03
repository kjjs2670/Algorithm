# 배열의 평균값
def solution(numbers):
    summ = 0
    for i in numbers:
        summ += i
    answer = summ/len(numbers)
    return answer