a, b = map(int, input().split())

def abc(level):
    print(level, end=' ')
    if level == b:
        return
    abc(level+1)
    print(level, end=' ')


abc(a)