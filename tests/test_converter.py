import unittest
from src.nfa import NFA
from src.converter import Converter

class TestConverter(unittest.TestCase):
    
    def setUp(self):
        self.nfa = NFA()
        self.converter = Converter(self.nfa)
        transition_states = ['q0','q1','q2']
        alphabet = ['a','b']
        transition_rules = {
                    'q0':{
                        'a': ['q1','q2'],
                        'b':[]
                    },
                    'q1':{
                        'a':[],
                        'b':[]
                    },
                    'q2':{
                        'a':['q1','q2'],
                        'b':['q2']
                    }
                }
        starting_state = 'q0'
        final_states = ['q2']

        self.nfa.set_transition_states(transition_states)
        self.nfa.set_alphabet(alphabet)
        self.nfa.set_transition_rules(transition_rules)
        self.nfa.set_starting_state(starting_state)
        self.nfa.set_final_states(final_states)

    # def test_generate_dfa_template(self):
        
    #     expected = {
    #                 'transition_states':[],
    #                 'alphabet':self.nfa.get_alphabet(),
    #                 'transition_rules':{},
    #                 'starting_state':'',
    #                 'final_states':[]
    #             }
        
    #     actual = self.converter.get_dfa_template()
        
    #     self.assertEqual(expected, actual)

    # def test_convert_to_dfa(self):
    #     expected = {
    #         'alphabet': self.nfa.get_alphabet(),
    #         'transition_states':['q0',['q1','q2'],['\u03C6']],
    #         'starting_state':'q0',
    #         'final_states':[],
    #         'transition_rules':{
    #             'q0':{
    #                 'a':    'q1q2',
    #                 'b':    '\u03C6'
    #             },
    #             'q1q2':{
    #                 'a':    'q1q2',
    #                 'b':    'q2'
    #             },
    #             '\u03C6':{
    #                 'a':    '\u03C6',
    #                 'b':    '\u03C6'
    #             }
    #         }
    #     }
        
    #     actual = self.converter.convert_2_dfa()
        
    #     self.assertEqual(expected,actual)
