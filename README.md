![imagen](assets/icono.jpeg)

# Analisis de chats de WhatsApp con sentimientos:

:vulcan_salute: Te gustaría saber quien es la persona que mas habla de tu grupo? Quién es la mas negativa o positiva? En este proyecto te muestro como saberlo.

## :footprints: First steps.

This is the Final project of Inronhack's Bootcamp.

## :thinking: Project:

In this project I am presenting an improvement proposal for WhatssApp applications. Con el que pretendo ayudar a muchos menores que puedan estar sufrido acoso por esta aplicación.

## :relieved: What does the project do?

Esta implementación transforma el .txt que exportamos de WhatssApp a .csv. Esta data se veria asi:

| Fecha | Time | Person | Mensaje |
|-------------------|---------------|-----------------|------------------|
| 30/11/2023 | 19:12:50 | Sil | Muchas gracias! |
| ...     | ...            | ...        | ...      |

Luego le extraemos información general para poder ver mas datos interesantes. Estos datos se ven asi:

| Fecha | Day | Num_Day | Num_Month | Month   | Year | ... |
|-------|-----|---------|-----------|-------|-----|-----|
| 30/11/2023 | Jueves | 30 | 11 | Nov | 2023 | ...  |
| ...   | ... | ...     | ...       | ...   |...   | ... |

- Fecha, Day, Num_Day, Num_Month, Month, Year, Time, Person, Mensaje, Num_palabra.  

Implementamos una limpieza de la columana mesaje para que luego el modelo puedo predecir el sentimiento, en la que utilizamos:

- La eliminación de acentos.

- Cambiamos abreviaturas como (example: "xq" por "porque").

- Caracteres especiales (entre ellos los números, exclamaciones, interrogaciones y @#, etc).

- Text lemmatization.

- Text stemming.

- Remove stopwords.

Tras tener esa la limpieza de la columana mensaje,analizamos el sentimniento de los mensajes enviaviados. Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. Utilizo TextBlob, Vader, N-grams:

- TextBlob.

- Vader con SentimentIntensityAnalyzer. Is a rule-based sentiment analysis tool that is specifically designed for analyzing social media texts. Vader is a pre-trained sentiment analysis model that provides a sentiment score for a given text.

- N-grams con nltk.

> [!NOTE]

- Implementación pre-educar un modelo de lenguaje o utilizar Embedding para que pueda predecir mejor los sentimientos. 

- Devolver los mensajes negativos como una alerta para los tutores.


## :star_struck: Why is this project useful?

## :robot: Additionally:

- Used libraries:
 
   * Pandas. 
   * Requests.
   * Re.
   * Json.
   * Math.
   * Bs4.
   * Numpy.
   * Arparse.
   * Fuzzywuzzy.

   ## 	:see_no_evil: Project structure:

``` bash
Proyect_m1/
├── _wip_
├──  assets
│    └── banco_espana.jpeg
│── data
│   ├── bici_monu.csv
│   ├── bicimad_realtime.csv
│   ├── bicimad_stations.csv
│   ├── bicipark_monu.csv
│   ├── bicipark_stations.csv
│   └── colum_bicimad_realtime1.csv
├── modules
│   ├── m_bic_ava.py
│   ├── m_biciMad.py
│   ├── m_biciPark.py
│   ├── m_func_ava.py
│   ├── m_funciones_bicimad.py
│   ├── m_funciones_bicipark.py
│   └── m_json.py
├── notebooks
│   ├── dev_api.ipynb
│   └── dev_notebook_.ipnb
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```