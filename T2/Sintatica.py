from lexico import Lexico
import pandas as pd

gramatica = {
    1: 'P->P',
    2: 'P->inicio V A',
    3: 'V->varinicio LV',
    4: 'LV->D LV',
    5: 'LV->varfim pt_v',
    6: 'D->TIPO L pt_v',
    7: 'L->id vir L',
    8: 'L->id',
    9: 'TIPO->inteiro',
    10: 'TIPO->real',
    11: 'TIPO->literal',
    12: 'A-> ES A',
    13: 'ES-> leia id pt_v',
    14: 'ES-> escreva ARG pt_v',
    15: 'ARG-> lit',
    16: 'ARG-> num',
    17: 'ARG-> id',
    18: 'A-> CMD A',
    19: 'CMD-> id atr LD pt_v',
    20: 'LD-> OPRD opm OPRD',
    21: 'LD-> OPRD',
    22: 'OPRD-> id',
    23: 'OPRD-> num',
    24: 'A-> COND A',
    25: 'COND-> CAB CP',
    26: 'CAB-> se ab_p EXP_R fc_p então',
    27: 'EXP_R-> OPRD opr OPRD',
    28: 'CP-> ES CP',
    29: 'CP-> CMD CP',
    30: 'CP-> COND CP',
    31: 'CP-> fimse',
    32: 'A-> RA',
    33: 'R-> CABR CPR',
    34: 'CABR -> repita ab_p EXP_R fc_p',
    35: 'CPR-> ES CPR',
    36: 'CPR-> CMD CPR',
    37: 'CPR-> COND CPR',
    38: 'CPR-> fimrepita',
    39: 'A-> fim'
}

var = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG')
erros = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG', True)
tabela = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T1/T1/FONTE.ALG', simbolos=True)

action = pd.read_csv('D:/Aulas/Compiladores/Meus trabalhos/T2/T2/p_action.csv')
goto = pd.read_csv('D:/Aulas/Compiladores/Meus trabalhos/T2/T2/p_goto.csv')

token = pd.DataFrame(var)
i = 0
pilha = [0]

while(True):
    s = pilha[len(pilha)-1]
    try:
        a = token.loc[i]['Classe']
    except:
        a = 'eof'
    print(a)
    print(s)
    print(pilha)
    match(action.loc[int(s)][a.lower()].split('/')[0]):
        case 'S':
            pilha.append(action.loc[int(s)][a.lower()].split('/')[1])
            i = i + 1

        case 'R':
            AB = gramatica[int(action.loc[int(s)][a.lower()].split('/')[1])]
            A,B = AB.split('->')
            for n in range(0, len(B.split(' '))):
                pilha.pop()
            pilha.append(goto.loc[int(action.loc[int(s),a.lower()].split('/')[1]),A])
            print(AB)
            i = i + 1

        case 'ACC':
            print('Aceito')
            break

        case _ :
            print('erro')