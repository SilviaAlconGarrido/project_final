import tokenize
from nltk.tokenize.toktok import ToktokTokenizer
from main import stopword_list

def remove_stopwords(text, is_lower_case=False):
    tokens = tokenize.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

#remove_stopwords("De, y, si son palabras vacías, la computadora no lo es")