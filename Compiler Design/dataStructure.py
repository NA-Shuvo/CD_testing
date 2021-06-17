
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def __show__(self):
        print(self.items)


class Node:

    def __init__(self, node_id, value = None, /, left_child_id = None, right_child_id = None, parent_id = None):
        self.id = node_id
        self.value = value
        self.left_child_id = left_child_id
        self.right_child_id = right_child_id
        self.parent_id = parent_id


class BinaryTree:

    def __init__(self):
        self.root = None
        self.nodes = []

    def new_node(self, val):
        pos = self.nodes.__len__()
        temp = Node(pos, val)  
        self.nodes.append(temp)
        return pos
    
    def make_relation(self, parent_id, child_id, order):

        parent = self.nodes[parent_id]
        child = self.nodes[child_id]

        if (order == 'left'):
            parent.left_child_id = child_id
            child.parent_id = parent_id
        else:
            parent.right_child_id = child_id
            child.parent_id = parent_id

    def set_root(self, pos):
        self.root = pos
            
    def in_order_traverse(self, root, result):
        if self.nodes[root].left_child_id != None:
            self.in_order_traverse(self.nodes[root].left_child_id, result)
        
        result.append(root)

        if self.nodes[root].right_child_id != None:
            self.in_order_traverse(self.nodes[root].right_child_id, result)

    def pre_order_traverse(self, root, result):

        result.append(root)

        if self.nodes[root].left_child_id != None:
            self.pre_order_traverse(self.nodes[root].left_child_id, result)
        
        if self.nodes[root].right_child_id != None:
            self.pre_order_traverse(self.nodes[root].right_child_id, result)

    def post_order_traverse(self, root, result):

        if self.nodes[root].left_child_id != None:
            self.post_order_traverse(self.nodes[root].left_child_id, result)
        
        if self.nodes[root].right_child_id != None:
            self.post_order_traverse(self.nodes[root].right_child_id, result)
        
        result.append(root)

    def traverse(self, order = 'in_order'):
        result = []
        if order == 'in_order':
            self.in_order_traverse(self.root, result)
        if order == 'pre_order':
            self.pre_order_traverse(self.root, result)
        if order == 'post_order':
            self.post_order_traverse(self.root, result)

        return  result

    def __print__(self, order = 'in_order'):
        result = self.traverse(order)
        for node_id in result:
            print(self.nodes[node_id].value, end = "")

    def render(self, parent, breadth = 0):
        for i in range(breadth):
            if i == breadth -1:                
                print("+--", end ="")
            else:
                print("|  ", end ="")
        output = "({})".format(self.nodes[parent].value) 
        print(output)
        if self.nodes[parent].right_child_id != None:
            self.render(self.nodes[parent].right_child_id, breadth + 1)
        if self.nodes[parent].left_child_id != None:
            self.render(self.nodes[parent].left_child_id, breadth + 1)
