
import pandas as pd 


import matplotlib.pyplot as plt  #pip install matplotlib
import seaborn as sns               #pip install seaborn

sns.set_theme(style="whitegrid")# Esto hace que las gráficas se vean mejor por defecto



df = pd.read_csv('Student_Performance.csv') #importamos el csv
           

            #Comandos para dibujar las graficas 

    #Histograma del rendimiento general 
plt.figure(figsize=(8, 5))#definimos el tamaño en pulgadas
#data indica de donde sacar los datos, bins es para la presicion de la grafica
sns.histplot(data=df, x='overall_score', bins=10, color='skyblue')
plt.title('Distribución de las Calificaciones Finales') #titulo
plt.xlabel('Puntuación General') #etiqueta del eje x
plt.ylabel('Cantidad de Estudiantes') #etiqueta del eje y
plt.show()#muestra la grafica


    #Dispersion 
plt.figure(figsize=(8, 5))

# sns.scatterplot es la función para puntos de dispersión
#las variables x y son las columnas que vayamos a comparar
sns.scatterplot(data=df, x='study_hours', y='overall_score')
#estos comandos ya los vimos
plt.title('Relación entre Horas de Estudio y Calificación')
plt.xlabel('Horas de Estudio Diarias')
plt.ylabel('Puntuación General')
plt.show()




    #Grafico de barras
plt.figure(figsize=(8, 6))
# sns.barplot calcula automáticamente el promedio (mean) para cada método
sns.barplot(data=df, x='study_method', y='overall_score', palette='viridis')
plt.ylim(60, 65) #como los graficos estaban bastante parejos, haremos enfoque entre las calificaiones 60 a 65 
plt.title('Nota Promedio por Método de Estudio')
plt.ylabel('Puntuación Promedio')
plt.show()