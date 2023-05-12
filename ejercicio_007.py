frase=input("Escribe una frese: ")
frase_lista=frase.split()#la funcion split se usa para dividir la frase en una lista a partir de los espacios

print(frase_lista)

for p in frase_lista:
    print (f"la longitud de la  palabra {p} es {len(p)}")