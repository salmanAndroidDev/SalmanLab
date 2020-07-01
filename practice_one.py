import re, math

variables = dict()
functions = ('add', 'sub', 'mul', 'div', 'pow', 'gcd', 'log')

def do_operation(variable, operation, val1, val2):
    if(operation == 'add'):
        variables[variable] = val1 + val2
    elif(operation == 'sub'):
        variables[variable] = val1 - val2
    elif(operation == 'mul'):    
        variables[variable] = val1 * val2
    elif(operation == 'div'):    
        variables[variable] = val1 / val2
    elif(operation == 'pow'):    
        variables[variable] = val1 ** val2
    elif(operation == 'gcd'):    
        variables[variable] =  math.gcd(val1, val2)
    elif(operation == 'log'):    
        variables[variable] = math.log(val1, val2)

def is_function(command):
    fun_pattern = re.compile(r'\w+\(\w+,\w+\)')
    result = fun_pattern.search(command)

    if result == None:
        return False
    return True    

def get_function_values(command):
    pattern = re.compile(r'(\w+)\((\w+),(\w+)\)')
    result = pattern.findall(command)

    return result[0]

def is_variable(command):
    variable_pattern = re.compile(r'\w+[^\(\)]')
    result = variable_pattern.search(command)
    if result == None or result.group() != command:
        return False
    return True

def variable_is_defined(var):
    if var in variables: return True
    else: return False

def is_valid_number(var):
    variable_pattern = re.compile(r'(\d+(\.)?\d+)')
    result = variable_pattern.search(command)
    
    if result != None and result.group() == var :
        return True
    return False    

def starts_with_number(var):
    pattern = re.compile(r'\d+\w+')
    result = pattern.search(var)
    
    return result

while True:
    command = input()
    chunck_command = command.split(':=')
    var = chunck_command[0].strip()

        # print if variale is called and is already defined
    if len(chunck_command) == 1:
        if variable_is_defined(var):
            print(variables.get(var))
        else:
            print('variable not found')
    
    elif is_function(chunck_command[1].strip()):
        function = chunck_command[1].strip()
        func_name, x , y = get_function_values(function)        
        
        if func_name in functions:
            
            # fixing value for x
            if is_valid_number(x):
                x = float(x)

            elif starts_with_number(x):
                print('val is not a number')

            elif variable_is_defined(x):
                x = variables.get(x)
            else:
                print('variable error')

            #fixing value for y
            if is_valid_number(y):
                y = float(y)

            elif starts_with_number(y):
                print('val is not a number')

            elif variable_is_defined(y):
                y = variables.get(x)
            else:
                print('variable error')
            

            do_operation(var, func_name, x, y)
        else:
            print('function not found')


    else:
        value = chunck_command[1].strip()    

        if is_valid_number(value):
            variables[var] = float(value)

        elif starts_with_number(value):
            print('val is not a number')

        elif variable_is_defined(value):
            variables[var] = variables.get(value)

        else:
            print('variable error')


        print('...........')
        print(variables)
        print('...........')

