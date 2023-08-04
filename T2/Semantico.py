
from lexico import Lexico
import pandas as pd
class Semantico():
    var = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/T2/T2/FONTE.ALG')
    cod = pd.DataFrame(var)

    def leitura(AB, file, i, tabela, cod=cod):
        with open(file, 'a') as file:
            match(AB):
                case'LV->varfim pt_v':
                    file.write("\n\n\n")

                case 'TIPO->inteiro':
                    file.write("int"+ " ")
                    return cod.loc[i-1]["Lexema"]
                
                case 'TIPO->real':
                    file.write("double" + " ")
                    return cod.loc[i-1]["Lexema"]
                
                case 'TIPO->literal':
                    file.write("literal" + " ")
                    return cod.loc[i-1]["Lexema"]
                
                case 'L->id':
                    if(cod.loc[i-2]["Lexema"]!=","):
                        file.write(cod.loc[i-1]["Lexema"] + ";\n")
                    return cod.loc[i-1]["Lexema"]
                
                case 'L->id vir L':
                    n=3
                    file.write(cod.loc[i-3]["Lexema"] + ","+ cod.loc[i-1]["Lexema"])
                    if(cod.loc[i]["Lexema"] == ";"):
                        file.write(";\n")
                    while(cod.loc[i-n]["Lexema"] == tabela[len(tabela)-1]):
                        n= 2 + n
                    return cod.loc[i-n]["Lexema"]
                
                case 'ES->leia id pt_v':
                    file.write("scanf(")
                    for m in range(0,len(tabela)):
                        if tabela[m] == cod.loc[i-2]['Lexema']:
                            for n in range(0, m):
                                if(tabela[m-n] == "inteiro"):
                                    file.write('"' + '%d' + '"' + ", &" + tabela[m] + ");\n")
                                elif(tabela[m-n] == "real"):
                                    file.write('"' + '%lf' + '"' + ", &" + tabela[m] + ");\n")
                                elif(tabela[m-n] == "literal"):
                                    file.write('"' + '%s' + '" ' + tabela[m] + ");\n")
                #Necessario correção, não esta funcionando direito

                case "ES->escreva ARG pt_v":
                    file.write("printf(")
                    file.write(cod.loc[i-2]["Lexema"]+")\n")

