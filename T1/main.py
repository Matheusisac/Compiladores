from lexico import Lexico
import pandas as pd

var = Lexico.Scanner('D:/Compiladores-main/Compiladores-main/T1/FONTE.ALG')
erros = Lexico.Scanner('D:/Compiladores-main/Compiladores-main/T1/FONTE.ALG', True)

index = 0
df = pd.DataFrame(var)

for i in range(len(var['Classe'])):
    lexema = df.loc[i]
    print(lexema)
    if(df.loc[i]['Classe'] == 'ERRO'):
        print(erros[index])
        index += 1
    print('\n')
