import math

def solution(ind):
    prime = [True for i in range(100000)]
    p = 2
    while(p*p <= 100000):
        if(prime[p]):
            for i in range(p*p, 100000, p):
                prime[i] = False
        p += 1
    lst = []
    for p in range(2, 100000):
        if(prime[p]):
            lst.append(p)
    # print(lst)
    amt = 0
    res = ""
    for i in range(len(lst)):
        prev = amt
        amt += len(str(lst[i]))
        # print(amt)
        # print(lst[i])
        if(amt > ind):
            k = i
            curlen = 0
            for j in range(5):
                if(ind - prev + j - curlen >= len(str(lst[k]))):
                    curlen += len(str(lst[k]))
                    k += 1
                # print(lst[k])
                # print(ind, prev, j, curlen, ind - prev + j - curlen)
                res += str(lst[k])[ind - prev + j - curlen]
            break

    return int(res)

print(solution(5))
