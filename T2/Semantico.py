from lexico import Lexico
import pandas as pd
class Semantico():
    var = Lexico.Scanner('D:/Aulas/Compiladores/Compiladores-main/T2/FONTE.ALG')
    cod = pd.DataFrame(var)

    def leitura(AB, file, i, tabela, linha, col, cod=cod):
        with open(file, 'a') as file:
            match(AB):
                case'LV->varfim pt_v':
                    linha_atual = []
                    tipo_atual = None
                    tabela1 = []
                    for item in tabela:
                        if item == "inteiro" or item == "literal" or item == "real":
                            if linha_atual:
                                tabela1.append(linha_atual)
                            linha_atual = [item]
                            tipo_atual = item
                        else:
                            if tipo_atual is not None:
                                linha_atual.append(item)

                    if linha_atual:
                        tabela1.append(linha_atual)

                    return tabela1

                case 'TIPO->inteiro':
                    file.write("\tint"+ " ")
                    tabela1 = tabela
                    tabela1.append(cod.loc[i-1]["Lexema"])
                    return tabela1
                
                case 'TIPO->real':
                    file.write("\tdouble" + " ")
                    tabela1 = tabela
                    tabela1.append(cod.loc[i-1]["Lexema"])
                    return tabela1
                
                case 'TIPO->literal':
                    file.write("\tliteral" + " ")
                    tabela1 = tabela
                    tabela1.append(cod.loc[i-1]["Lexema"])
                    return tabela1
                
                case 'L->id':
                    file.write(cod.loc[i-1]["Lexema"] + ";\n")
                    tabela1 = tabela
                    tabela1.append(cod.loc[i-1]["Lexema"])
                    return tabela1
                
                case 'L->id vir L':
                    n=3
                    fim = 0
                    while fim != 1:
                        id = cod.loc[i-n]["Lexema"]
                        if id in tabela or id == "," or id == ';':
                            n=n+1
                        else:
                            while(cod.loc[i-n]["Classe"]== "id" or cod.loc[i-n]["Lexema"]== ","):
                                n=n+1
                            if(cod.loc[i-n]["Lexema"] == "inteiro"):
                                file.write('\tint ')
                            if(cod.loc[i-n]["Lexema"] == "real"):
                                file.write('\tdouble ')
                            if(cod.loc[i-n]["Lexema"] == "literal"):
                                file.write('\tliteral ')
                            file.write(id + ";\n")
                        tabela1 = tabela
                        tabela1.append(id)
                        return tabela1
                    
                case "ES->leia id pt_v":
                    ERRO_SEMANTICO = 0
                    count = 0
                    for n in range (0, len(tabela)):
                        if cod.loc[i-2]["Lexema"] in tabela[n]:
                            match(tabela[n][0]):
                                case "inteiro":
                                    file.write("\tscanf("+ '"' + '%d'+'"'+', &' + cod.loc[i-2]["Lexema"]+');\n')
                                    count = 0
                                case "literal":
                                    file.write("\tscanf("+ '"' + '%s'+'"'+', &' + cod.loc[i-2]["Lexema"]+');\n')
                                    count = 0
                                case "real":
                                    file.write("\tscanf("+ '"' + '%lf'+'"'+',' + cod.loc[i-2]["Lexema"]+');\n')
                                    count = 0
                        else:
                            count = count + 1
                    if(count == len(tabela)):
                        ERRO_SEMANTICO = 1
                        print(f"Erro: Variável não declarada, linha: {linha} coluna {col}")
                    if ERRO_SEMANTICO == 1:
                        tabela1 = tabela
                        tabela1.append("ERRO_SEMANTICO")
                        return tabela1
                        
                
                case "ES->escreva ARG pt_v":
                    ERRO_SEMANTICO = 0
                    match(cod.loc[i-2]["Classe"]):
                        case "Lit":
                            file.write("\tprintf(" +cod.loc[i-2]["Lexema"]+");\n")
                        case "Num":
                            file.write('\tprintf("'+ cod.loc[i-1]["Lexema"]+'");\n')
                        case "id":
                            count = 0
                            for n in range (0, len(tabela)):
                                if cod.loc[i-2]["Lexema"] in tabela[n]:
                                    match(tabela[n][0]):
                                        case "inteiro":
                                            file.write('\tprintf("' + '%d'+'"'+',' + cod.loc[i-2]["Lexema"]+');\n')
                                            count = 0
                                        case "literal":
                                            file.write('\tprintf("' + '%s'+'"'+',' + cod.loc[i-2]["Lexema"]+');\n')
                                            count = 0
                                        case "real":
                                            file.write('\tprintf("' + '%lf'+'"'+',' + cod.loc[i-2]["Lexema"]+');\n')
                                            count = 0
                                else:
                                    count = count + 1
                            if(count == len(tabela)):
                                print(f"Erro: Variável não declarada, linha: {linha} coluna {col}")
                                ERRO_SEMANTICO = 1
                    if ERRO_SEMANTICO == 1:
                        tabela1 = tabela
                        tabela1.append("ERRO_SEMANTICO")
                        return tabela1
                                
                        
                case "CMD->id rcb LD pt_v":
                    ERRO_SEMANTICO = 0
                    fim=0
                    n=0
                    count=0
                    while fim == 0:
                        n=n+1
                        if cod.loc[i-n]["Lexema"] == "<-":
                            fim = 1
                            id = cod.loc[i-n-1]["Lexema"]
                            for m in range(0, len(tabela)):
                                if id in tabela[m]:
                                    if(cod.loc[i-n+1]["Classe"] == 'id'):
                                        count = 0
                                        for t in range(0, len(tabela)):
                                            if cod.loc[i-n+1]["Lexema"] in tabela[t]:
                                                if  tabela[t][0] == tabela[m][0]:
                                                    file.write("\t"+id+"="+cod.loc[i-n+1]["Lexema"])
                                                    count =0
                                                else:
                                                    ERRO_SEMANTICO = 1
                                                    print(f"Erro: Tipos diferentes para atribuição, linha: {linha} coluna {col}")
                                                    count = 0
                                            else:
                                                count = count+1
                                            if(count == len(tabela)):
                                                ERRO_SEMANTICO = 1
                                                print(f"Erro: Variável não declarada, linha: {linha} coluna {col}")
                                                count = 0
                                                
                                                
                                    else:
                                        if(tabela[m][0] == cod.loc[i-n+1]["Tipo"]):
                                            file.write("\t"+id+"="+cod.loc[i-n+1]["Lexema"])
                                            count = 0
                                        elif(count != 0):
                                            ERRO_SEMANTICO = 1
                                            print(f"Erro: Tipos diferentes para atribuição, linha: aqui {linha} coluna {col}")
                                            count = 0
                                            
                                else:
                                    count= count+1
                                
                            t=0
                            for t in range (i-n,i):
                                if(cod.loc[t]["Classe"]=="OPM"):
                                    file.write(cod.loc[t]["Lexema"]+cod.loc[t+1]["Lexema"])
                                if(cod.loc[t]["Lexema"]==";"):
                                    file.write(";\n")
                                    
                    if ERRO_SEMANTICO == 1:
                        tabela1 = tabela
                        tabela1.append("ERRO_SEMANTICO")
                        return tabela1
               

                case "COND->CAB CP":
                    file.write("\t}\n")
                
                case "CAB->se ab_p EXP_R fc_p entao":
                    file.write("\tif("+cod.loc[i-5]["Lexema"]+""+cod.loc[i-4]["Lexema"]+""+cod.loc[i-3]["Lexema"]+"){\n")

                case 'EXP_R->OPRD opr OPRD':
                    ERRO_SEMANTICO = 0

                    if cod.loc[i-3]['Classe'] == "id":
                        id1 = cod.loc[i-3]['Lexema']
                        for t in range (0,len(tabela)):
                            if id1 in tabela[t]:
                                Tipo1 = tabela[t][0]
                    else:
                        Tipo1=cod.loc[i-2]["Tipo"]
                    if cod.loc[i-1]['Classe'] == "id":
                        id2 = cod.loc[i-1]['Lexema']
                        for t in range (0,len(tabela)):
                            if id2 in tabela[t]:
                                Tipo2 = tabela[t][0]
                    else:
                        Tipo2=cod.loc[i-1]["Tipo"]
                        fim = 0
                    if Tipo1 != Tipo2:
                        print(f"Erro: Tipos são imcompativeis, linha: {linha} coluna {col}")
                        ERRO_SEMANTICO = 1
                    if ERRO_SEMANTICO == 1:
                        tabela1 = tabela
                        tabela1.append("ERRO_SEMANTICO")
                        return tabela1
                
                case "P->inicio V A":
                    file.write("}\n")
                
                case "CABR->repita ab_p EXP_R fc_p":
                    file.write("\twhile("+cod.loc[i-4]["Lexema"]+""+cod.loc[i-3]["Lexema"]+""+cod.loc[i-2]["Lexema"]+"){\n")
                
                case "CPR->fimrepita":
                    file.write("\t}\n")
