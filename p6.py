def solution(x, y):
    x = int(x)
    y = int(y)
    res = 0
    while(x != 1 or y != 1):
        prevx = x
        prevy = y
        if(x > y):
            res += ((x-1)//y)
            x -= ((x-1)//y)*y
        else:
            res += ((y-1)//x)
            y -= ((y-1)//x)*x
        if(prevx == x and prevy == y):
            return "impossible"

    return str(res)

print(solution('1', '50'))
