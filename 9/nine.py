import math


class Loc:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def up(self):
        self.y += 1
    def down(self):
        self.y -= 1
    def left(self):
        self.x -= 1
    def right(self):
        self.x += 1
    def move(self, x, y):
        self.x = x
        self.y = y

    def get_loc(self):
        return (self.x, self.y)

def tail_follows(head_x, head_y, tail_x, tail_y):
    diff_x = head_x - tail_x
    diff_y = head_y - tail_y
    
    if abs(diff_x) + abs(diff_y) > 2:
        tail_x += int(math.copysign(1, diff_x))
        tail_y += int(math.copysign(1, diff_y))
    elif abs(diff_x) + abs(diff_y) < 2:
        return (tail_x, tail_y) # adjacent
    elif diff_y and not diff_x:
        tail_y += int(math.copysign(1, diff_y))
    elif diff_x and not diff_y:
        tail_x += int(math.copysign(1, diff_x))

    return (tail_x, tail_y)




