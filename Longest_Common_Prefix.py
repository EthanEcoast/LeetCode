#Definir string

string0 = input("Primera palabra: ")
string1 = input("Segunda palabra: ")
string2 = input("Tercera palabra: ")

#Funcion de cambio de string a lista

def string_lista(palabra):
    lista = []
    for i in palabra:
        lista.append(i)
    return lista

string0_lista = string_lista(string0)
string1_lista = string_lista(string1)
string2_lista = string_lista(string2)

#Bloque de comparacion

prefix = []

for x, y, z in zip(string0_lista, string1_lista, string2_lista):
    if x == y == z:
        prefix.append(x)
    else:
        break

prefix_string = "".join(prefix)

if prefix_string: 
    print(f'{prefix_string}- es el prefijos coincidente')
else:
    print('No coincide en prefijos')