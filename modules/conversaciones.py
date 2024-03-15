import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk

df = pd.read_csv("../data/data_chat_clear_text.csv")
df.head(10)

def dividir_y_agrupar_por_tiempo(df, intervalo_tiempo):
    # Convierte la columna de fechas a tipo datetime si no lo está
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Agrupa el DataFrame por el intervalo de tiempo deseado y la columna de conversación
    grupos = df.groupby([pd.Grouper(key='Fecha', freq=intervalo_tiempo), 'Persona', 'Mensaje'])['clean_text'].apply(list)
    
    # Devuelve el DataFrame original junto con la agrupación por conversación
    return grupos


# intervalo_tiempo puede ser 'D' para días, 'H' para horas, 'M' para minutos, etc.

#df, conversaciones_agrupadas = dividir_y_agrupar_por_tiempo(df, 'D')
a = dividir_y_agrupar_por_tiempo(df, 'D')
#pd.set_option("max_colwidth", None)
#a.to_frame()
a = pd.DataFrame(a)
a

# Ahora, definimos una función para analizar el sentimiento de un texto usando TextBlob
def analizar_sentimiento(texto):
    analysis = TextBlob(str(texto))
    polarity = analysis.sentiment.polarity
    if polarity == 0:
        return 'neutro'
    elif polarity < 0:
        return 'negativo'
    else:
        return 'positivo'
    

# Aplicamos la función a cada fila de la columna 'text_clean' y creamos una nueva columna 'sentimiento'
a['sentimiento'] = a['clean_text'].apply(analizar_sentimiento)

# Ahora el DataFrame tiene una nueva columna llamada 'sentimiento' que contiene el resultado del análisis de sentimiento
a

# Puedes guardar este DataFrame modificado en un nuevo archivo CSV si lo deseas
a.to_csv('../data/conversacion_D.csv')