import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams
from textblob import TextBlob
import nltk
from nltk import word_tokenize
nltk.download('punkt')
import pandas as pd

def sent_ngrams():
    df = pd.read_csv("../data/chat.csv")

    # Función para generar n-grams de una lista de tokens
    def generar_ngrams(tokens, n):
        return list(ngrams(tokens, n))

    # Tokenización y generación de n-grams para cada fila del DataFrame
    n = 2  # Tamaño de los n-grams

    def analisis_sentimiento(texto):
        # Tokenizar el texto
        tokens = word_tokenize(texto)
        # Generar n-grams
        n_grams = generar_ngrams(tokens, n)
        # Verificar si hay n-grams
        if not n_grams:
            return 'neutro'  # Devolver 'neutro' si no hay n-grams
        # Calcular el sentimiento para cada n-gram y promediar los resultados
        sentimientos = [TextBlob(' '.join(ngram)).sentiment.polarity for ngram in n_grams]
        # Calcular el promedio de los sentimientos de los n-grams
        promedio_sentimientos = sum(sentimientos) / len(sentimientos)
        # Categorizar el sentimiento
        if promedio_sentimientos > 0.2:
            return 'positivo'
        elif promedio_sentimientos < -0.2:
            return 'negativo'
        else:
            return 'neutro'

    # Aplicar el análisis de sentimientos a cada texto en el DataFrame
    df['n-grams'] = df['clean_text'].apply(analisis_sentimiento)

    df