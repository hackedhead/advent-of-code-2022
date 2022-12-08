import os

def print_grid(grid):
    for row in grid:
        print(row)

def path_reveals_tree(trees):
    """list of trees from edge to target"""
    print(trees, end="")
    height = trees[-1]
    for each in trees[:-1]:
        if each >= height:
            print(" H")
            return False
    print(" V")
    return True
    

def tree_is_visible(tree_row, tree_col, grid):
    tree_height = grid
    top_path = []
    for row in range(0, tree_row+1):
        top_path.append(grid[row][tree_col])

    bottom_path = []
    for row in range(len(grid)-1, tree_row-1, -1):
        bottom_path.append(grid[row][tree_col])
    
    left_path = []
    for col in range(0, tree_col+1):
        left_path.append(grid[tree_row][col])
    
    right_path = []
    for col in range(len(grid[0])-1, tree_col-1, -1):
        right_path.append(grid[tree_row][col])

    if any(map(path_reveals_tree, [top_path, bottom_path, right_path, left_path])):
        return True
    return False

lines = []
with open(os.environ["IN"],"r") as file:
    lines = file.readlines()

grid = []
for line in lines:
    grid.append(list(map(int,list(line.strip()))))

width = len(grid[0])
height = len(grid)

print_grid(grid)

visible_trees = len(grid) *2 + ( len(grid[0]) -2 )*2

for row in range(1, len(grid)-1):
    for col in range(1, len(grid[0])-1):
        print(f"checking {row},{col}")
        if tree_is_visible(row, col, grid):
            visible_trees += 1
print(f"Grid: {width} x {height}")
print(f"Total Trees:   {width*height}")
print(f"Visible Trees: {visible_trees}")
