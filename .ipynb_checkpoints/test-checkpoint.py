import math

variables = {}
functions = ('add', 'sub', 'mul', 'div', 'pow', 'gcd', 'log')

def is_input_value_valid(variable):
    if variable.isdigit():
        return True
    elif variable.replace('_','').isalpha():
        return True
    return False

output = ''

def is_a_valid_function(value):
        global output
        try:
                # print('read-1')
                function, second = value.split('(')
                # print('read-2',second.split(')')[0])
                val1, val2 = second.split(')')[0].split(',')
                if(not function in functions):
                    output = 'function not found'
                    return False
                else:
                    if is_input_value_valid(val1)  :
                        var1 = variables.get(val1)
                        
                        if var1 == None and val1.isdigit() == False:
                            output = 'variable error'
                            return False
                    elif val1.isdigit() == False:
                        output = 'val is not a number'
                        return False
                    

                    if is_input_value_valid(val2) :
                        var2 = variables.get(val2)
                        if var2 == None and val2.isdigit() == False:
                            output = 'variable error'
                            return False
                    elif val2.isdigit() == False:
                        output = 'val is not a number'
                        return False

                    return val1,val2,function

        except Exception as e:
            return False
    
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

            print('output: ', output,' result', result, ' variable: ', value.isdigit())
            if  result != False:
                val1, val2, operation = result
                if val1.isalpha():
                    val1 = variables[val1]
                if val2.isalpha():
                    val2 = variables[val2]

                val1 = int(val1)
                val2 = int(val2)

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
            # ************************************************ variable assignment
            elif output == '':                   
                if is_input_value_valid(variable) and not variable.isdigit():
                    if is_input_value_valid(value):
                        if value.isdigit():
                            # print('readx ', value)
                            variables[variable] = value
                        else:
                            # print('ready')
                            variables[variable] = variables[value]
                    else:
                        print("val is not a number")
                    
                else:
                    print('variable error')
            else:
                print(output)        