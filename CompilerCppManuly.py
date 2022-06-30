
from symtable import Symbol
from tkinter import W


opreator = ['!', '*', '+', '-', '/', '%', '^', '+=', '-=', '++', '<', '<=', '>', '>=', '=', '==', '!='
            , '||', '&&', '~','[', ']', '{', '}', '(', ')', ',', ';', '<<<', '>>>', '>>', '<<', '#']
x = ['\n', '\t', '\r', ' ']
keywords = [ 'main', 'id', 'num', 'string', 'character', 'int', 'char', 'float', 'double', 'void', 'cin', 'cout', 
    'while', 'for', 'if', 'else', 'break', 'return'] 
numbers = [1,2,3,4,5,6,7,8,9,0]

def read_file(file_address):
    file = open(file_address)
    syntax = file.read()
    file.close()
    return syntax     

def tokenizer(addres_code, keywords, opreations):

    syntax = read_file(addres_code)
    iterateNumber = 0
    states = []
    state = ''
    while len(syntax) > iterateNumber:
        if syntax[iterateNumber] == "\"":
            iterateNumber += 1
            while True:
                state += syntax[iterateNumber]
                if syntax[iterateNumber] == "\"":
                    iterateNumber += 1
                    states.append(("value", state))
                    state = ""
                    break
                
        if syntax[iterateNumber] == "\\":
            iterateNumber += 1
            while True:
                iterateNumber+= 1
                if syntax[iterateNumber] == "\n":
                    iterateNumber += 1
                    break
  
        if state in opreations:
            while True:
                if (state + syntax[iterateNumber]) in opreations:
                    state += syntax[iterateNumber]
                    iterateNumber += 1
                    continue
                else:
                    break 
            states.append(('opreation', state))
            state = ''
        elif state in keywords and (syntax[iterateNumber] == ' ' or syntax[iterateNumber] in x or syntax[iterateNumber] in opreations):
            states.append(('keyword', state))
            state = ''
        elif (syntax[iterateNumber] == ' ' or syntax[iterateNumber] in opreations) and state != '':
            states.append(('identifier', state))
            state = ''
        if syntax[iterateNumber] not in x:
            state += syntax[iterateNumber]
        

        iterateNumber += 1
    return states

address_code = 'code/helloWorld.cpp'
print(tokenizer(address_code, keywords=keywords, opreations=opreator))