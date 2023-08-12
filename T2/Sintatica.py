from lexico import Lexico
from Semantico import Semantico
import pandas as pd


with open('obj.c', "w") as file:
    file.truncate(0)
    file.write("""#include<stdio.h>\n
typedef char literal[256]\n
void main(void){\n""")
gramatica = {
    1: "P'->P",
    2: "P->inicio V A",
    3: "V->varincio LV",
    4: "LV->D LV",
    5: "LV->varfim pt_v",
    6: "D->TIPO L pt_v",
    7: "L->id vir L",
    8: "L->id",
    9: "TIPO->inteiro",
    10: "TIPO->real",
    11: "TIPO->literal",
    12: "A->ES A",
    13: 'ES->leia id pt_v',
    14: 'ES->escreva ARG pt_v',
    15: 'ARG->lit',
    16: 'ARG->num',
    17: 'ARG->id',
    18: 'A->CMD A',
    19: 'CMD->id rcb LD pt_v',
    20: 'LD->OPRD opm OPRD',
    21: 'LD->OPRD',
    22: 'OPRD->id',
    23: 'OPRD->num',
    24: 'A->COND A',
    25: 'COND->CAB CP',
    26: 'CAB->se ab_p EXP_R fc_p entao',
    27: 'EXP_R->OPRD opr OPRD',
    28: 'CP->ES CP',
    29: 'CP->CMD CP',
    30: 'CP->COND CP',
    31: 'CP->fimse',
    32: 'A->R A',
    33: 'R->CABR CPR',
    34: 'CABR->repita ab_p EXP_R fc_p',
    35: 'CPR->ES CPR',
    36: 'CPR->CMD CPR',
    37: 'CPR->COND CPR',
    38: 'CPR->fimrepita',
    39: 'A->fim'
}
erro=0
var = Lexico.Scanner('D:/Aulas/Compiladores/Compiladores-main/T2/FONTE.ALG')
erros = Lexico.Scanner('D:/Aulas/Compiladores/Compiladores-main/T2/FONTE.ALG', True)
tabela = []
n=0
action = pd.read_csv('D:/Aulas/Compiladores/Compiladores-main/T2/p_action.csv')
goto = pd.read_csv('D:/Aulas/Compiladores/Compiladores-main/T2/p_goto.csv')
j=0
token = pd.DataFrame(var)
i = 0
pilha = [0]
a = ''
while(True):
    s = pilha[len(pilha)-1]
    if(a == ''):
        try:
            a = token.loc[i]['Classe']
        except:
            a = 'eof'
    if(a == "ERRO"):
        erro = 1
        print("\n" + erros[j]+ "\n")
        j=j+1
        i=i+1
        a=''
    else:
        match((action.loc[s][a.lower()])[0]):

            case 'S':
                pilha.append(int(action.loc[s][a.lower()][1:]))
                a=''
                i = i + 1

            case 'R':
                AB = gramatica[int(action.loc[s][a.lower()][1:])]
                A,B = AB.split('->')
                for n in range(len(B.split(' '))):
                    pilha.pop()
                print(AB + '\n')
                pilha.append(int(goto.loc[pilha[len(pilha)-1]][A]))
                if(AB == "LV->varfim pt_v" or A == "TIPO" or A == "L"):
                    tabela = Semantico.leitura(AB,"obj.c", i, tabela, token.loc[i-1]['Linha'], token.loc[i-1]['Coluna'])
                else:
                    Semantico.leitura(AB,"obj.c", i, tabela, token.loc[i-1]['Linha'], token.loc[i-1]['Coluna'])
                n = n+1
                

            case 'A':
                if erro == 0:
                    print('Aceito')
                else:
                    print('Com erro Sintatico')
                break

            case 'E':
                erro = 1
                if(int(action.loc[s][a.lower()][1:]) == 0):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM ";" Linha: {linha} Coluna {col} \n')
                    a = 'pt_v'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 1):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM ")" Linha: {linha} Coluna {col} \n')
                    a = 'fc_p'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 2):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM identificador Linha: {linha} Coluna {col} \n')
                    a = 'id'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 3):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM Argumento(literal, numeral ou identificador) Linha: {linha} Coluna {col} \n')
                    a = 'lit'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 4):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM Operando Linha: {linha} Coluna {col} \n')
                    a = 'id'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 5):
                    linha = token.loc[i]['Linha']
                    col = token.loc[i]['Coluna']
                    print(f'\nERRO SINTATICO - Codigo tem que iniciar com "inicio" Linha: {linha} Coluna {col} \n')
                    a = 'inicio'
                    i=i+1
                
                elif(int(action.loc[s][a.lower()][1:]) == 6):
                    linha = token.loc[i]['Linha']
                    col = token.loc[i]['Coluna']
                    print(f'\nERRO SINTATICO - Esperando um "varinicio" Linha: {linha} Coluna {col} \n')
                    a = 'varinicio'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 7):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - O codigo está finalizado no fim Linha: {linha} Coluna {col} \n')
                    a = 'eof'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 8):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Precisa-se declarar um TIPO Linha: {linha} Coluna {col} \n')
                    a = 'literal'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 9):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "fim" Linha: {linha} Coluna {col} \n')
                    a = 'fim'
                    i=i+1
                
                elif(int(action.loc[s][a.lower()][1:]) == 10):
                    linha = token.loc[i]['Linha']
                    col = token.loc[i]['Coluna']
                    print(f'\nERRO SINTATICO - Erro inesperado Linha: {linha} Coluna {col} \n')
                    a=''
                    i=i+1

                elif(int(action.loc[s][a.lower()][1:]) == 11):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "fimrepita" Linha: {linha} Coluna {col} \n')
                    a = 'fimrepita'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 12):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "fimse" Linha: {linha} Coluna {col} \n')
                    a = 'fimse'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 13):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "entao" Linha: {linha} Coluna {col} \n')
                    a = 'entao'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 14):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "opm" Linha: {linha} Coluna {col} \n')
                    a = 'opm'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 15):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Não foi encontrado o "rcb" Linha: {linha} Coluna {col} \n')
                    a = 'rcb'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 16):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Em vez de um operador, é um receba Linha: {linha} Coluna {col} \n')
                    a = 'rcb'

                elif(int(action.loc[s][a.lower()][1:]) == 17):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Falta uma virgula Linha: {linha} Coluna {col} \n')
                    a = 'vir'
                    i=i-1

                elif(int(action.loc[s][a.lower()][1:]) == 18):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Falta o TIPO Linha: {linha} Coluna {col} \n')
                    a = 'real'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 19):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Era pra ser um id Linha: {linha} Coluna {col} \n')
                    a = 'id'
                
                elif(int(action.loc[s][a.lower()][1:]) == 20):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM "(" Linha: {linha} Coluna {col} \n')
                    a = 'ab_p'
                    i=i-1
                
                elif(int(action.loc[s][a.lower()][1:]) == 21):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Era pra ser um Argumento Linha: {linha} Coluna {col} \n')
                    a = 'id'
                
                elif(int(action.loc[s][a.lower()][1:]) == 22):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - Era pra ser um Identificador Linha: {linha} Coluna {col} \n')
                    a = 'id'
                
                elif(int(action.loc[s][a.lower()][1:]) == 23):
                    linha = token.loc[i-1]['Linha']
                    col = token.loc[i-1]['Coluna']
                    print(f'\nERRO SINTATICO - FALTA UM "escreva" Linha: {linha} Coluna {col} \n')
                    a = 'escreva'
                    i=i-1
