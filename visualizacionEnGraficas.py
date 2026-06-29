
import pandas as pd 


import matplotlib.pyplot as plt  #pip install matplotlib
import seaborn as sns               #pip install seaborn

sns.set_theme(style="whitegrid")# Esto hace que las gráficas se vean mejor por defecto



df = pd.read_csv('Student_Performance.csv') #importamos el csv
           

            #Comandos para dibujar las graficas 
"""
    #Histograma del rendimiento general 
plt.figure(figsize=(8, 5))#definimos el tamaño en pulgadas
#data indica de donde sacar los datos, bins es para la presicion de la grafica
sns.histplot(data=df, x='overall_score', bins=10, color='skyblue')
plt.title('Distribución de las Calificaciones Finales') #titulo
plt.xlabel('Puntuación General') #etiqueta del eje x
plt.ylabel('Cantidad de Estudiantes') #etiqueta del eje y
plt.show()#muestra la grafica

"""

