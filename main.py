import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize.toktok import ToktokTokenizer
import re
import unicodedata
from collections import Counter
from abreviaturas import corregir_abreviaturas
from acentos import remove_accented_chars
from carasteres_especiales import remove_special_characters
from general import limpieza
from lemmatizacion import lemmatize_text
from Remove_stopwords import remove_stopwords
from Text_stemming import simple_stemmer
from normalize import normalize_corpus

# Inicializar el tokenizador
tokenizer = ToktokTokenizer()

# Descargar la lista de stopwords en español de NLTK
nltk.download('stopwords')
stopword_list = nltk.corpus.stopwords.words('spanish')

# mi df
df = pd.read_csv("../data/capi_chat.csv")
df

if __name__ == '__main__':
    print('Bienvenido, dime tu edad')
    # Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))
# Verificar si la edad es mayor o igual a 18
if edad >= 18:
    print("Eres mayor de 18 años. Chao!")
elif edad <= 16:
    print("Eres menor de 16 años. Por favor ingrese el número de su tutor:")
    
    

        
# Pre-process and normalize news articles
df['clean_text'] = normalize_corpus(df['Mensaje'])
#norm_corpus = list(df['Mensaje'])
df.iloc[1][['Mensaje', 'clean_text']].to_dict()
#news_df.iloc[1]['clean_text'].to_dict()
df