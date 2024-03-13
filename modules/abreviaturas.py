# abreviaturas

CONTRACCIONES_ESP = {
"xq": "porque",

"sticker omitido": "imagen",
"imagen omitida": "imagen",
"q": "que",
"X": "por",
"x": "por",
"esq": "es que",
"GIF omitido": "GIF",
"Valee": "vale",
"perfe": "perfecto",
"Siiii": "Si",
"siii": "Si",
"Ayyy":"Ay",
"proque": "porque",
"nose": "no se",

"tmbn": "tambien",
"lab": "laboratorio",
"labs": "labboratotios",
"lst": "lista",
"reu": "reunion",
"michi": "gato",
"jaajaaj": "jajajajaja",
"xd": "risa",
"capiiis": "capi",
"smpr": "siempre",
"Noup": "No",
"okii": "vale",
"year": "año",
"string": "letras",
"colorinchis": "colores",
"pull request": "subir",
"LOL": "risa a carcajadas",
"Wsp": "WhatsApp",
"Wasap": "WhatsApp",
"wa": "WhatsApp",
"Guasap": "WhatsApp",
"Pq": "porque",
"Xq": "porque",
"q": "que",
"Dnd": "donde",
"K": "que",
"T": "te",
"+/-": "mas o menos",
"Nd": "nada",
"Vdd": "verdad",
"Ntp": "no te preocupes",
"Tqm": "Te quiero mucho",
"Tq": "Te quiero",
"Tmb": "tambien",
"Dps": "despues",
"Xfa": "por favor",
"Dd": "donde",

"Tkt": "tranquilo", 
"Tqg": "te quiero un monton",
"Bss": "besos",
"Tmbn": "tambien",
"Fvr": "favor",
"Msj": "mensaje",
"LMAO": "risa",
"BRB": "Vuelvo enseguida",
"IDK": "no se",
"idk": "no se",
"ASAP": "tan pronto como sea posible",
"OMG": "Oh Dios mio",
"BFF": "Mejores amigos para siempre",

}

def corregir_abreviaturas(texto, mapeo_abreviaturas=CONTRACCIONES_ESP):
    texto_corregido = []
    for palabra in texto.replace(".","").split():
        palabra_corregida = mapeo_abreviaturas.get(palabra.lower(), palabra)
        if palabra_corregida is not None:
            texto_corregido.append(palabra_corregida)
        else:
            texto_corregido.append(palabra)
    return ' '.join(texto_corregido)
# Llamar a la función corregir_abreviaturas con el diccionario de abreviaturas
#a = corregir_abreviaturas( 'Q tal. okey xq.')
#print(a)