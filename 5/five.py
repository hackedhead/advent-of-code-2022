import os
import itertools


layout = []
instructions = []

def parse_move(line):
    tokens = line.strip().split(" ")
    return (tokens[1], tokens[3], tokens[5])

def reflow_layout(layout):
    # drop two final lines
    layout = list(reversed(layout[:-2]))
    # print(list(layout))
    # reorder to column-centric
    new_layout = []
    for item in layout[0]:
        new_layout.append([])

    for row in layout:
        for col, item in enumerate(row):
            if item != " ":
                new_layout[col].append(item)

    return new_layout



with open(os.environ["IN"],"r") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("move"):
            instructions.append(parse_move(line))
        else:
            layout.append(list(itertools.islice(line,1,None,4)))


    layout =  reflow_layout(layout)
