
#   Module: analyzer

#   Contents

*   [Introduction](#intro)
*   [Dependency](#depend)
*   [Functions](#func)
    *   [infix_to_postfix](#i2p)
    *   [postfix_to_parse_tree](#p2pt)
*   [Examples](#example)

<br/>

<h2 id = 'intro'> Introduction </h2>

This module is a initial stage of a project 'yet another compiler of c in pyhton'. It was developed as a part of CSE326: Compiler Construction (sessional) course lecture.


<h2 id = 'depend'> Dependency </h2>

This module is highly dependent on [dataStructure](https://github.com/NA-Shuvo/CD_testing/blob/master/Compiler%20Design/Data%20Structure/dataStructure.py). To use this module put the dataStructure module in 
the same folder.  

<h2 id = 'func'> Functions </h2>

<h3 id = 'i2p'> infix_to_postfix(infix) </h3>

This function takes an infix string as an input and returns corresponding postfix string.

<h3 id = 'p2pt'> postfix_to_parse_tree(postfix) </h3>

This function takes an postfix string as input and returns corresponding parse tree. This parse
tree is a BinaryTree object.

<h2 id = 'example'> Examples </h2>

```python
# ! /Test Codes/test.py

import analyzer

infix = input()
postfix = analyzer.infix_to_postfix(infix)
T = analyzer.postfix_to_parse_tree(postfix)
print(T)

```
### Output  
```output

Test Code>  python test.py 
ab+c-
+-(+)
+-(-)
| +-(c)
| +-(b)
+-(a)

```