import re

def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text

#remove_special_characters("¡Bueno, esto fue divertido! ¿Qué opinas? 123#@!", 
#                          remove_digits=True)