print ('Asignacon de equipo')
nombre = input ("Nombre: ")
sexo = input ('Sexo: ')

primera_letra_nombre = nombre[:1]
primera_letra = primera_letra_nombre.lower()
#print (primera_letra)

if sexo == ('F') and primera_letra in ('abcdefghijkl'):
    print ('Estas en el Grupo A')
elif sexo ==('M') and primera_letra in ('mnopqrstuvwxyz'):
        print ('Estas en el Grupo A')
else:
    print ('Estas en el rupo B')
