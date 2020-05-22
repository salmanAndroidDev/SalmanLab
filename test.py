import math

variables = {}
functions = ('add', 'sub', 'mul', 'div', 'pow', 'gcd', 'log')

def is_input_value_valid(variable):
    if variable.isdigit():
        return True
    elif variable.replace('_','').isalpha():
        return True
    return False

def is_a_valid_function(value):
        try:
                # print('read-1')
                function, second = value.split('(')
                # print('read-2',second.split(')')[0])
                val1, val2 = second.split(')')[0].split(',')
                if(not function in functions):
                    print('function not found')
                    return False
                else:
                    print('val1: ', type(val1), ' val2: ', type(val2), ' operation: ', function)
                    if is_input_value_valid(val1)  :
                        var1 = variables.get(val1)
                        
                        if var1 == None and val1.isdigit() == False:
                            print('variable error1')
                            return False
                    elif val1.isdigit() == False:
                        print('val is not a number****')
                        return False
                    print('reads between')       
                    if is_input_value_valid(val2) :
                        var2 = variables.get(val2)
                        print('read2')
                        
                        if var2 == None and val2.isdigit() == False:
                            print('variable error2')
                            return False
                    elif val2.isdigit() == False:
                        print('val is not a number====')
                        return False

                    return val1,val2,function

        except Exception as e:
            print(e)
            return False 
    

output = ''
while True:
    command = input().replace(' ','').split(':=')   
    

    if('end' in command):
        break

    variable = command[0]

    if len(command) == 1:
            output = variables.get(variable)

            if output == None:
                output = "variable not found"
                
            print(output)    
       
    else:
            value = command[1]
            
            result = is_a_valid_function(value)
            
            if  result != False:
                val1, val2, operation = result

                print('aval1: ', val1, ' val2: ', val2, operation)
            
            # ************************************************ variable assignment
            
            else:                   
                if is_input_value_valid(variable) and not variable.isdigit():
                    if is_input_value_valid(value):
                        if value.isdigit():
                            print('readx ', value)
                            variables[variable] = value
                        else:
                            print('ready')
                            variables[variable] = variables[value]
                    else:
                        print("val is not a number")
                    
                else:
                    print('variable error')        