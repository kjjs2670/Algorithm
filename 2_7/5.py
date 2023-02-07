# 중앙값 구하기
def solution(array):
    array1 = sorted(array)
    answer = array1[len(array1)//2]
    return answer