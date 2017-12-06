class Action:

    def __init__ (self, parameters, pre_cond, effect):
        self.parameters = parameters
        self.pre_cond = pre_cond
        self.effect = effect
        self.name = ''

    def __hash__ (self):
        return hash(str(self.pre_cond) + str(self.effect))
    
    def __repr__(self):
    	return str(self.pre_cond) + str(self.effect)

    def __eq__(self, other):
        return str(self) == str(other)