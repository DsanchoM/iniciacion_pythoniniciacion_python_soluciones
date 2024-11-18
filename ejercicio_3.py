'''
EJERCICIO 3: Supongamos que ejecutamos las siguientes instrucciones de asignación:
width = 17
height = 12.0

Para cada una de las siguientes expresiones, escriba el valor de la expresión y el tipo (del valor de la expresión).
Use el intérprete de Python para verificar sus respuestas.
width//2
width/ 2.0
height/ 3
1+2*5
'''
width = 17
height = 12.0

caso1 = width//2
print(f'El valor del primer caso es {caso1} y su tipo es {type(caso1)}')

caso2 = width/2.0
print(f'El valor del segundo caso es {caso2} y su tipo es {type(caso2)}')

caso3 = height/2
print(f'El valor del tercer caso es {caso3} y su tipo es {type(caso3)}')

caso4 = 1+2*5
print(f'El valor del cuarto caso es {caso4} y su tipo es {type(caso4)}')
