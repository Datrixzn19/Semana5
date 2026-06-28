import pandas as pd 

#Cargar el archivo CSV en un DataFrame
df = pd.read_csv('Student_Performance.csv')

            #Comandos de exploracion del dataset 
print("Comando .head()")
print(df.head(5)) #Mostramos los primeros 5 registros

print("Comando .info()")
print(df.info()) #Muestra informacion general del dataset

print("Comando .describe()")
print(df.describe())

print("Comando .tail()")
print(df.tail(5))  #Muestra los ultimos n registros 


            #Comandos para dibujar las graficas 