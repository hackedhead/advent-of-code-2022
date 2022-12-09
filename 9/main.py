import functools
import os
import nine


lines = []
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()


knots = {}
for each in range(10):
    knots[ each ] = nine.Loc(0,0)

tail_visits = []
tail_visits.append(knots[9].get_loc())
for line in lines:
    direction, count = line.strip().split()
    count = int(count)
    
    movement = {"R": nine.Loc.right,
                "L": nine.Loc.left,
                "D": nine.Loc.down,
                "U": nine.Loc.up}[direction]
    for step in range(count):
        movement(knots[0]) # move the head
        for idx in range(1,len(knots)):
            prev_idx = idx - 1
            knots[idx].move(*nine.tail_follows(*knots[prev_idx].get_loc(),*knots[idx].get_loc()))
        tail_visits.append(knots[9].get_loc())

print(f"Visits: {len(set(tail_visits))}")


