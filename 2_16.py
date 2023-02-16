checkList = [0]*4   # 비밀번호 체크 리스트
myList = [0]*4      # 현재 상태 리스트
checkSecret = 0     # 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수

def add(c):   # 새로 들어온 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def remove(c):      # 제거되는 문자 처리
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i]==0:     # 비밀번호 조건 중 0개인 조건
        checkSecret += 1

for i in range(P):      # 초기 슬라이딩 윈도우 생성
    add(A[i])
if checkSecret == 4:
    Result += 1

for i in range(P,S):    # 슬라이딩 윈도우 이동
    j = i-P
    add(A[i])
    remove(A[j])
    if checkSecret == 4 :
        Result += 1

print(Result)