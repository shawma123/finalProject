class Automata():

    def __init__(self, X, E, theta, x0):
        self.X = X
        self.E = E
        self.theta = theta
        self.x0 = x0

    def f(self, x, e):
        new_state = []
        for item in self.theta:
            if x == item[0] and e == item[1]:
                new_state.append(item[2])
        return new_state

    def f_sets(self, S, e):
        results = []
        for s in S:
            one = self.f(s, e)
            for o in one:
                results.append(o)
        return transferToSets(results)

    def hasOutput(self, S):
        for s in S:
            for e in self.E:
                if self.f(s, e) != []:
                    return True
        return False

class process_file_data:
    # preprocess data: removal of new line, spaces, tabs and comments from data file
    def preprocess_data(self,data):
        data = data.split(';')
        data_arr = list()
        for word in data:
            word_to = ""
            i=0
            while i < len(word):
                if word[i] == '\n' or word[i] == '\t' or word[i] == ' ':
                    i = i + 1
                elif word[i] == '#':
                    i = i + 1
                    while word[i] != '\n':
                        i = i + 1
                else:
                    word_to = word_to + word[i]
                    i = i + 1
            data_arr.append(word_to)
        return self.process_data(data_arr)
    #process input to get data and check if valid
    def process_data(self,data_arr):
        operation = operations()
        for word in data_arr:
            if '->' in word:
                process = word.split('->')
                if(process[0] == 'states'):
                    states = self.check_data(process[1],process[0])
                elif(process[0] == 'alphabet'):
                    alphabet = self.check_data(process[1],process[0])
                elif(process[0] == 'accept_states'):
                    accept_states = self.check_data(process[1],process[0])
                elif(process[0] == 'start_state'):
                    start_state = self.check_data(process[1],process[0])
                elif(process[0] == 'transition'):
                    transition = self.check_data(process[1],process[0])
                else:
                    operation.error_msg("illegal DFA tuple declaration: %s"%process[0])
            else:
                pass
        return states,alphabet,accept_states,start_state,transition
    def check_data(self,data,type):
        data_arr = list()
        operation = operations()
        if(type == "states" or type == "accept_states"):
            data = data.split(',')
            # limit states to 3
            if len(data) > 4:
                operation.error_msg("number of states must be less than 5 ")
            for token in data:
                if re.match('^[0-9]',token):
                    data_arr.append(int(token))
                else:
                    operation.error_msg("%s must be an integer"%type)
        elif(type == "start_state"):
            data_arr = int(data)
        elif(type == "alphabet"):
            data = data.split(',')
            for token in data:
                if re.match('^[A-Z,a-z]',token):
                    data_arr.append(str(token))
                else:
                    operation.error_msg("%s must be an alphabet"%type)
        elif(type == "transition"):
            data_arr = dict()
            #split transition data
            data = data.split(':')
            data_list = list()
            for transition in data:
                #split transition data using ',' to get initialize data
                transition_list = list()
                transition = transition.split(',')
                for transition_data in transition:
                    #split again to seperate name and value
                    transition_data = transition_data.split('=')
                    transition_data_list= list()
                    for transition_data_value_name in transition_data:
                        #turn name and value into array to check for errors and eliminate some characters
                        transition_data_value_name_map = map(str,transition_data_value_name)
                        array_token_list = ""
                        if '{' in transition_data_value_name_map or '}' in transition_data_value_name_map:
                            array_token = ""
                            for transition_data_value_name_array in transition_data_value_name_map:
                                if(transition_data_value_name_array == '{' or transition_data_value_name_array == '}'):
                                    pass
                                else:
                                    array_token = array_token + transition_data_value_name_array
                            array_token_list = array_token_list + array_token
                        else:
                            array_token_list =array_token_list + transition_data_value_name
                        transition_data_list.append(array_token_list)
                    transition_list.append(transition_data_list)
                data_list.append(transition_list)
            #build dict to create transition function
            for word in data_list:
                initial = word[0][1]
                value = word[1][1]
                target = word[2][1]
                data_arr[(int(initial),value)] = int(target);

        return data_arr

class AutomataPlus:
    def __init__(self, states, alphabet, transition_function, start_state):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
    def f(self, x, e):
        new_state = []
        for item in self.theta:
            if x == item[0] and e == item[1]:
                new_state.append(item[2])
        return new_state

    def f_sets(self, S, e):
        results = []
        for s in S:
            one = self.f(s, e)
            for o in one:
                results.append(o)
        return transferToSets(results)

    def hasOutput(self, S):
        for s in S:
            for e in self.E:
                if self.f(s, e) != []:
                    return True
        return False