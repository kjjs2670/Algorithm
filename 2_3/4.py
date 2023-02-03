# 삼각형의 완성조건 (1)
def solution(sides):
    sides = sorted(sides)
    if sides[0]+sides[1] > sides[2]:
        return 1
    else:
        return 2