# Salomé Lahmar 16201438

from node import Node 
from random import randint

# Generate a tree with a height of h, a branching factor of b
# v : true value of the node to create
# i : inaccuracy of the static evaluation function
# s : spread of values of the children of any parent
def generate_tree(b, h, v, i, s):
    if h == 0 :
        node = Node(v)
        return node
    else : 
        node = Node(v+randint(-i,i))
        index = randint(0, b-1)
        for idx in range(0, b):
            if idx == index :
                value = -v
            else :
                value = -v+randint(0,s)
            child = generate_tree(b, h-1, value, i, s)
            node.append_child(child)
        return node
