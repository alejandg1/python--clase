import json


archivo1 = open('datos/archivo1.txt','r')
contenido = archivo1.read()
# print(f"{contenido}")
# archivo1.close()


archivo2 = open('datos/archivo2.json','r')
conten2 = json.load(archivo2)

for i in conten2:
    print(i)