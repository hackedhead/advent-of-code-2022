import os
import itertools


layout = []
instructions = []


class Move:
    def __init__(self, count, from_col, to_col):
        self.count = count
        self.from_col = from_col-1
        self.to_col = to_col-1

def parse_move(line):
    tokens = line.strip().split(" ")
    return Move(int(tokens[1]), int(tokens[3]), int(tokens[5]))

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


def print_layout(layout):
    for each in layout:
        for crate in each:
            print(crate, end=" ")
        print("")

def process_move(move, layout):
    stack = []
    for step in range(move.count):
        stack.append(layout[move.from_col].pop())
    stack.reverse()
    for crate in stack:
        layout[move.to_col].append(crate)


def process_instructions(instructions, layout):
    for move in instructions:
        process_move(move, layout)


with open(os.environ["IN"],"r") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("move"):
            instructions.append(parse_move(line))
        else:
            layout.append(list(itertools.islice(line,1,None,4)))


    layout =  reflow_layout(layout)
    print_layout(layout)

    process_instructions(instructions, layout)
    print("-----")
    print_layout(layout)
