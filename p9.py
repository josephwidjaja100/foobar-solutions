from math import factorial, pow

def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b);

def partition(n, x=1):
    yield [n]
    for x in range(x, n//2+1):
        for y in partition(n-x, x):
            yield [x] + y

def expsum(rowp, colp):
    amt = 0
    for a in rowp:
        for b in colp:
            amt += gcd(a, b)
    return amt

def conjugate(c, n):
    res = factorial(n)
    d = {}
    for val in c:
        if(not(val in d)):
            d[val] = 1
        else:
            d[val] += 1
    for a, b in d.items():
        res //= (a**b)*factorial(b)
    return res

def solution(w, h, s):
    div = factorial(w) * factorial(h)

    res = 0
    for r in partition(w):
        for c in partition(h):
            exp = expsum(r, c)
            x = conjugate(r, w) * conjugate(c, h)
            res += x*(s**exp)

    return str(int(res//div))

# print(solution(2,2,2))
