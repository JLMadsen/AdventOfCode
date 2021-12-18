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
            print('explode pair', self, 'with depth', self.depth)
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
            # parent is none if there are no numbers in that direction from origin
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
            print('split at value', self.value)
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

    def __repr__(self):
        return ( "\nNode:" + 
                 "\nValue " + str(self.value) +
                 "\nDepth " + str(self.depth) + 
                 "\nChildres " + str(self.left != None) + " " + str(self.right != None) +
                 "\nParent " + str(self.parent != None) )

def add(a, b):
    print('add', a, ' + ', b)
    parent = Node()
    parent.append(a)
    parent.append(b)
    return parent

def parse(string):

    numbers = [*map(int, re.findall(r'\d+', string))]
    if len(numbers) == 1:
        return Node( int(numbers[0]) )

    left = ""
    right = ""
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

    right = buffer

    node = Node()
    node.append( parse(left) )
    node.append( parse(right) )

    return node

test = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

if __name__ == "__main__":
    with open('input/day18.txt') as f:
        content = f.read().split('\n')




        #test = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"

        #content = test.split('\n')

        tree = parse(content[0])

        for line in content:
            if not line:
                continue
        
            if tree == None:
                tree = parse(line)
            else:
                try:
                    node = parse(line)
                except:
                    print('crashed parsing', line)
                    exit()

                tree = add(tree, node)

            done = False
            while not done:
                print('tree', tree)
            
                if not tree.explode():
                    if not tree.split():
                        done = True

        result = tree.magnitude()
        print(result)

        # start = Node()
        # start.append(Node(5))
        # start.append(Node(6))
        # new = Node()
        # new.append(Node(11))
        # new.append(Node(12))
        # res = add(start, new)
        # print(res)
        # res.split()
        # print(res)
        # res.right.left.explode()
        # print(res)


