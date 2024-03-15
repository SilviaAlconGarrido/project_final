import pandas as pd
import csv
import re

#Cambiamos el formato txt por csv
def limpieza():

# Ruta al archivo de texto que deseas convertir
    archivo_txt = '../data/chat.txt'

# Ruta al archivo CSV de salida
    archivo_csv = '../data/chat.csv'

# Patrón de expresión regular para buscar la fecha, hora, persona y mensaje
    patron = r'\[(.*?)\] (.*?): (.*)'

# Lee el archivo de texto y escribe los datos en un archivo CSV
    with open(archivo_txt, 'r') as txt_file, open(archivo_csv, 'w', newline='') as csv_file:
    # Crea un objeto de escritura de CSV
        writer = csv.writer(csv_file)
    # Escribe el encabezado del CSV
        writer.writerow(["Fecha", "Hora", "Persona", "Mensaje"])
    
    # Procesa cada línea del archivo de texto
    for linea in txt_file:
        # Busca coincidencias con el patrón de expresión regular
        match = re.match(patron, linea)
        
        # Si hay una coincidencia, extrae la información
        if match:
            fecha_hora, persona, mensaje = match.groups()
            fecha, hora = fecha_hora.split()
            
            # Escribe los datos en el archivo CSV
            writer.writerow([fecha, hora, persona, mensaje])

#print("El archivo TXT se ha convertido exitosamente a CSV.")

# sacamos la data

    df = pd.read_csv("../data/chat.csv")


# Limpiamos la columan Fecha

    fecha = df['Fecha']

# Eliminar la coma de las fechas
    fechas_sin_coma = fecha.str.replace(",", "")

# Reemplazar la columna 'fecha' en el DataFrame original
    df['Fecha'] = fechas_sin_coma

# diccionario con el valor y nombre de los dias
    week = {
    6:'Domingo',
    0:'Lunes',
    1:'Martes',
    2:'Miercoles',
    3:'Jueves',
    4:'Viernes',
    5:'Sabado'
    }

# Diccionario con el valor y nombre de los meses
    month = {
    1:'Ene',
    2:'Feb',
    3:'Mar',
    4:'Abr',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Ago',
    9:'Sept',
    10:'Obt',
    11:'Nov',
    12:'Dic'
    }


# dar formato de fecha a los dias 
    df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

# nueva columna con los nombres de los dias
#df['Dia'] = df['Fecha'].dt.strftime('%A') #(esto tambien lo cambia)
    df['Dia'] = df['Fecha'].dt.weekday.map(week)

# nueva columna con el numero del dia
    df['Num_Day'] = df['Fecha'].dt.day

# nueva columna con el año 
    df['Year'] = df['Fecha'].dt.year

# nueva columna con el numero de mes
    df['Num_Month'] = df['Fecha'].dt.month

# nueva columna con el nombre de los meses
    df['Month'] = df['Fecha'].dt.month.map(month)

# nueva columna con el nombre de numero de palabras
# Dividir cada mensaje en palabras y contar la cantidad de palabras
    df['Num_palabra'] = df['Mensaje'].str.split().apply(len)


# organizar las columnas
    df = df[['Fecha', 'Dia', 'Num_Day','Num_Month', 'Month', 'Year', 'Hora', 'Persona', 'Mensaje']]

# cambiar el tipo de dato de la columna Day
    df['Dia'] = df['Dia'].astype('category')
#cambiar formato fecha 
    df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y')

# cantidad de palabras
    
    df['Letras'] = df['Mensaje'].apply(lambda s:len(s))

# Cantidad de palabras por mensaje

    df['Palabras'] = df['Mensaje'].apply(lambda s:len(s.split(' ')))

# Exportamos la data

#Exportamos los datos limpios en un archivo csv
    df.to_csv('../data/Limpieza_inicial_chat.csv', header=True, index=True)