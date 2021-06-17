# Node: Class

## INTRODUCTION

**Node** is an user defined class designed with a view to define a node for a binary tree 
dynamically. It is **NOT** a generalised node and only compatible for a binary trees.  

## ARCHITECTURE

A self sufficient entity for a node of a binary tree. Mainly designed as a node for 
BinaryTree data structure. 

## DATA MEMBERS

**Node.id**
*   *int*  
*   Id of that particular node. This id can be used as a primary key to uniquely specify
    this node in a data structure. For example this id is used as index of the node list
    in a BinaryTree object. Thus it allows to access in O(1) time.

**Node.value**
*   *anything*   
*   value of the node.

**Node.left_child_id**
*   *int*
*   id of the left child.

**Node.right_child_id**
*   *int*
*   id of the right child.

**Node.parent_id**
*   *int*
*   id of the parent.


## MEMEBER METHODS

*No member functions.*

## EXAMPLES
```python
#Importing
from dataStructure import Node

#Creating/initializing an object
N = Node(parent_id, value = val)
    
#Set parent
N.parent_id = a_parent_id

#Set left_child_id
N.left_child_id =  a_left_child_id
```

