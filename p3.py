import math

def convert(n, b):
    res = 0
    ns = str(n)
    for i in range(len(ns)):
        d = int(ns[i])
        res += d*math.pow(b,len(ns)-i-1)
    return int(res)

def convert10(n, b):
    res = ""
    high = math.floor(math.log(n)/math.log(b))
    for i in range(int(high), -1, -1):
        d = int(n//math.pow(b,i))
        res += str(int(d))
        n -= math.pow(b,i)*d
        # print(res)
    return int(res)

def solution(n, b):
    st = n
    s = []
    s.append(n)

    if(int(n) == 0):
        return 1

    while(True):
        while(len(n) != len(st)):
            n = '0' + n
        nincl = sorted(n)
        ndecl = sorted(n, reverse = True)
        ninc = ""
        for i in nincl:
            ninc += i

        ndec = ""
        for i in ndecl:
            ndec += i

        # print('ndec:', ndec)
        # print('ninc:', ninc)
        # print(convert(int(ndec), b))
        # print(convert(int(ninc), b))
        z = convert10(convert(int(ndec), b) - convert(int(ninc), b), b)
        # print(z)
        n = str(z)
        while(len(n) != len(st)):
            n = '0' + n

        print(s)
        if(n in s):
            return str(len(s) - s.index(n))

        s.append(n)

    return str(0)

print(solution('0000', 2))
