import os

lines = []
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()


class Node:
    def __init__(self, name, parent: 'Node', size:int=0):
        self.name = name
        self.type = "f" if size > 0 else "d"
        self.size = size
        self.parent = parent
        self.children:dict[str,'Node'] = {}

    def isdir(self):
        return self.size == 0

    def get_children(self):
        return self.children

    def add_child(self, child_node:'Node'):
        self.children[child_node.name] = child_node
        return child_node

    def get_total_size(self):
        if self.size > 0:
            return self.size
        else:
            size_map = map(lambda x: x.get_total_size(), self.children.values())
            return sum(size_map)

    def __str__(self):
        return str(self.size) + str(self.children)
        
def print_node(node: Node, max_size=None, depth=0):
    size = node.get_total_size()
    if max_size is not None and size <= max_size and node.isdir():
        print(" "*depth, node.name, node.type, str(size))
    for name, cnode in node.get_children().items():
        print_node(cnode, max_size=max_size, depth=depth+1)




disk = Node(name="/", parent=None)
cwd = disk
for line in lines:
    if line.startswith("$ cd .."):
        cwd = cwd.parent
    elif line.startswith("$ cd /"):
        cwd = disk
    elif line.startswith("$ cd"):
        target = line.strip().split(" ")[2]
        cwd = cwd.add_child(Node(name=target, parent=cwd))
    elif line.startswith("$ ls") or line.startswith("dir"):
        continue
    else:
        size = line.strip().split(" ")[0]
        target = line.strip().split(" ")[1]
        cwd.add_child(Node(name=target, parent=cwd, size=int(size)))

print_node(disk)
print_node(disk, max_size=100000)

