# 아이스 아메리카노
def solution(money):
    answer1 = money//5500
    answer2 = money - answer1*5500
    answer = [answer1, answer2]
    return answer