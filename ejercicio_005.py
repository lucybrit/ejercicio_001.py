#Fruta
precio_fruta = {}
precio_fruta ["Platano"]=1.35
precio_fruta ["Manzana"]=0.80
precio_fruta ["Pera"]=0.85
precio_fruta ["Naranja"]=0.70

#print (precio_fruta)
fruta=input("que precio deseas saber: Platano, Manzana, Pera o Naranja: ")


#for f,v in precio_fruta.items():
if fruta in precio_fruta.keys():
    print (f"El Precio de {fruta} es ${precio_fruta[fruta]}")
        
else :
    print (f"{fruta} no esta en el catalogo")
    

