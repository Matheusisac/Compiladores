
from lexico import Lexico
import pandas as pd
class Semantico():
    var = Lexico.Scanner('D:/Aulas/Compiladores/Meus trabalhos/Compiladores-main/Compiladores-main/T2/FONTE.ALG')
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
                    file.write(cod.loc[i-1]["Lexema"] + ";\n")
                    return cod.loc[i-1]["Lexema"]
                
                case 'L->id vir L':
                    n=3
                    fim = 0
                    while fim != 1:
                        id = cod.loc[i-n]["Lexema"]
                        if id in tabela or id == "," or id == ';':
                            n=n+1
                        else:
                            print(id)
                            while(cod.loc[i-n]["Classe"]== "id" or cod.loc[n]["Lexema"]== ","):
                                n=n+1
                            if(cod.loc[i-n]["Lexema"] == "inteiro"):
                                file.write('int ')
                            if(cod.loc[i-n]["Lexema"] == "real"):
                                file.write('double ')
                            if(cod.loc[i-n]["Lexema"] == "literal"):
                                file.write('literal ')
                            file.write(id + ";\n")
                            return id
                
                case 'ES->leia id pt_v':
                    fim = 0
                    file.write("scanf(")
                    for m in range(0,len(tabela)):
                        if tabela[m] == cod.loc[i-2]['Lexema']:
                            for n in range(0, m+1):
                                if fim == 0:
                                    if(tabela[m-n] == "inteiro"):
                                        file.write('"' + '%d' + '"' + ", &" + tabela[m] + ");\n")
                                        fim = 1
                                    elif(tabela[m-n] == "real"):
                                        file.write('"' + '%lf' + '"' + ", &" + tabela[m] + ");\n")
                                        fim = 1
                                    elif(tabela[m-n] == "literal"):
                                        file.write('"' + '%s' + '" ' + tabela[m] + ");\n")
                                        fim = 1

                case "ES->escreva ARG pt_v":
                    fim = 0
                    file.write("printf(")
                    if(cod.loc[i-2]["Classe"] == 'id'):
                        for m in range(0,len(tabela)):
                            if tabela[m] == cod.loc[i-2]['Lexema']:
                                for n in range(0, m+1):
                                    if fim == 0:
                                        if(tabela[m-n] == "inteiro"):
                                            file.write('"' + '%d' + '"' + "," + tabela[m] + ");\n")
                                            fim = 1
                                        elif(tabela[m-n] == "real"):
                                            file.write('"' + '%lf' + '"' + "," + tabela[m] + ");\n")
                                            fim = 1
                                        elif(tabela[m-n] == "literal"):
                                            file.write('"' + '%s' + '", ' + tabela[m] + ");\n")
                                            fim = 1
                    else:
                        file.write(cod.loc[i-2]["Lexema"]+")\n")

