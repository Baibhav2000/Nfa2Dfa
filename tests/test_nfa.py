import unittest
from src.nfa import NFA


class TestNfa(unittest.TestCase):
    def setUp(self):
        self.transition_states = ['A','B','C']
        self.alphabet = ['a','b']
        self.transition_rules = {
                    'A':{
                        'a':['B'],
                        'b':['C']
                    },
                    'B':{
                        'a':[],
                        'b':['C']
                    },
                    'C':{
                        'a':[],
                        'b':[]
                    }
                }
        self.starting_state = 'A'
        self.final_states = ['C']

        self.nfa = NFA()
        self.nfa.set_transition_states(self.transition_states)
        self.nfa.set_alphabet(self.alphabet)
        self.nfa.set_transition_rules(self.transition_rules)
        self.nfa.set_starting_state(self.starting_state)
        self.nfa.set_final_states(self.final_states)

    def test_get_nfa_info(self):
        expected = {
                    'transition_states' :   self.transition_states,
                    'alphabet'          :   self.alphabet,
                    'transition_rules'  :   self.transition_rules,
                    'starting_state'    :   self.starting_state,
                    'final_states'      :   self.final_states
                }

        actual = self.nfa.get_nfa_info()

        self.assertEqual(expected,actual)


