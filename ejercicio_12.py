str = 'X-DSPAM-Confidence: 0.8475'

# localizamos posicion
index = str.find(':')

# Extraemos a la parte que queremos de la cadena
# index + 1 para empezar justo después del ":"
num_str = str[index + 1:].strip()

# Convertimos la variable a float
try:
    num = float(num_str)
    # Imprime el resultado
    print(num)
except:
    # Controlamos por si no encontramos la cadena tal y como la queremos encontrar
    print("Error cant cast to float")
