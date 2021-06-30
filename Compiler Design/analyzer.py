
from dataStructure import BinaryTree, Stack

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




def postfix_to_parse_tree(postfix):

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

    return T
