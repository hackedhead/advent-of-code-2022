import os

def pairs_to_tuple(pair):
    return list(map(int, pair.split("-")))

def get_ranges(line):
    return sorted(map(pairs_to_tuple, line.split(",")))

def contained(r_one, r_two):
    if r_one[0] <= r_two[0] and r_one[1] >= r_two[1]:
        return True
    if r_two[0] <= r_one[0] and r_two[1] >= r_one[1]:
        return True
    return False

def overlap(r_one, r_two):
    oneset = set(range(r_one[0], r_one[1]+1))
    twoset = set(range(r_two[0], r_two[1]+1))
    
    return oneset.intersection(twoset) != set()

with open(os.environ["IN"],"r") as file:
    contained_count = 0
    overlap_count = 0
    for line in file:
        ranges = get_ranges(line)
        print(line.strip(), end="  ---- ")
        print(ranges, end="")
        if contained(*ranges):
            print("contained ", end="")
            contained_count +=1
        if overlap(*ranges):
            print("overlaps ", end="")
            overlap_count +=1
        print("")
print("Contained: ", contained_count)
print("Overlaps: ", overlap_count)
