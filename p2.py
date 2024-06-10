def solution(l, t):
    pre = [0]
    for i in range(len(l)):
        pre.append(pre[-1]+l[i])

    for i in range(len(pre)):
        for j in range(i, len(pre)):
            if(pre[j] - pre[i-1] == t):
                return (i-1, j-1)

    return (-1, -1)

print(solution([4,3,5,7,8], 12))
