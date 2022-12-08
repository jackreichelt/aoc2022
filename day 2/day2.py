#!/usr/bin/env python3

guide = [x.strip().split() for x in open("data.txt").readlines()]

myPlayScores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}
resultScores = {
  "L": 0,
  "D": 3,
  "W": 6
}

score = 0

for opp, me in guide:
  score += myPlayScores[me]
  result = ""
  
  if opp == "A":  # rock
    if me == "X":
      result = "D"
    elif me == "Y":
      result = "W"
    else:
      result = "L"
  elif opp == "B":  # paper
    if me == "X":
      result = "L"
    elif me == "Y":
      result = "D"
    else:
      result = "W"
  elif opp == "C":  # scissors
    if me == "X":
      result = "W"
    elif me == "Y":
      result = "L"
    else:
      result = "D"
    
  score += resultScores[result]
  
print(score)  # score 1

score = 0
playScores = {
  "R": 1,
  "P": 2,
  "S": 3
}
resultScores = {
  "X": 0,
  "Y": 3,
  "Z": 6
}

for opp, me in guide:
  score += resultScores[me]
  
  myPlay = ""
  if opp == "A":  # rock
    if me == "X":
      myPlay = "S"
    elif me == "Y":
      myPlay = "R"
    else:
      myPlay = "P"
  elif opp == "B":  # paper
    if me == "X":
      myPlay = "R"
    elif me == "Y":
      myPlay = "P"
    else:
      myPlay = "S"
  elif opp == "C":  # scissors
    if me == "X":
      myPlay = "P"
    elif me == "Y":
      myPlay = "S"
    else:
      myPlay = "R"
    
  score += playScores[myPlay]
  
print(score)  # score 2