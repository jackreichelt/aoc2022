#!/usr/bin/env python3

data = [x.strip() for x in open("data.txt").readlines()]

sandOrigin = (500, 0)

cells = {}

for formation in data:
    rocks = [[int(n) for n in x.split(",")] for x in formation.split(" -> ")]
    for i, rock1 in enumerate(rocks[:-1]):
        rock2 = rocks[i+1]
        if rock1[0] == rock2[0]:
            # rock moves vertically
            x = rock1[0]
            start = min(rock1[1], rock2[1])
            end = max(rock1[1], rock2[1]) + 1
            for y in range(start, end):
                cells[(x, y)] = '#'
        else:
            # rock moves horizontally
            y = rock1[1]
            start = min(rock1[0], rock2[0])
            end = max(rock1[0], rock2[0]) + 1
            for x in range(start, end):
                cells[(x, y)] = "#"

lowestPoint = max([y for x, y in cells.keys()])

floor = lowestPoint + 2

def canMoveDown(sandPos):
    return (sandPos[0], sandPos[1]+1) not in cells and sandPos[1]+1 != floor

def canMoveDownLeft(sandPos):
    return (sandPos[0]-1, sandPos[1]+1) not in cells and sandPos[1]+1 != floor

def canMoveDownRight(sandPos):
    return (sandPos[0]+1, sandPos[1]+1) not in cells and sandPos[1]+1 != floor

totalSandCount = 0
sandPos = sandOrigin
while True:
#   if sandPos[1] > lowestPoint:
#       break
    
    if canMoveDown(sandPos):
        sandPos = (sandPos[0], sandPos[1]+1)
    elif canMoveDownLeft(sandPos):
        sandPos = (sandPos[0]-1, sandPos[1]+1)
    elif canMoveDownRight(sandPos):
        sandPos = (sandPos[0]+1, sandPos[1]+1)
    else:
        cells[sandPos] = "o"
        totalSandCount += 1
        if sandPos == sandOrigin:
            break
        sandPos = sandOrigin

print("Total sand units:", totalSandCount)
    