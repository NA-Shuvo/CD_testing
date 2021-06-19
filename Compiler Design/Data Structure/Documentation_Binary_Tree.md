# Class: BinaryTree 

## INTRODUCTION

**BinaryTree** is an user defined class designed with a view to construct a binary tree 
dynamically and traverse through its nodes with different orders. 


## ARCHITECTURE

The definition of the class is based on very simple architecture. In a rooted binary tree 
every node has at most two children. In this class a node is defined as another class with 
object variables such as node id, value, ids of the left and right children and parent id. 
The ids of the left and right child nodes are indices to the list where they are stored. 
The BinaryTree class declares a public list to hold all the nodes. The node id is the own 
index of the node to the node list. Thus, one can access to a particular node only by its 
node id. Another public variable is used as the root's index for the tree.


## DATA MEMBERS

**BinaryTree.nodes**
*   *list*  
*   It is initialized as a blank list at the creation of BinaryTree object.

**BinaryTree.root**
*   *int*   
*   Root's index to the node list (ie. BinaryTree.nodes).
*   root is initialized as None when an object is created. It can be updated to a new_index 
    dynamically by the member function set_root(new_index)


## MEMEBER METHODS

**BinaryTree.new_node(self, val)**    
*   Creates a new node with the value val. This function appends this newly created node to 
    the node list, sets its index as node_id and returns the id.

**BinaryTree.make_relation(self, parent_id, child_id, order)** 
*   Defines relation between a node with parent_id and a node with child_id with given order.
    The parameter order can take only two values ('left' or 'right'). If 'left' argument is 
    passed then the child_id is set as the left_child_id in the node with parent_id. Same 
    argument is valid for the argument 'right'. On the other hand parent_id is set as the 
    parent_id in child node.

**BinaryTree.set_root(self, new_root_id)**
*   Sets the new_root_id as root.

**traverse(self, order = 'in_order')**
*   Traverse through the nodes of the tree in different orders. The parameter order can take
    only three('pre_order', 'in_order', 'post_order') values. It returns a list with node 
    indices according to the given order. Root must be set prior to calling this function.

**BinaryTree.__print__(self, order = 'in_order')**
*   Prints the values of the nodes according to given order. The parameter order can take
    only three('pre_order', 'in_order', 'post_order') values like above.

**BinaryTree.__str__(self)**
*   Prints the whole tree object. But like traverse function root must be set prior to calling
    this function.   


## EXAMPLES

```python
#Importing
from dataStructure import BinaryTree

#Creating/initializing an object
T = BinaryTree()

#Creating a new node with the value 1. 
root = T.new_node(1)

#Creating a new node with value 2 and declare it a child of root
left = T.new_node(2)
T.make_relation(root, left, "left")

#A right right for the above root
right = T.new_node(3)
T.make_relation(root, right, "right")

#Some more codes
right_left = T.new_node(4)
T.make_relation(right, right_left, "left")
right_right = T.new_node(5)
T.make_relation(right, right_right, "right")
rll = T.new_node(6)
T.make_relation(right_left, rll, "left")
rllr = T.new_node(7)
T.make_relation(rll, rllr, "right")

#Set the root as new root
T.set_root(root)
#Printing the tree in post order
T.__print__('post_order')

#Printing Tree T:
print(T)
```
