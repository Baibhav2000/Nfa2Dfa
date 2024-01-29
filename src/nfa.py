class NFA():
	def __init__(self):
		self.transition_states = []
		self.alphabet = []
		self.transition_rules = {}
		self.starting_state = []
		self.final_states = []

	def set_transition_states(self, transition_states):
		self.transition_states = transition_states

	def set_alphabet(self, alphabet):
		self.alphabet = alphabet

	def set_transition_rules(self, transition_rules):
		self.transition_rules = transition_rules

	def set_starting_state(self, starting_state):
		self.starting_state = starting_state

	def set_final_states(self, final_states):
		self.final_states = final_states

	def get_transition_states(self):
		return self.transition_states

	def get_alphabet(self):
		return self.alphabet

	def get_transition_rules(self):
		return self.transition_rules

	def get_starting_state(self):
		return self.starting_state

	def get_final_states(self):
		return self.final_states

	def get_nfa_info(self):
		info = {}
		info['transition_states'] = self.get_transition_states()
		info['alphabet'] = self.get_alphabet()
		info['transition_rules'] = self.get_transition_rules()
		info['starting_state'] = self.get_starting_state()
		info['final_states'] = self.get_final_states()

		return info



