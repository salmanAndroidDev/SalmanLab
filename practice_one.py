import re

variables = {}

def is_function(command):
    fun_pattern = re.compile(r'\w+\(\w+,\w+\)')
    result = fun_pattern.search(command)

    if result == None:
        return False
    return True    

def is_variable(command):
    variable_pattern = re.compile(r'\w+[^\(\)]')
    result = variable_pattern.search(command)
    if result == None or result.group() != command:
        return False
    return True

def variable_is_defined(var):
    if var in variables: return True
    else: return False



command = input()

chunck_command = command.split()
var = chunck_command[0]

# print if variale is called and is already defined
if len(chunck_command) == 1:
    if variable_is_defined(var):
        print(variables.get(var))
    else:
        print('variable not found')



