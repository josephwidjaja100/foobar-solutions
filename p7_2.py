import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def flipc(x, y, dimx0, dimx, dimy0, dimy, flipx, flipy):
    newx = x - dimx0
    newy = y - dimy0

    if(flipx):
        newx = dimx - newx
    if(flipy):
        newy = dimy - newy

    return [newx + dimx0, newy + dimy0]

def filter(pts, your_position, distance):
    filtdist = []
    for c in pts:
        if(dist(c[0], c[1], your_position[0], your_position[1]) <= distance):
            filtdist.append(c)

    filtang = []
    angset = set()
    for c in filtdist:
        ang = math.atan2(c[1] - your_position[1], c[0] - your_position[0])
        if(ang not in angset):
            angset.add(ang)
            filtang.append(c)

    return filtang

def solution(dimensions, your_position, trainer_position, distance):
    maxx = float(your_position[0] + distance)
    maxy = float(your_position[1] + distance)

    mirrordimx = int(math.ceil(maxx/dimensions[0]))
    mirrordimy = int(math.ceil(maxy/dimensions[1]))

    quad1target = []
    quad1player = []

    for i in range(mirrordimx+1):
        for j in range(mirrordimy+1):
            flipx = (i % 2 == 1)
            flipy = (j % 2 == 1)
            quad1target.append(flipc(trainer_position[0]+i*dimensions[0], trainer_position[1]+j*dimensions[1], i*dimensions[0], dimensions[0], j*dimensions[1], dimensions[1], flipx, flipy))
            quad1player.append(flipc(your_position[0]+i*dimensions[0], your_position[1]+j*dimensions[1], i*dimensions[0], dimensions[0], j*dimensions[1], dimensions[1], flipx, flipy))

    quad2target = [[-quad1target[i][0],quad1target[i][1]] for i in range(len(quad1target))]
    quad3target = [[-quad1target[i][0],-quad1target[i][1]] for i in range(len(quad1target))]
    quad4target = [[quad1target[i][0],-quad1target[i][1]] for i in range(len(quad1target))]

    quad2player = [[-quad1player[i][0],quad1player[i][1]] for i in range(len(quad1player))]
    quad3player = [[-quad1player[i][0],-quad1player[i][1]] for i in range(len(quad1player))]
    quad4player = [[quad1player[i][0],-quad1player[i][1]] for i in range(len(quad1player))]

    targetpts = filter(quad1target + quad2target + quad3target + quad4target, your_position, distance)
    playerpts = filter(quad1player + quad2player + quad3player + quad4player, your_position, distance)

    res = set()
    angset = set()
    angpt = {}
    for pt in targetpts:
        ang = math.atan2(pt[1] - your_position[1], pt[0] - your_position[0])
        angset.add(ang)
        angpt[ang] = pt
        res.add(ang)

    for pt in playerpts:
        if(pt == your_position):
            continue

        ang = math.atan2(pt[1] - your_position[1], pt[0] - your_position[0])
        if(ang in angset and dist(pt[0], pt[1], your_position[0], your_position[1]) < dist(angpt[ang][0], angpt[ang][1], your_position[0], your_position[1])):
            res.remove(ang)

    return len(res)

# print(solution([300,275], [150,150], [185,100], 500))
