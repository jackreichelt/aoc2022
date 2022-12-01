#!/usr/bin/env python3

elves = [x.strip() for x in open("data.txt").read().split("\n\n")]

elfInts = [sum([int(x) for x in e.split("\n")]) for e in elves]
elfInts.sort()

print(elfInts[-1])  # part 1

print(sum(elfInts[-3:]))  # part 2
