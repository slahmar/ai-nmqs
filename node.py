# Salomé Lahmar 16201438

class Node:
    def __init__(self, estimated): 
        self.estimated = estimated
        self.children = list()
	
    def print_message(self, depth, alpha, beta, value, method):
        print("Depth {} with a={}, b={} by {} evaluation -> value={}".format(depth, alpha, beta, method, value))
   
    def print_node(self, height):
        display = ""
        for i in range(0, height):   
            display += "   "
        print("{} e = {}".format(display, self.estimated))
        
    def print_tree(self, height):
        self.print_node(height)
        for child in self.children:
            child.print_tree(height-1)
		
    def append_child(self, child):
        self.children.append(child)
