elves = [0,]
index = 0
with open("input.txt","r") as f:
    for line in f:
        if not line.strip():
            elves.append(0)
            index += 1
        else:
            elves[index] += int(line.strip())

print(elves)

print("Max:", max(elves))
