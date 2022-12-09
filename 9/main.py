import functools
import os
import nine


lines = []
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()


head = nine.Loc(0,0)
tail = nine.Loc(0,0)
tail_visits = []
tail_visits.append(tail.get_loc())
for line in lines:
    direction, count = line.strip().split()
    count = int(count)
    
    movement = {"R": head.right,
                "L": head.left,
                "D": head.down,
                "U": head.up}[direction]
    for step in range(count):
        movement() # move the head
        tail.move(*nine.tail_follows(*head.get_loc(),*tail.get_loc()))
        tail_visits.append(tail.get_loc())

print(f"Visits: {len(set(tail_visits))}")


