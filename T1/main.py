import os
import string
import pandas as pd

col = 0
linha = 0
estado = 0
palavra = []
listlinha = []
listcol = []
lexemalist = []
estadolist = []
tipolist = []
classelist = []
erros = []

estados_finais = {
    1: ('Num', None, 'inteiro'),
    3: ('Num', None, 'real'),
    6: ('Num', None, 'real'),
    8: ('Lit', None, None),
    9: ('id', None, None),
    11: ('comentario', None, None),
    12: ('EOF', None, None),
    13: ('OPR', None, None),
    14: ('OPR', None, None),
    15: ('OPR', None, None),
    16: ('RCB', None, None),
    17: ('OPR', None, None),
    18: ('OPR', None, None),
    19: ('OPR', None, None),
    20: ('AB_P', None, None),
    21: ('FC_P', None, None),
    22: ('PT_V', None, None),
    23: ('VIR', None, None),
    24: ('OPM', None, None),
}
tabela = pd.DataFrame(columns=['Classe', 'Lexema', 'Tipo'])
path_arquivo_fonte = os.path.join(os.path.dirname(__file__), 'FONTE.ALG')

arquivo_fonte = open(path_arquivo_fonte, mode='r', encoding='utf-8')

letras = list(string.ascii_letters)
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
reservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'Repita', 'fimRepita', 'fim', 'inteiro', 'literal', 'real']


#Scanner
with open('D:/Compiladores-main/Compiladores-main/T1/FONTE.ALG', 'r') as file:
            code = file.read()
            state = 0
            i = 0
            while i < len(code):
                char = code[i]
                col += 1
                palavra.append(code[i])
                if(code[i] == '\n'):
                    col = 0
                    linha += 1

                if(estado == 7):
                    if(code[i] == '"'):
                        estado = 8
                    else:
                        estado = 7

                if(estado==0):
                    if(code[i] in numeros):
                        estado = 1
                    elif(code[i] in letras):
                        estado = 9
                    elif(code[i] == '{'):
                        estado = 10
                    elif(code[i]=='"'):
                        estado = 7
                    elif(code[i]=='<'):
                        estado = 13
                    elif(code[i]=='>'):
                        estado = 17
                    elif(code[i]=='='):
                        estado = 19
                    elif(code[i]=='('):
                        estado=20
                    elif(code[i]==')'):
                        estado=21
                    elif(code[i]==';'):
                        estado=22
                    elif(code[i]==','):
                        estado=23
                    elif(code[i]=='+' or code[i]=='-' or code[i]=='*' or code[i]=='/'):
                        estado=24
                    elif(code[i]==' ' or code[i]=='\n' or code[i]=='\t'):
                        estado=0
                    else:
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                if(estado==1):
                    if(code[i] in numeros):
                        estado = 1
                    elif(code[i] == '.'):
                        estado = 2
                    else:
                        i=i-1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                if(estado == 2):
                    if(code[i] in numeros):
                        estado = 3
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                if(estado == 3):
                    if(code[i] in numeros):
                        estado = 3
                    elif(i == 'e' or i == 'E'):
                        estado = 4
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                if(estado == 4):
                    if(code[i] == '+' or code[i]=='-'):
                        estado = 5
                    elif(code[i] in numeros):
                        estado = 6
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []

                if(estado == 5):
                    if(code[i] in numeros):
                        estado = 6
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                if(estado == 6):
                    if(code[i] in numeros):
                        estado = 6 
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []

                if(estado == 9):
                    if(code[i] in letras):
                        estado = 9
                    else:
                        i = i - 1
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                
                if(estado==10):
                    if(code[i] == '}'):
                        estado = 11
                    else:
                        estado = 10
                
                if(estado==17):
                    if(code[i] == '='):
                        estado = 18
                    else:
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                
                if(estado==8 or estado==11 or estado==14 or estado==15 or estado==16 or estado==18 or estado==19 or estado==20 or estado==21 or estado==22 or estado==23 or estado==24):
                    lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                    listcol.append(col)
                    listlinha.append(linha)
                    estadolist.append(estado)
                    estado = 0
                    palavra = []
                i+=1
            estadolist.append(12)
            lexemalist.append('EOF')
            listcol.append(col)
            listlinha.append(linha)
for i in range(len(lexemalist)):
    if(lexemalist[i] in reservadas):
        classelist.append(lexemalist[i])
        tipolist. append(lexemalist[i])
    else:
        try:
            classelist.append(estados_finais[estadolist[i]][0])
            tipolist.append(estados_finais[estadolist[i]][2])
        except:
            erros.append(f"Erro lexico na linha {listlinha[i]} e coluna {listcol[i]}")
            classelist.append("ERRO")
            tipolist.append("None")

Token = {
    'Classe': classelist,
    'Lexema': lexemalist,
    'Tipo': tipolist 
}
tabela = pd.DataFrame(Token)

print(tabela)
print(erros)
