#!/usr/bin/env python3

cratesData, movesData = open("data.txt").read().split('\n\n')

def parseMove(move):
	# example move: move 1 from 2 to 1
	_, count, _, origin, _, dest = move.split(' ')
	return int(count), int(origin)-1, int(dest)-1

moves = [parseMove(x.strip()) for x in movesData.split('\n')]

# make empty stack lists
cratesData = cratesData.rstrip().split('\n')
stacksCount = int(cratesData[-1].split(' ')[-1])
stacks = [[] for x in range(stacksCount)]

# populate initial stacks
for i  in range(len(cratesData)-2, -1, -1):
	stackRow = cratesData[i]
	for stack in range(stacksCount):
		crateID = stackRow[1+4*stack]
		if crateID != ' ':
			stacks[stack].append(crateID)

# perform movements
for move in moves:
	count, origin, dest = move
	# part 1
	#for i in range(count):
		# stacks[dest].append(stacks[origin].pop())
		
	# part 2
	moving = stacks[origin][-count:]
	stacks[origin] = stacks[origin][:-count]
	stacks[dest] += moving
		
topCrates = [x[-1] for x in stacks]
print(''.join(topCrates))