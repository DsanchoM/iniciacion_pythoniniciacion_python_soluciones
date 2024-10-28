str = 'X-DSPAM-Confidence: 0.8475'
posicion = str.find(':')
cadena= str[posicion + 1:].strip()
numCadena = float(cadena)
print(f"Numero extraido es:{numCadena}")