from pathlib import Path
import csv

from src.converter import Converter
from src.nfa import NFA

if __name__ == "__main__":

    # Take user input
    project_root = Path(__file__).parent.parent

    input_file_path = Path(project_root, "transitions.csv")

    with open(input_file_path, 'r') as file:
        
        transitions = csv.reader(file)

        transition_states = []
        alphabet = []
        transition_rules = {}
        starting_states = []
        final_states = []

        header = next(transitions)

        alphabet.extend(header[1:])


        for row in transitions:
            symbol_index = -1
            state = ''

            if '->' in row[0]:
                state = row[0][2:]
                starting_states.append(state)

            elif '*' in row[0]:
                state = row[0][1:]
                final_states.append(state)

            else:
                state = row[0]

            transition_states.append(state)

            transition_rules[state] = {}

            for ele in row[1:]:
                if ele == '':
                    symbol_index += 1
                    transition_rules[state][alphabet[symbol_index]] = []
                elif ele[0] == '{':
                    symbol_index += 1
                    transition_rules[state][alphabet[symbol_index]] = [ele[1:]]
                elif ele[-1] == '}':
                    transition_rules[state][alphabet[symbol_index]].append(ele[:-1])

                else:
                    symbol_index += 1
                    transition_rules[state][alphabet[symbol_index]] = [ele]


        nfa = NFA()
        nfa.set_transition_states(transition_states)
        nfa.set_alphabet(alphabet)
        nfa.set_transition_rules(transition_rules)
        nfa.set_starting_state(starting_states)
        nfa.set_final_states(final_states)

        converter = Converter(nfa)
        dfa_info = converter.convert_2_dfa()
        print(dfa_info)
