import json
import time
directorio = open('datos/directorio.json','r')
usuarios = json.load(directorio)
userinfo=[]
cargos=[]
departamentos=[]

def runner():
    print("escoja la información que desea ver: 1. información de los usuarios, 2. total de cargos,usuarios y departamentos.")
    eleccion = input("escriba su respuesta:  ")
    match eleccion:
        case "1":
            personas_info()
            presentar()
        case "2":
            personas_info()
            total()
            print(f"total de usuarios: {len(userinfo)}")
            print(f"total de cargos registrados: {len(cargos)}")
            print(f"total de departamentos: {len(departamentos)}")

def personas_info():
    guardados=[]
    for usuario in usuarios:
        nombres = usuario['nombres']
        apellidos = usuario['apellidos']
        cargo = usuario['cargo']
        departamento = usuario['departamento']
        extension = usuario['extension']
        if not(guardados.__contains__(extension)):
            userinfo.append({'nombres': nombres,'apellidos':apellidos,'cargo':cargo,'departamento':departamento})
            guardados.append(extension)
def total():
    for usuario in usuarios:
        cargo = usuario['cargo']
        departamento = usuario['departamento']
    
        if not(cargos.__contains__(cargo)):
            cargos.append(cargo)
        if not(departamentos.__contains__(departamento)):
            departamentos.append(departamento)

def presentar():
    for usuario in userinfo:
        time.sleep(2)
        print("__________________________________________________________________")
        print(" ")
        print(f"nombre: {usuario['nombres']}")
        print(" ")
        print(f"apellidos: {usuario['apellidos']}")
        print(" ")
        print(f"cargo: {usuario['cargo']}")
        print(" ")
        print(f"departamento: {usuario['departamento']}")
        print(" ")

if __name__ == "__main__":
    runner()