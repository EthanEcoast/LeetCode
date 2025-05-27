import random

numero: int= random.randint(10, 999) #Obviamente un numero con un digito es palindromo, y habiendo 90 palindromos tanto en el rango de 3 digitos como de 4 digitos, la probabilidad es mucho inferior en 4 (1%) que en 3(10%)
print(f'El numero es: {numero}')

#Bloque para obtener los digitos de "numero" y listarlos
numero_digitos = numero
digitos_totales = 0
lista_digitos = [] #Se almacena el numero invertido
while numero_digitos != 0:
    lista_digitos.append(numero_digitos % 10)
    numero_digitos = numero_digitos // 10
    digitos_totales += 1

#Transformaremos la lista en un numero entero, respetando el orden invertido
#Si hay un cero al final de "numero", problemas al invertirlo. Ej : 10 --> 01 (python no contempla enteros con cero a la izquierda) !!!!!!!

numero_invertido = 0
for d in lista_digitos:
        numero_invertido += (10 ** (digitos_totales - 1) * d)
        digitos_totales -= 1

#Es palindromo?
if numero == numero_invertido:
    print(f'{numero} es palindormo')
else:
    print(f'El invertido de {numero} es {numero_invertido}, no es palindromo')