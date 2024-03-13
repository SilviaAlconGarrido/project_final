# Importar NLTK
import nltk
from main import SnowballStemmer
from main import nlp

# Crear una instancia de SnowballStemmer para español
stemmer_es = SnowballStemmer('spanish')

def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

#lemmatize_text('Mi sistema sigue fallando. El suyo falló ayer, el nuestro falla diariamente.')