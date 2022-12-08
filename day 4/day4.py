#!/usr/bin/env python3

pairRanges = [x.strip().split(',') for x in open("data.txt").readlines()]


totalOverlaps = 0
anyOverlaps = 0
for a, b in pairRanges:
  aStart, aStop = a.split('-')
  bStart, bStop = b.split('-')
  
  aRange = set([x for x in range(int(aStart), int(aStop)+1)])
  bRange = set([x for x in range(int(bStart), int(bStop)+1)])
  
  if aRange.issubset(bRange) or bRange.issubset(aRange):
    totalOverlaps += 1
    
  if len(aRange.intersection(bRange)) != 0:
    anyOverlaps += 1
    
print(totalOverlaps)
print(anyOverlaps)