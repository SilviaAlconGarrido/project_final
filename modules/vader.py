import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize.toktok import ToktokTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
def sent_vader():
    df = pd.read_csv("../data/chat.csv")

    valores_de_sentimiento = {
        "feliz": 0.7,
        "bien": 0.5,
        "genial": 0.8,
        "triste": -0.7,
        "cabreado": -0.8,
        "mal": -0.5,
        "espero": 0,
        "caer": -0.1,
        "gripe": -0.1,
        "malo": -0.2,
        "vale perfecto": 0.8,
        "jajajajaja": 0.1,
    }

    # Define una función para calcular un resumen del análisis de sentimientos
    def calcular_sentimiento_vader(texto):
        # Asegurarse de que el texto sea una cadena de texto
        if isinstance(texto, str):
            ### Analizando el sentimiento con VADER
            sia = SentimentIntensityAnalyzer()
            # Calcular los sentimientos utilizando VADER
            sentimientos = sia.polarity_scores(texto)
            # Devolver el sentimiento dominante
            if sentimientos['compound'] >= 0.05:
                return 'positivo'
            elif sentimientos['compound'] <= -0.05:
                return 'negativo'
            elif sentimientos['compound'] == 0.00:
                return 'neutro'
        else:
            return 'no aplicable'  # O cualquier otro valor que desees para casos donde el texto no sea una cadena de texto

    # Aplicar la función a cada mensaje en el DataFrame
    df['sentimiento_vader'] = df['clean_text'].apply(calcular_sentimiento_vader)
    df