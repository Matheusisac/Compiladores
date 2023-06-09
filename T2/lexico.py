import string

class Lexico:
    global numeros, letras, reservadas, estados_finais
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
    letras = list(string.ascii_letters)
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    reservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'repita', 'fimrepita', 'fim', 'inteiro', 'literal', 'real']

    def Scanner(fonte, err = False, simbolos = False):
        idlexemalist = []
        idclasselist = []
        idtipolist = []
        col = 0
        linha = 1
        estado = 0
        palavra = []
        listlinha = []
        listcol = []
        lexemalist = []
        estadolist = []
        tipolist = []
        classelist = []
        erros = []



        with open(fonte, 'r') as file:
            code = file.read()
            i = 0
            while i < len(code):
                col += 1
                palavra.append(code[i])
                if(code[i] == "\n"):
                    if(col>1):
                        linha = linha + 1
                    col = 0
                match(estado):
                    case 13:
                        if(code[i] == '='):
                            i+=1
                            estado = 14
                        elif(code[i] == '>'):
                            i+=1
                            estado = 15
                        elif(code[i] == '-'):
                            i+=1
                            estado = 16
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                    case 7:
                        if(code[i] == '"'):
                            i+=1
                            estado = 8
                        else:
                            estado = 7
                            i+=1
                    case 0:
                        if(code[i] in numeros):
                            i+=1
                            estado = 1
                        elif(code[i] in letras):
                            i+=1
                            estado = 9
                        elif(code[i] == '{'):
                            i+=1
                            estado = 10
                        elif(code[i]=='"'):
                            i+=1
                            estado = 7
                        elif(code[i]=='<'):
                            i+=1
                            estado = 13
                        elif(code[i]=='>'):
                            i+=1
                            estado = 17
                        elif(code[i]=='='):
                            i+=1
                            estado = 19
                        elif(code[i]=='('):
                            i+=1
                            estado=20
                        elif(code[i]==')'):
                            i+=1
                            estado=21
                        elif(code[i]==';'):
                            i+=1
                            estado=22
                        elif(code[i]==','):
                            i+=1
                            estado=23
                        elif(code[i]=='+' or code[i]=='-' or code[i]=='*' or code[i]=='/'):
                            i+=1
                            estado=24
                        elif(code[i]==' ' or code[i]=='\n' or code[i]=='\t'):
                            i+=1
                            estado=0
                        else:
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                            i+=1                        
                    case 2:
                        if(code[i] in numeros):
                            i+=1
                            estado = 3
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                    case 1:
                        if(code[i] in numeros):
                            i+=1
                            estado = 1
                        elif(code[i] == '.'):
                            i+=1
                            estado = 2
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                    case 3:
                        if(code[i] in numeros):
                            i+=1
                            estado = 3
                        elif(i == 'e' or i == 'E'):
                            i+=1
                            estado = 4
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []

                    case 4:
                        if(code[i] == '+' or code[i]=='-'):
                            i+=1
                            estado = 5
                        elif(code[i] in numeros):
                            i+=1
                            estado = 6
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []

                    case 5:
                        if(code[i] in numeros):
                            i+=1
                            estado = 6
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []

                    case 6:
                        if(code[i] in numeros):
                            i+=1
                            estado = 6 
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []

                    case 9:
                        if((code[i] in letras) or (code[i] == '_') or (code[i] in numeros)):
                            i+=1
                            estado = 9
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                    
                    case 10:
                        if(code[i] == '}'):
                            i+=1
                            estado = 11
                            palavra.pop()
                            palavra = []
                        else:
                            estado = 10
                            i+=1

                    case 11:
                        palavra.pop()
                        estado = 0
                        palavra = []

                    case 17:
                        if(code[i] == '='):
                            estado = 18
                            i+=1
                        else:
                            palavra.pop()
                            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                            listcol.append(col)
                            listlinha.append(linha)
                            estadolist.append(estado)
                            estado = 0
                            palavra = []
                    case 8:
                        palavra.pop()
                        lexemalist.append(''.join(palavra))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []
                    case _:
                        palavra.pop()
                        lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
                        listcol.append(col)
                        listlinha.append(linha)
                        estadolist.append(estado)
                        estado = 0
                        palavra = []

            lexemalist.append(''.join(palavra).replace('\t', '').replace('\n','').replace(' ', ''))
            listcol.append(col)
            listlinha.append(linha)
            estadolist.append(estado)

        for i in range(len(lexemalist)):
            if(lexemalist[i] in reservadas):
                classelist.append(lexemalist[i])
                tipolist.append(lexemalist[i])
            else:
                try:
                    temp = lexemalist[i]
                    if(temp in idlexemalist):
                        for n in range(len(idlexemalist)):
                            if(idlexemalist[n] == temp):
                                idclasselist[n] = estados_finais[estadolist[i]][0]
                                idtipolist[n] = estados_finais[estadolist[i]][2]
                                classelist.append(idclasselist[n])
                                tipolist.append(idtipolist[n])
                                temp = ''
                    else:
                        classelist.append(estados_finais[estadolist[i]][0])
                        tipolist.append(estados_finais[estadolist[i]][2])
                        if(estadolist[i] == 9):
                            idlexemalist.append(lexemalist[i])
                            idclasselist.append(estados_finais[estadolist[i]][0])
                            idtipolist.append(estados_finais[estadolist[i]][2])
                except:
                    erros.append(f"ERRO léxico – Caractere inválido na linguagem. Linha {listlinha[i]} e Coluna {listcol[i]}")
                    classelist.append("ERRO")
                    tipolist.append(None)


        if(simbolos == True):
            tabelaSimbolos = {
                'Classe': reservadas + idclasselist,
                'Lexema': reservadas + idlexemalist,
                'Tipo' : reservadas + idtipolist,
                'Linha' : listlinha,
                'Coluna' : listcol
            }
            return tabelaSimbolos

        if(err == False):
            Token = {
                'Classe': classelist,
                'Lexema': lexemalist,
                'Tipo': tipolist,
                'Linha' : listlinha,
                'Coluna' : listcol
            }
            return Token
        else:
            return erros
