from textblob import TextBlob
import pandas as pd
def sent_blod():
    df = pd.read_csv("../data/chat.csv")

    mensajes = df['clean_text'].tolist()

    # Lista para almacenar los sentimientos de cada mensaje
    sentimientos = []

    # Iterar sobre cada mensaje y calcular el sentimiento
    for texto in mensajes:
        blob = TextBlob(texto)
        sentimiento = blob.sentiment.polarity
        if sentimiento > 0:
            sentimientos.append("positivo")
        elif sentimiento < 0:
            sentimientos.append("negativo")
            
        elif sentimiento == 0:
            sentimientos.append("neutro")

    # Imprimir los mensajes y sus sentimientos correspondientes
    for i, mensaje in enumerate(mensajes):
        #print("Mensaje:", mensaje)
        #print("Sentimiento:", sentimientos[i])
        #print()
        # Agregar los sentimientos al DataFrame original
        df['texBlod'] = sentimientos