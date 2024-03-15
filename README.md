![imagen](assets/foto.png)

# Whatsapp chats sentiment analysis:

:vulcan_salute: Do you want to know who is the person who talks the most in your group? Who is the most negative or the most positive? In this project I will show you how to know it.

## :footprints: First steps.

This is the Final project of Inronhack's Bootcamp.

## :thinking: Project:

In this project I am presenting an improvement proposal for WhatssApp application. With which I can know who is the conversation leader or the most negative, besides being able to make an implementation to help minors that can be suffering harassment in this application.

## :relieved: What does the project do?

This implementation transforms the .txt file from Whatsapp to a .csv file. This dataframe looks like this:

| Fecha | Time | Person | Mensaje |
|-------------------|---------------|-----------------|------------------|
| 30/11/2023 | 19:12:50 | Sil | Muchas gracias! |
| ...     | ...            | ...        | ...      |

Then we extract the general information so we can have see more interesting data. This data looks like this:

| Fecha | Day | Num_Day | Num_Month | Month   | Year | ... |
|-------|-----|---------|-----------|-------|-----|-----|
| 30/11/2023 | Jueves | 30 | 11 | Nov | 2023 | ...  |
| ...   | ... | ...     | ...       | ...   |...   | ... |

- Fecha, Day, Num_Day, Num_Month, Month, Year, Time, Person, Mensaje, Letras, Palabras.  

We implement a data cleaning on the "mensaje" column to make the model able to predict sentiments, in which we use:

- Removing of accent marks.

- Changing abbreviation (for example: "xq" by "porque")

- Special characters (like numbers, exclamations, interrogations, @, #, etc.)

- Text lemmatization.

- Text stemming.

- Removing stopwords.

After that data cleaning of the "mensaje" column, we analyse the sentiments of the sent messages. Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. I use TextBlob, Vader, N-grams:

- TextBlob is a Python library used for text data mining and naturan language processing.

- Vader with SentimentIntensityAnalyzer. Is a rule-based sentiment analysis tool that is specifically designed for analyzing social media texts. Vader is a pre-trained sentiment analysis model that provides a sentiment score for a given text.

- N-grams con nltk. A n-grama is a collection of n successive elements in a text document that can include words, numbers, symbols and punctiation. N-gramas models are useful in many text analysis applications where word sequences are relevant like sentiment analysis, text clasification and text generation.

We keep "Fecha", "Person", "Mensaje" and "clean_text" columns. After this, we split the text by days, hours and minutes to analyse its sentiment. With this information we can display our Dashboard.

With which we can know:

- Message frequency.

- User participation.

- Most used words.

- Sentiment analysis.

- Topics analysis.

- Social network analysis.

- Changes over time analysis.

[Dashboard link](https://public.tableau.com/app/profile/silvia.alcon.garrido/viz/ProyectoWhatsApp_17104079815290/Historia1?publish=yes)

> [!NOTE]

- Implent a pre education language model or use an Embedding for a better prediction of sentiments. 

- Return negative messages as an alert to tutors in cases of harassment in this platform.


## :star_struck: Why is this project useful?

This project is useful to know how is a conversation evolving, who is the conversations leader, who is the most positive or the most negative person. And in case of cyberbullying, the tutors of these minors could put measures on the situation.

## :robot: Additionally:

- Used libraries:
 
   * Pandas. 
   * csv.
   * Re.
   * matplotlib.
   * nltk.
   * unicodedata.
   * Numpy.
   * wordcloud.
   * TextBlob.
   * vaderSentiment.
   * spacy.

   ## 	:see_no_evil: Project structure:

``` bash
Proyect_final/
├──  assets
│    ├── foto.png
│    └── whatsapp.png
│── data
│   ├── chat_sentimientos.csv
│   ├── chat_Vader.csv
│   ├── chat.csv
│   ├── chat.txt
│   ├── conversacion_3H_TextBlod.csv
│   ├── conversacion_D_TextBlod.csv
│   ├── conversacion_M_TextBlod.csv
│   ├── data_chat_clear_text.csv
│   ├── Limpieza_inicial_chat.csv
│   └── pruebas
│       ├── all_sentimientos.csv
│       ├── capi_chat.csv
│       ├── clearM.csv
│       ├── conversacion_1H_sentimiento.csv
│       ├── conversacion_5H_sentimiento.csv
│       ├── conversacion_D_sentimiento.csv
│       ├── conversacion_Dia_sentimiento.csv
│       ├── conversacion_M_sentimiento.csv
│       └── data_capi_chat_clear.csv
├── modules
│   ├── m_bic_ava.py
│   ├── m_biciMad.py
│   ├── m_biciPark.py
│   ├── m_func_ava.py
│   ├── m_funciones_bicimad.py
│   ├── m_funciones_bicipark.py
│   └── m_json.py
├── notebooks
│   ├── Capi_chat_limpieza.ipynb
│   ├── chat_sentimientos.ipynb
│   ├── conversaciones_chat.ipynb
│   ├── EDA_capi.ipynb
│   └── Limpieza_inicial_chats.ipnb
├── LICENSE
├── main.py
└── README.md
```