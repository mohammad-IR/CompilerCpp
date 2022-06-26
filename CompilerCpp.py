import code
import keyword
from operator import add


def read_file(file_address):
    file = open(file_address)
    syntax = file.read()
    file.close()
    return syntax     

def get_grammar_tokens(inpput_text):
    keywords = [inpput_text[0][0]]
    keywords += inpput_text[0][1:].split('\'')
    keywords = list(filter(lambda keyword: (keyword != '\n' and keyword != ";\n") and keyword != "\t",keywords))
    opreations = list(filter(lambda keyword: keyword.find("\\") >= 0, keywords))

    keywords = list(filter(lambda keyword: keyword.find("\\") == -1, keywords))
    opreations = list((i.replace("\\", "") )  for i in opreations )
    opreations += list(f"""\{i}""" for i in opreations[0].split("|"))[1:]
    opreations = opreations[1:]
    return  [keywords, opreations]                                
def tokenizer(addres_code, keywords, opreations):
    syntax = read_file(addres_code)
    for i in syntax.split():
        if i in opreations:
            pass
        elif i in keywords:
            pass
        else:
            pass
         


address_grammer = 'files_syntax/c++Grammer.txt'
syntax = read_file(address_grammer).split('##')
keywords, opreations = get_grammar_tokens(syntax)
address_code = 'code/helloWorld.cpp'

print(f"keywords : {keywords} \nopreations :{opreations}")