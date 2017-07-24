#Simple derivative calculator
def deri(eq,var):
    result = ''
    sign = '+-'
    while var in eq:        #Check if the variable is in the equation
        while eq != '' and any(s in sign for s in eq):     #Eventually work through the entire equation, cutting it until nothing is left in the string
            for i in reversed(eq):      #Looking through the string backwards to find a '+' or '-' sign so that we can seperate the string to only include what comes after that sign
                for j in sign:
                    if j == i:
                        temp = eq[eq.rfind(j)+1:]       #Make a temporary string containing the coefficient, variable, and exponent that appear after the sign
                        if var in temp:
                            coeff = 1
                            if temp[:temp.find(var)] != '':
                                coeff = int(temp[:temp.find(var)])
                            exp = 1
                            if temp.find('^') > -1:
                                exp = int(temp[temp.find('^')+1:])
                            if exp - 1 == 1:
                                result =  j + str(coeff*exp) + var + result
                            elif exp - 1 == 0:
                                result = j + str(coeff*exp) +  result
                            else:
                                result = j + str(coeff*exp) + var + '^' + str(exp - 1) + result
                        eq = eq[:eq.rfind(j)]#Cutting off everything past that sign to make a new equation
        if var not in eq:
            result = result[1:]
            break
        coeff = 1
        if eq[:eq.find(var)] != '':
            coeff = int(eq[:eq.find(var)])
        exp = 1
        if eq.find('^') > -1:
            exp = int(eq[eq.find('^')+1:])
        if exp - 1 == 1:
            result = str(coeff*exp) + var + result
        elif exp - 1 == 0:
            result = str(coeff*exp) + result
        else:
            result = str(coeff*exp) + var + '^' + str(exp - 1) + result
        eq = ''
    return result    

eq = str(input('What is your equation?'))
var = str(input('You are taking the derivative in respect to what variable?'))
print('The derivative is ' + deri(eq,var))

        
