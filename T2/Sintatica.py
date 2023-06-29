from lexico import Lexico
import pandas as pd

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
    26: 'CAB->se ab_p EXP_R fc_p então',
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

var = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG')
erros = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG', True)
tabela = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG', simbolos=True)

action = pd.read_csv('D:/Aulas/Compiladores/Meus trabalhos/T2/T2/p_action.csv')
goto = pd.read_csv('D:/Aulas/Compiladores/Meus trabalhos/T2/T2/p_goto.csv')

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
    print(str(s) + ' ' + a)
    match((action.loc[s][a.lower()])[0]):
        case 'S':
            pilha.append(int(action.loc[s][a.lower()][1:]))
            a=''
            i = i + 1

        case 'R':
            AB = gramatica[int(action.loc[s][a.lower()][1:])]
            A,B = AB.split('->')
            print(pilha)
            for n in range(len(B.split(' '))):
                pilha.pop()
            print(pilha)
            print(AB + '\n')
            pilha.append(int(goto.loc[pilha[len(pilha)-1]][A]))
            

        case 'A':
            print('Aceito')
            break

        case 'E':
            if(int(action.loc[s][a.lower()][1:]) == 0):
                linha = token.loc[i-1]['Linha']
                col = token.loc[i-1]['Coluna']
                print(f'\nERRO SINTATICO - FALTA UM ";" Linha: {linha} Coluna {col} \n')
                a = 'pt_v'
                i=i-1
