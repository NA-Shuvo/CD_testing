
#   Module: analyzer

#   Contents

*   [Introduction](#intro)
*   [Dependency](#depend)
*   [Functions](#func)
    *   [analyzer.infix_to_postfix](#i2p)
    *   [analyzer.postfix_to_parse_tree](#p2pt)
*   [Examples](#example)
    *   [Script](#script)
    *   [Outputs](#output)

<br/>

<h2 id = 'intro'> Introduction </h2>

This module is an initial script of 'yet another compiler of c in pyhton' project. It is developed as a part of CSE326: Compiler Construction (sessional) course lecture for  students of summer 21.


<h2 id = 'depend'> Dependency </h2>

This module is highly dependent on [dataStructure](https://github.com/NA-Shuvo/CD_testing/blob/master/Compiler%20Design/Data%20Structure/dataStructure.py). To use this module put the dataStructure.py module in 
the same folder. You can organize your folder in the followingt manner:

```folder organization 
your_drive:/.../your_folder/dataStructure.py
your_drive:/.../your_folder/analyzer.py
your_drive:/.../your_folder/your_other_script_that_is_dependent_on_analyzer.py

```

<h2 id = 'func'> Functions </h2>

<h3 id = 'i2p'> analyzer.infix_to_postfix(infix) </h3>

This function takes an infix string as an input and returns corresponding postfix string.

<h3 id = 'p2pt'> analyzer.postfix_to_parse_tree(postfix) </h3>

This function takes an postfix string as an input and returns corresponding parse tree. This parse
tree is a [BinaryTree](https://github.com/NA-Shuvo/CD_testing/blob/master/Compiler%20Design/Data%20Structure/Documentation_Binary_Tree.md) object.

<h2 id = 'example'> Examples </h2>

<h3 id = 'script'> Script </h3>

```python
# ! your_drive:.../your_folder/your_other_script_that_is_dependent_on_analyzer.py

import analyzer

infix = input()
postfix = analyzer.infix_to_postfix(infix)
T = analyzer.postfix_to_parse_tree(postfix)
print(T)

```
<h3 id = 'output'> Output </h3>
  
```output

your_drive:/.../your_folder>  python your_other_script_that_is_dependent_on_analyzer.py 
ab+c-
+-(+)
+-(-)
| +-(c)
| +-(b)
+-(a)

```
