n = int(input())
# 각 변수들 초기화
count = 1
start = 1
end = 1
summ = 1

while end != n :
    if summ == n:   # summ이 n일 때 count 증가 후
        count += 1
        summ += end
    elif summ >n:   # summ이 n보다 클 때 start 위치를 뒤로 옮겨줌. summ 값 감소
        summ -= start
        start += 1
    else:   # summ이 n보다 작을 때 end 위치를 뒤로 옮겨줌. summ값 증가
        end += 1
        summ += end
print(count) 
