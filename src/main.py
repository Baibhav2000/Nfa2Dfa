from src.converter import Converter
from src.nfa import NFA

if __name__ == "__main__":
    nfa = NFA()
    nfa.set_transition_states(['q0','q1','q2'])
    nfa.set_alphabet(['a','b'])
    nfa.set_transition_rules({
            'q0':{
                'a':['q0'],
                'b':['q0','q1']
            },
            'q1':{
                'a':[],
                'b':['q2']
            },
            'q2':{
                'a':[],
                'b':[]
            }
        })

    nfa.set_starting_state(['q0'])
    nfa.set_final_states(['q2'])
    converter = Converter(nfa)
    dfa_info = converter.convert_2_dfa()
