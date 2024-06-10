import math

def log2(x):
    return float(math.log(x))/float(math.log(2))

def gcd(x, y):
    if(y == 0):
        return x
    return gcd(y, x%y)

def infloop(x, y):
    g = gcd(x, y)
    x /= g
    y /= g

    if(log2(x+y) == math.ceil(log2(x+y))):
        return False

    return True

def solution(banana_list):
    banana_list = sorted(banana_list)
    pair = {}
    for i in range(len(banana_list)):
        pair[i] = set()

    inpair = set()
    for i in range(len(banana_list)):
        for j in range(i+1, len(banana_list)):
            if(not(infloop(banana_list[i], banana_list[j]))):
                pair[i].add(j)
                pair[j].add(i)
                inpair.add(i)
                inpair.add(j)

    idx = [i for i in range(len(banana_list))]
    def compare(x, y):
        if(len(pair[x]) > len(pair[y])):
            return -1
        elif(len(pair[x]) < len(pair[y])):
            return 1
        return 0
    idx = sorted(idx, cmp=compare)

    # print(idx)
    # print(pair)
    # print(inpair)
    res = 0
    used = [False for _ in range(len(banana_list))]
    for i in range(len(banana_list)):
        if(used[idx[i]]):
            continue

        pi = None
        for j in range(len(banana_list)):
            if(j != idx[i] and j not in pair[idx[i]] and not(used[j])):
                pi = j
                if(j in inpair):
                    break
        # print(pi)
        if(pi != None):
            used[idx[i]] = True
            used[pi] = True
        else:
            res += 1

    return res

# print(solution([1,7,3,21,13,19]))
