from lexico import Lexico
import pandas as pd

var = Lexico.Scanner('D:/Compiladores-main/Compiladores-main/T1/FONTE.ALG')

df = pd.DataFrame(var)

lexema = df.loc[0]['Lexema']

print(df.to_string())
