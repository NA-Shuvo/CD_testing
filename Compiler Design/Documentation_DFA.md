# Class: DFA

# Contents

* [Introduction](#intro)
* [Architecture](#archi)
* [Attributes](#data)
* [Interfaces](#methods)
  * [DFA.\__int\__](#init)
  * [DFA.update_transition_table](#ut)
  * [DFA.clear_transition_table](#ct)
  * [DFA.run](#run)
  * [DFA.sigma](#sigma)
  * [DFA.is_final_state](#check)
  * [DFA.\_str\_](#render)
* [Examples](#example)

<h2 id = 'intro'> Introduction </h2>

**DFA** is an user defined class of [models](https://github.com/NA-Shuvo/CD_testing/blob/master/Compiler%20Design/models.py) module designed with a view to implement a simple Deterministic Finite Automaton.

<h2 id = 'archi'> Architecture </h2>

The definition of the class is very straight forward and is according to the formal definition of a Finite State Machine. An object of this class will be initilaised with five arguments which are exactly the same five components of a Finite State Machine:

* A set of input alphabets(A)
* A set of states(Q)
* An startig state(s)
* A set of final states(F)
* A transition relation as a table (T)

**Note: Transition relation can be updated at run time. So, T is optional at the time of initialization.**

<h2 id = 'data'> Attributes </h2>

This class is implemented with the intention to provide only the methods or interfaces. As in python access protocols are only symbolic in meaning, any one interested to the attributes are advised to read the whole code.

<h2 id = 'methods'> Interfaces </h2>

<h3 id = 'init'> DFA.__init__(self, /, A, Q, s, F, T = None) </h3>

Initilization of a DFA requires exactly the five components mentioned above. The transition relation T is 
advised to be passed in the time of initialization. Otherwise the [update_transition_table](#ut) function can be used to set transition relation in run time. T must be given as a list of 3-tuple where first member is the current state, second member is the input alphabet and finally the last one is state after the tarsition.
 
<h3 id = 'ut'> DFA.update_transition_table(self, T) </h3>

Updates the transition table in run time. Some specific relations/the whole table can be updated with this method. T must be given as a list of 3-tuple as mentioned above.  

<h3 id = 'ct'> DFA.clear_transition_table(self) </h3>

Clear the whole transition table and set all relations to None.

<h3 id = 'run'> DFA.run(self, input) </h3>

Runs the automaton according to given inputs. Input must be given as a list. Returns the last state where the automaton stops.

<h3 id = 'sigma'> DFA.sigma(self, q, a) </h3>

Returns the state from q if input input alphabet is given a.

<h3 id = 'check'> DFA.is_final_state(self, input_state) </h3>

Returns if input_state is a final state.

<h3 id = 'render'> DFA.__str__(self) </h3>

Prints information about the DFA.

<h2 id = 'example'> Examples </h2>

```python

from models import DFA

d1 = DFA(A = [0,1], Q = ['s', 't'], s = 's', F = ['t'], T = [('s',0,'s'), ('s', 1, 't'), ('t', 0, 't'), ('t', 1, 's')])
print(d1)
print(d1.is_final_state(d1.run([0,0,1,0,1,1,1,0,1,0,0])))
print(d1.is_final_state(d1.run([1,1,1,0,1,1,0,1])))
d1.clear_transition_table()
print(d1)

d2 = DFA(Q = [0,1], A = ['s', 't'], s = 0, F = [1], T = [(0,'s',0), (0, 't', 1), (1, 's', 1), (1, 't', 0)])
print(d2)
print(d2.is_final_state(d2.run(['s','s','t','s','t','t','t','s','t','s','s'])))
print(d2.is_final_state(d2.run(['t','t','t','s','t','t','s','t'])))

```
