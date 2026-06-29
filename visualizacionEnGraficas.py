
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
"""
    #Dispersion 
plt.figure(figsize=(8, 5))

# sns.scatterplot es la función para puntos de dispersión
# (útil cuando tienes 25,000 puntos para que no se vea todo negro)
#las variables x y son las columnas que vayamos a comparar, alpha=0.5: Hace que los puntos sean un poco transparentes 
sns.scatterplot(data=df, x='study_hours', y='overall_score')

plt.title('Relación entre Horas de Estudio y Calificación')
plt.xlabel('Horas de Estudio Diarias')
plt.ylabel('Puntuación General')
plt.show()
"""

