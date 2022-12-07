import os

lines = []
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()


class Node:
    def __init__(self, parent: 'Node', size=0):
        self.type = "f" if size > 0 else "d"
        self.size = size
        self.parent = parent
        self.children:dict[str,'Node'] = {}

    def isdir(self):
        return self.type == "d"

    def get_children(self):
        return self.children

    def add_child(self, child_name: str, child_node:'Node'):
        self.children[child_name] = child_node
        return child_node

    def __str__(self):
        return str(self.size) + str(self.children)
        
def print_node(node: Node, depth=0):
    print(" "*depth, node.type, node.size)
    for name, cnode in node.get_children().items():
        print_node(cnode, depth+1)




disk = Node(parent=None)
cwd = disk
for line in lines:
    if line.startswith("$ cd .."):
        cwd = cwd.parent
    elif line.startswith("$ cd /"):
        cwd = disk
    elif line.startswith("$ cd"):
        target = line.strip().split(" ")[2]
        cwd = cwd.add_child(target, Node(parent=cwd))
    elif line.startswith("$ ls") or line.startswith("dir"):
        continue
    else:
        size = line.strip().split(" ")[0]
        target = line.strip().split(" ")[1]
        cwd.add_child(target, Node(parent=cwd, size=int(size)))

print_node(disk)
        


