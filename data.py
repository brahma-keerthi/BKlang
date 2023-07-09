class Data:
    def __init__(self):
        self.variables = {}
    
    # reads one particular variable
    def read(self, id):
        return self.variables[id]
    
    # reads all variables already existing
    def read_all(self):
        return self.variables
    
    # prints the all variables
    def write(self, variable, expression):
        variable_name = variable.value
        self.variables[variable_name] = expression