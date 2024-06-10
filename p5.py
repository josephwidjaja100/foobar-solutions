def solution(l):
    adj = {}
    # lst = sorted(l)
    # print(lst)
    for i in range(len(l)):
        adj[i] = []

    for i in range(len(l)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if(l[i] % l[j] == 0):
                adj[i].append(j)
    print(adj)
    res = 0
    for i in range(len(l)-1, -1, -1):
        for j in adj[i]:
            res += len(adj[j])

    return res

print(solution([1, 5, 10, 1, 20, 10]))
