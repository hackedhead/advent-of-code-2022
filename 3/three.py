import os

def get_pri(letter):
    lord = ord(letter)
    if lord <= ord("Z"):
        return lord - ord('A') + 27
    else:
        return lord - ord('a') + 1

total_pri = 0
with open(os.environ["IN"],"r") as file:
    for line in file:
        first = line[:int(len(line)/2)]
        second = line[int(len(line)/2):]
        fset = set(first)
        sset = set(second)

        both = fset.intersection(sset)
        total_pri += get_pri(both.pop())
    print(total_pri)


