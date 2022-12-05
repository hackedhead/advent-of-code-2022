import os
import itertools

def get_pri(letter):
    lord = ord(letter)
    if lord <= ord("Z"):
        return lord - ord('A') + 27
    else:
        return lord - ord('a') + 1

total_pri = 0
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()
    for k, group in itertools.groupby(enumerate(lines),key=lambda x: x[0] // 3):
        packs = list(group)
        items = set(packs[0][1].strip())
        items.intersection_update(set(packs[1][1].strip()), set(packs[2][1].strip()))

        total_pri += get_pri(items.pop())
    print(total_pri)


