# 머쓱이보다 키 큰 사람
def solution(array, height):
    count = 0
    for i in array:
        if i>height:
            count += 1
    answer = count
    return answer