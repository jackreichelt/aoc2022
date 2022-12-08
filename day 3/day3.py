#!/usr/bin/env python3

rucksacks = [x.strip() for x in open("data.txt").readlines()]


def calcPriority(item):
  if item.isupper():
    return ord(item) - ord('A') + 27
  else:
    return ord(item) - ord('a') + 1
  
prioritySum = 0
for sack in rucksacks:
  c1 = set(sack[:len(sack)//2])
  c2 = set(sack[len(sack)//2:])
  
  shared = list(c1.intersection(c2))[0]
  prioritySum += calcPriority(shared)
  
print(prioritySum)  # part 1

badgePrioritySum = 0 
for i in range(0, len(rucksacks), 3):
  group = (rucksacks[i], rucksacks[i+1], rucksacks[i+2])
  badge = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
  
  badgePrioritySum += calcPriority(badge)
  
print(badgePrioritySum)