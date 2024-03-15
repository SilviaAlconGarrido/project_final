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
from textblob import sent_blod
from vader import sent_vader
from ngrams import sent_ngrams
from conversaciones import dividir_y_agrupar_por_tiempo

# Inicializar el tokenizador
tokenizer = ToktokTokenizer()

df = pd.read_csv("../data/chat.csv")

# Descargar la lista de stopwords en español de NLTK
nltk.download('stopwords')
stopword_list = nltk.corpus.stopwords.words('spanish')

def normalize_corpus(corpus, contraction_expansion=True,
                     accented_char_removal=True, text_lower_case=True, 
                     text_lemmatization=True, special_char_removal=True, 
                     stopword_removal=True, remove_digits=True):
    
    normalized_corp = []
    # normalize each document in the corpus
    for doc in corpus():
        # remove accented characters
        if accented_char_removal():
            doc = remove_accented_chars(doc)
        # expand contractions    
        if contraction_expansion():
            doc = corregir_abreviaturas(doc)
        # lowercase the text    
        if text_lower_case():
            doc = doc.lower()
        # remove extra newlines
            doc = re.sub(r'[\r|\n|\r\n]+', ' ',doc)
        # lemmatize text
        if text_lemmatization():
            doc = lemmatize_text(doc)
        # remove special characters and\or digits    
        if special_char_removal():
            # insert spaces between special characters to isolate them    
            special_char_pattern = re.compile(r'([{.(-)!}])')
            doc = special_char_pattern.sub(" \\1 ", doc)
            doc = remove_special_characters(doc, remove_digits=remove_digits)  
        # remove extra whitespace
            doc = re.sub(' +', ' ', doc)
        # remove stopwords
        if stopword_removal():
            doc = remove_stopwords(doc, is_lower_case=text_lower_case)
            

if __name__ == '__main__':
    normalized_corpus.append(doc)

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