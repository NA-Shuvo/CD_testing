

class DFA:

    def __init__(self, /, A, Q, s, F, T = None):
        self.A = A
        self.Q = Q
        self.s = s
        self.F = F

        self.transition_table = dict()

        for q in Q:
            temp = dict()
            for a in A:
                temp[a] = None
            self.transition_table[q] = temp 
        
        if T != None:
            for t in T:
                self.transition_table[t[0]][t[1]] = t[2]

    def clear_transition_table(self):
        for q in self.Q:
            temp = dict()
            for a in self.A:
                temp[a] = None
            self.transition_table[q] = temp 
        
    def update_transition_table(self, T):
        for t in T:
            self.transition_table[t[0]][t[1]] = t[2]

    def sigma(self, q, a):
        return self.transition_table[q][a]

    def run(self, input):
        i = 0
        input_size = input.__len__()
        current_state = self.s
        
        while i<input_size:
            next_state = self.transition_table[current_state][input[i]]
            current_state = next_state
            i += 1
        
        return next_state

    def is_final_state(self, input_state):
        return (input_state in self.F)

    def __str__(self):
        print("Alphabet: ", str(self.A))
        print("States: ", str(self.Q))
        print("Start state: ", self.s)
        print("Final states: ", str(self.F))
        print("Transition table: ", str(self.transition_table))
        return ""

            





        
