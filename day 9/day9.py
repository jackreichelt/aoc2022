#!/usr/bin/env python3
from math import sqrt

steps = [x.strip().split(" ") for x in open("data.txt").readlines()]

headPos = (0,0)
tailPos = (0,0)
tailLog = {(0,0)}

U = (0,1)
D = (0, -1)
L = (-1, 0)
R = (1, 0)

dirs = {"U": U, "D":D, "L":L, "R":R}

def moveHead(dir):
    global headPos
    headPos = (headPos[0] + dir[0], headPos[1] + dir[1])

def ropeLength():
    a = headPos[0] - tailPos[0]
    b = headPos[1] - tailPos[1]
    return sqrt(a**2 + b**2)

def catchUpTail():
    global tailPos
    global tailLog
    
    rLen = ropeLength()
    if rLen < 2:
        # close enough
        pass
    elif rLen == 2:
        # linear offset
        if tailPos[0] == headPos[0]:
            # x pos is the same
            if tailPos[1] < headPos[1]:
                tailPos = (tailPos[0] + U[0], tailPos[1] + U[1])
            else:
                tailPos = (tailPos[0] + D[0], tailPos[1] + D[1])
        else:
            # y pos is the same
            if tailPos[0] < headPos[0]:
                tailPos = (tailPos[0] + R[0], tailPos[1] + R[1])
            else:
                tailPos = (tailPos[0] + L[0], tailPos[1] + L[1])
    else:
        # it's diagonally away
        if tailPos[1] < headPos[1]:
            tailPos = (tailPos[0] + U[0], tailPos[1] + U[1])
        else:
            tailPos = (tailPos[0] + D[0], tailPos[1] + D[1])
        if tailPos[0] < headPos[0]:
            tailPos = (tailPos[0] + R[0], tailPos[1] + R[1])
        else:
            tailPos = (tailPos[0] + L[0], tailPos[1] + L[1])
    tailLog.add(tailPos)
    
for d, c in steps:
    for i in range(int(c)):
        moveHead(dirs[d])
        catchUpTail()

print(len(tailLog))