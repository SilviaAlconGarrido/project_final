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
            
normalized_corpus.append(doc)

df['clean_text'] = normalize_corpus(df['Mensaje'])
#norm_corpus = list(df['Mensaje'])
df.iloc[1][['Mensaje', 'clean_text']].to_dict()
#news_df.iloc[1]['clean_text'].to_dict()
