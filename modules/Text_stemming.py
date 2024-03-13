import nltk

def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

#simple_stemmer('Mi sistema sigue fallando. El suyo falló ayer, el nuestro falla diariamente.')