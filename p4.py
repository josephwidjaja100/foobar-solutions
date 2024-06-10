def path(map):
    vis = [[False for i in range(len(map[0]))] for j in range(len(map))]
    # print(vis)
    q = []
    q.append([0, 0, 1])
    while(len(q) != 0):
        cur = q.pop(0)
        x = cur[0]
        y = cur[1]
        d = cur[2]
        vis[x][y] = True

        if(x == len(map)-1 and y == len(map[0])-1):
            return d

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            x2 = x + dx[i]
            y2 = y + dy[i]

            if(x2 >= 0 and x2 < len(map) and y2 >= 0 and y2 < len(map[0]) and map[x2][y2] == 0 and not vis[x2][y2]):
                q.append([x2, y2, d+1])

    return 1e9

def solution(map):
    res = path(map)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] == 1):
                map[i][j] = 0
                res = min(res, path(map))
                map[i][j] = 1

    return str(res)

print(solution([[0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 1, 0]]))

# print(solution([[0, 0], [0, 0]]))
