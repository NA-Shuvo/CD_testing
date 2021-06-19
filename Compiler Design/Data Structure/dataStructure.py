
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
        self.depth = []

    def new_node(self, val):
        pos = self.nodes.__len__()
        temp = Node(pos, val)  
        self.nodes.append(temp)
        self.depth.append(None)
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

    def __set_level(self, parent, depth):
        
        if self.nodes[parent].left_child_id != None:
            self.depth[self.nodes[parent].left_child_id] = depth + 1
            self.__set_level(self.nodes[parent].left_child_id, depth + 1)
        
        if self.nodes[parent].right_child_id != None:
            self.depth[self.nodes[parent].right_child_id] = depth + 1
            self.__set_level(self.nodes[parent].right_child_id, depth + 1)

    def set_root(self, pos):
        self.root = pos
        self.depth[pos] = 0
        self.__set_level(self.root, 0)
            
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
    
    def __prl_traverse(self, root, result):

        result.append(root)

        if self.nodes[root].right_child_id != None:
            self.__prl_traverse(self.nodes[root].right_child_id, result)


        if self.nodes[root].left_child_id != None:
            self.__prl_traverse(self.nodes[root].left_child_id, result)
        
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
        print("\n")

    def __get_tree_string(self, Id):
        path_string = []
        while(self.nodes[Id].parent_id != None):
            if self.nodes[self.nodes[Id].parent_id].right_child_id == Id:
                path_string.append("| ")
            else:
                path_string.append("  ")
            Id = self.nodes[Id].parent_id
        return path_string

    def __str__(self):

        result = []
        self.__prl_traverse(self.root, result)
        
        for nodeId in result:
            string_list = self.__get_tree_string(nodeId)
            string_list.reverse()
            for character in string_list[:string_list.__len__()-1]:
                print(character, end = "")
            print("+-", end="(")
            print(self.nodes[nodeId].value, end=")\n")
        return ""

