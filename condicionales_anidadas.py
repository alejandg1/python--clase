estudiantes = [
    {'nombre': 'Alejandro', 'sexo': 'M', 'carrera': 'soft', 'estado.': 'bajo',
        'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'ED', 'sexo': 'F', 'carrera': 'bio', 'estado.': 'medio alto',
     'promedio': 99, 'asistencia': 97, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'alguien', 'sexo': 'M', 'carrera': 'soft', 'estado.': 'medio bajo',
     'promedio': 80, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Carlos', 'sexo': 'F', 'carrera': 'med', 'estado.': 'medio bajo',
     'promedio': 85, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Udyr', 'sexo': 'M', 'carrera': 'soft', 'estado.': 'medio',
     'promedio': 78, 'asistencia': 90, 'beca': False, 'deuda': 4, 'tipo': ""},
    {'nombre': 'Martha', 'sexo': 'F', 'carrera': 'soft', 'estado.': 'medio',
     'promedio': 100, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Camille', 'sexo': 'F', 'carrera': 'soft', 'estado.': 'bajo',
     'promedio': 98, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Andres', 'sexo': 'M', 'carrera': 'med', 'estado.': 'alto',
     'promedio': 70, 'asistencia': 60, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Alison', 'sexo': 'f', 'carrera': 'bio', 'estado.': 'medio',
     'promedio': 98, 'asistencia': 80, 'beca': False, 'deuda': 0, 'tipo': ""},
    {'nombre': 'Adrian', 'sexo': 'M', 'carrera': 'med', 'estado.': 'alto',
     'promedio': 96, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo': ""},
]


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

            if i['estado.'] == "bajo" or i['estado.'] == "medio bajo":
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
