import os

play_map = {
    "A": 0, #rock
    "B": 1, #paper
    "C": 2, #scissors
    "X": 0, #rock
    "Y": 1, #paper
    "Z": 2, #scissors
    }

def score_outcome(opp, own):
  if opp == own:
    return 3
  if ((opp+1) % 3) == own: # win (A Y, B Z, C X)
    return 6
  else:
    return 0

def score_plan(opp, own):
    return own+1 + score_outcome(opp, own)

with open(os.environ["INPUT"], "r") as f:
  score = 0
  for line in f:
    opp, own = line.strip().split(" ")
    opp_n = play_map[opp]
    own_n = play_map[own]
    print(opp_n, own_n)
    score += score_plan(opp_n, own_n)

  print(score)


