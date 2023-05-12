while True :
    psw_validar = input ('Escribe la contraseña: ')
    counter = counter + 1
    if psw_validar == psw:
        print ('La contraseña es correcta')
        break
    if psw_validar != psw and counter < 7 : 
        print (f"Te quedan {7- counter} intentos")
    if counter == 7:
        print ('Se termiaron tus intentos')
        break
        
