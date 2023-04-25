Actual_Year = 2023
nombre = input ('¿Cuál es tu nombre?')
primer_apellido = input ('¿Cuál es tu primer apellido?')
segundo_apellido =input ('¿Cuál es tu segundo apellido?')
yyyy= input ('¿En qué año naciste?')
mmdd=input ('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')

#concatenar nombre y apellido
nombre_completo = nombre +" "+ primer_apellido+" "+segundo_apellido 
nombre_completo_sin_espacios=nombre+primer_apellido+segundo_apellido

#impresion A
nombre_completo_upper = nombre_completo.upper()
print (nombre_completo_upper)

#impresion B
nombre_completo_lower = nombre_completo.lower()
print (nombre_completo_lower)

#impresion C
DOB = mmdd[3:]+"-"+mmdd[:2]+"-"+yyyy
print (DOB)

#Impresion D

age = Actual_Year-int(yyyy)
print (age)

#impresion E
def contar_vocales(nombre_completo_lower):
	contador = 0
	for letra in nombre_completo_lower:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

cantidad = contar_vocales(nombre_completo_lower)

print(f"En la cadena '{nombre_completo_lower}'' hay {cantidad} vocales")


#impresion F
nombre_completo_sin_espacios = nombre_completo_sin_espacios.lower()
print ('Tu nombre completo tiene' ,len(nombre_completo_sin_espacios), 'letras')


#Impresion G
if  type (age) == int:
	print  ('¿Tu edad es un carácter de tipo número?', True)
else:
	print (False)

#Impresion H
if  type (nombre_completo_sin_espacios) == str:
	print  ('¿Tu nombre completo es un carácter de tipo alfanumérico?', True)
else:
	print (False)

#Impresion I
age_in_10_years=age+10
age_in_20_years=age+20
print ('Tu edad en 10 años será:', age_in_10_years)

#Impresion J
promedio = (age+age_in_20_years/2)
print ('La media de tu edad actual y tu edad en 20 años es', promedio)










