import os


stream = ""
with open(os.environ["IN"],"r") as file:
    stream = file.readlines()[0].strip()

for idx in range(14, len(stream)):
    group = set(stream[idx-14:idx])
    if len(group) == 14:
        print(idx)
        break
