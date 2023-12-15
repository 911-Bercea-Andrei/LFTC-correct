class FA:
    def __init__(self, filename):
        self.states = []
        self.alphabet = []
        self.transition = {}
        self.initial_state = ""
        self.final_states = []
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename) as f:
            self.states = f.readline().strip().replace(" ", "").split(",")
            self.alphabet = f.readline().strip().replace(" ", "").split(",")
            self.initial_state = f.readline().strip()
            self.final_states = f.readline().strip().replace(" ", "").split(",")

            for read_line in f:
                line = read_line.strip().replace(" ", "").split(",")
                pair = line[:-1]
                if len(pair) < 2 or len(line) == 0:
                    raise RuntimeError("Error while parsing transition functions")
                self.transition.setdefault(tuple(pair), []).append(line[-1])


    def deterministic(self):
        return False if any([elem for elem in self.transition.values() if len(elem) > 1]) else True

    def check_sequence(self, sequence):
        if self.deterministic():
            state = self.initial_state
            for symbol in sequence:
                transition_key = (state, symbol)
                # print(f"Transition key: {transition_key}")
                if transition_key not in self.transition.keys():
                    # print("No transition defined for key.")
                    return False
                next_states = self.transition[transition_key]
                # print(f"Next states: {next_states}")
                state = next_states[0]
            return state in self.final_states
        return False

    def is_identifier(self, token):
        return self.check_sequence(token) and 'q1' in self.final_states

    def is_integer_constant(self, token):
        return self.check_sequence(token) and ('q2' in self.final_states or 'q3' in self.final_states)

    def __repr__(self):
        return " States: " + str(self.states) + "\n Alphabet: " + str(
            self.alphabet) + "\n Transition Functions: " + str(
            self.transition) + "\n Initial state: " + self.initial_state + "\n Final states: " + str(self.final_states)