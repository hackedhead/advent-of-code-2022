import os
import itertools


stream = ""
with open(os.environ["IN"],"r") as file:
    stream = file.readlines()[0].strip()


print(stream)
for idx in range(4, len(stream)):
    group = set(stream[idx-4:idx])
    print(group)
    if len(group) == 4:
        print(idx)
        break


