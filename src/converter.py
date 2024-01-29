from collections import deque

class Converter():
    def __init__(self, nfa):
        self.nfa_info = nfa.get_nfa_info()
        
    # Data strcuture for implementing
    # Deterministic Finite Automaton
    def get_dfa_template(self):
        dfa_info = {}

        dfa_info['alphabet'] = self.nfa_info['alphabet']
        dfa_info['transition_states'] = []
        dfa_info['transition_rules'] = {}
        dfa_info['starting_states'] = ''
        dfa_info['final_states'] = []

        return dfa_info
        
    # Go to the next state
    def get_next_state(self, states, symbol):
        # If the current state is dead state state
        if states == '\u03C6':
            return '\u03C6'

        next_state = []
        
        rules = self.nfa_info['transition_rules']

        for state in states:
            next_state += rules[state][symbol]

        next_state = list(set(next_state))
        next_state.sort()

        return next_state if next_state else '\u03C6'

    # Convert the NFA to DFA
    def convert_2_dfa(self):
        starting_state = self.nfa_info['starting_state']
        
        dfa_info = self.get_dfa_template()
        dfa_info['starting_states'] = starting_state
        queue = deque()
        queue.append(starting_state)
        dfa_info['transition_states'].append(''.join(queue[0]))
        
        alphabet = dfa_info['alphabet']

        while queue:
            curr_state = queue[0]
            curr = ''.join(curr_state)
            dfa_info['transition_rules'][''.join(curr_state)] = {}
            for symbol in alphabet:
                
                next_state = self.get_next_state(curr_state, symbol)
                nxt = ''.join(next_state)
                dfa_info['transition_rules'][curr][symbol] = nxt
                
                if nxt not in dfa_info['transition_states']:
                    dfa_info['transition_states'].append(nxt)
                    queue.append(next_state)
                
                if set(next_state).intersection(set(self.nfa_info['final_states'])):
                    if nxt not in dfa_info['final_states']:
                        dfa_info['final_states'].append(nxt)
                
            queue.popleft()        
        
        return dfa_info    
