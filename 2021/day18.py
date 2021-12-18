import math
import re

class Side:
    LEFT = 0
    RIGHT = 1

class Node:
    def __init__(self, value=None, left=None, right=None, depth=1, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth
        self.parent = parent

    def increase_depth(self):
        self.depth += 1
        if self.left: self.left.increase_depth()
        if self.right: self.right.increase_depth()

    def explode(self):
        if self.depth > 4 and self.value == None:
            self.parent.__explode__(self, Side.RIGHT, self.left.value)
            self.parent.__explode__(self, Side.LEFT, self.right.value)
            self.left = self.right = None
            self.value = 0
            return True
        if self.left: 
            if self.left.explode():
                return True
        if self.right: 
            if self.right.explode():
                return True
        return False

    def __explode__(self, caller, target, value):
        if caller == self.right and target == Side.RIGHT:

            self.left.traverse_and_add(value, target)

        elif caller == self.left and target == Side.LEFT:

            self.right.traverse_and_add(value, target)
        else:
            if self.parent != None:
                self.parent.__explode__(self, target, value)

    def traverse_and_add(self, value, side):
        if self.value != None:
            self.value += value
            return

        elif side == Side.RIGHT:
            self.right.traverse_and_add(value, side)
        else:
            self.left.traverse_and_add(value, side)

    def split(self):
        if self.value != None and self.value >= 10:
            div = self.value / 2
            self.value = None
            self.left = Node(math.floor(div), depth=self.depth+1, parent=self)
            self.right = Node(math.ceil(div), depth=self.depth+1, parent=self)
            return True
        else:
            if self.left: 
                if self.left.split():
                    return True
            if self.right: 
                if self.right.split():
                    return True
        return False

    def append(self, node):
        node.increase_depth()
        node.parent = self
        if not self.left:
            self.left = node
        else:
            self.right = node

    def magnitude(self):
        if self.value != None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def __str__(self):
        if self.value != None:
            return self.value
        
        left = self.left.__str__()
        right = self.right.__str__()
        return f"[{left},{right}]"

def add(a, b):
    parent = Node()
    parent.append(a)
    parent.append(b)
    return parent

def parse(string):
    numbers = [*map(int, re.findall(r'\d+', string))]
    if len(numbers) == 1:
        return Node( int(numbers[0]) )

    left = ""
    buffer = ""
    nest = 0
    for i, char in enumerate(string[1:-1]):
        if char == '[': nest += 1
        if char == ']': nest -= 1

        if char == ',' and nest == 0:
            left = buffer
            buffer = ""
        else:
            buffer += char

    node = Node()
    node.append( parse(left) )
    node.append( parse(buffer) )
    return node

if __name__ == "__main__":
    with open('input/day18.txt') as f:
        content = f.read().split('\n')
        tree = None

        for line in content:
            if not line: continue
        
            if tree == None:
                tree = parse(line)
            else:
                tree = add(tree, parse(line))

            while not done:            
                if not tree.explode():
                    if not tree.split():
                        break

        result = tree.magnitude()
        print(tree)
        print(result) # 4116

        tree = None
        max_magnitude = 0

        for l1 in content:
            for l2 in content:
                if not l1 or not l2 or l1 == l2: continue
                tree = add(parse(l1), parse(l2))
                while 1:
                    if not tree.explode():
                        if not tree.split():
                            break

                if (magnitude := tree.magnitude()) > max_magnitude:
                    max_magnitude = magnitude
                
        print( max_magnitude ) # 4638