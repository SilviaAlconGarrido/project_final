from main import pandas as pd

df = pd.read_csv("../data/capi_chat.csv")
df
 
def limpieza():

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
