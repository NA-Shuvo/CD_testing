

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


precedence = {
    
    '/': 2,
    '*': 2,
    '+': 1,
    '-': 1
}

operators = ['/', '*', '+', '-']


def infix_to_postfix(infix):

    postfix = ""
    stack = Stack()

    for symbol in infix:

        if symbol in operators:
            while((not stack.isEmpty()) and precedence[symbol]<precedence[stack.top()]):
                postfix += stack.pop()
            
            stack.push(symbol)

        else:
            postfix += symbol

    while(not stack.isEmpty()):
        postfix += stack.pop()

    return postfix



infix = input("Enter Infix Notation: ")
output = "Resultant Postfix Notation: {}".format(infix_to_postfix(infix))
print(output)



from dataStructure import BinaryTree, Stack


operators = ['/', '*', '+', '-']

postfix = input()

T = BinaryTree()
stack = Stack()
parent = None


for current_symbol in postfix:

    if(current_symbol not in  operators):
        leaf = T.new_node(current_symbol)
        stack.push(leaf)

    else:
        parent = T.new_node(current_symbol)
        right_child_id = stack.pop()
        left_child_id = stack.pop()
        T.make_relation(parent, left_child_id, "left")
        T.make_relation(parent, right_child_id, "right") 

        stack.push(parent)

T.set_root(parent)
print(T)
