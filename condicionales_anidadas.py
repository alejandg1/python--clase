estudiantes = [
    {'nombre': 'Alejandro', 'sexo': 'M', 'carrera': 'soft', 'estado': 'Bajo',
        'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'ED', 'sexo': 'F', 'carrera': 'bio', 'estado': 'Medio Alto',
     'promedio': 99, 'asistencia': 97, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'alguien', 'sexo': 'M', 'carrera': 'soft', 'estado': 'Medio bajo',
     'promedio': 80, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Carlos', 'sexo': 'F', 'carrera': 'med', 'estado': 'Medio bajo',
     'promedio': 85, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Udyr', 'sexo': 'M', 'carrera': 'soft', 'estado': 'Medio',
     'promedio': 78, 'asistencia': 90, 'beca': False, 'deuda': 4, 'tipo': ""},
    {'nombre': 'Martha', 'sexo': 'F', 'carrera': 'soft', 'estado': 'Medio',
     'promedio': 100, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Camille', 'sexo': 'F', 'carrera': 'soft', 'estado': 'Bajo',
     'promedio': 98, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Andres', 'sexo': 'M', 'carrera': 'med', 'estado': 'Alto',
     'promedio': 70, 'asistencia': 60, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Alison', 'sexo': 'f', 'carrera': 'bio', 'estado': 'Medio',
     'promedio': 98, 'asistencia': 80, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Adrian', 'sexo': 'M', 'carrera': 'med', 'estado': 'Alto',
     'promedio': 96, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
]

# estudiantes = [
#         {'nombre': 'Kerly','carrera': 'Soft', 'sexo': 'M', 'estado': 'Medio', 'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda':23.50, 'tipo':''},
#         {'nombre': 'Andres','carrera': 'Soft', 'sexo': 'H', 'estado': 'Medio alto', 'promedio': 92, 'asistencia': 95, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Fernando','carrera': 'Soft', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 98, 'asistencia': 80, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Karla','carrera': 'Bio', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 99, 'asistencia': 98, 'beca': False,'deuda':0,'tipo':''},
#         {'nombre': 'Manuel','carrera': 'Bio', 'sexo': 'H', 'estado': 'Alto', 'promedio': 90, 'asistencia': 99, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Anna','carrera': 'Bio', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 85, 'asistencia': 93, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Brianna','carrera': 'Ali', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 88, 'asistencia': 92, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Ivan','carrera': 'Ali', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 92, 'asistencia': 90, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Tom','carrera': 'Ind', 'sexo': 'H', 'estado': 'Medio alto', 'promedio': 93, 'asistencia': 85, 'beca': False,'deuda':0, 'tipo':''},
#         {'nombre': 'Omar','carrera': 'Ind', 'sexo': 'H', 'estado': 'Alto', 'promedio': 95, 'asistencia': 89, 'beca': False,'deuda':0, 'tipo':''},
#         ]




def beca_academica():
    print("---------------------------------------------------------becas academicas------------------------------------------------------")
    for i in estudiantes:
        if i['beca'] == False:

            if 95 <= i['promedio'] <= 100:
                cumplep = True
            else:
                cumplep = False
            if 90 <= i['asistencia'] <= 100:
                cumplea = True
            else:
                cumplea = False
            if i['deuda'] == 0:
                cumpled = True
            else:
                cumpled = False
            if (cumplep & cumplea & cumpled):
                i['beca'] = True
                i['tipo'] = "A"
                print(
                    f"beca otorgada a {i['nombre']}: {i['beca']}, tipo: {i['tipo']}  ")


def beca_socioeconomica():
    print("-------------------------------------------------------becas socioeconomicas---------------------------------------------------")
    for i in estudiantes:
        if i['beca'] == False:

            if i['estado'] == "Bajo" or i['estado'] == "Medio bajo":
                socioe = True
            else:
                socioe = False
            if 80 <= i['promedio'] <= 100:
                cumplep = True
            else:
                cumplep = False
            if 90 <= i['asistencia'] <= 100:
                cumplea = True
            else:
                cumplea = False
            if i['deuda'] == 0:
                cumpled = True
            else:
                cumpled = False
            if (cumplep & cumplea & cumpled & socioe):
                i['beca'] = True
                i['tipo'] = "S"
                print(
                    f"beca otorgada a {i['nombre']}: {i['beca']}, tipo: {i['tipo']}  ")

def nobecados():
    print("-------------------------------------------------------estudiantes no becados------------------------------------------------")
    for i in estudiantes:
        if not(i['beca']):
            print(f"a el estudiante: {i['nombre']} no se le ha otorgado ninguna beca")


def run():
    beca_academica()
    beca_socioeconomica()
    nobecados()


if __name__ == "__main__":
    run()