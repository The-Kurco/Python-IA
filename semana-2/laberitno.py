with open("laberinto.txt","r") as archivo:
    laberinto = archivo.readlines()

for i in range(len(laberinto)):
    laberinto[i]= laberinto[i].replace("\n","")

for linea in laberinto:
    print(linea)
    