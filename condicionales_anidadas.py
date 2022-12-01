estudiantes = [
    {'nombre': 'Alejandro', 'sexo': 'M', 'carrera': 'soft', 'estado S.E.': 'bajo',
        'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'ED', 'sexo': 'F', 'carrera': 'bio', 'estado S.E.': 'medio alto',
     'promedio': 99, 'asistencia': 97, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'alguien', 'sexo': 'M', 'carrera': 'soft', 'estado S.E.': 'medio bajo',
     'promedio': 80, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Carlos', 'sexo': 'F', 'carrera': 'med', 'estado S.E.': 'medio bajo',
     'promedio': 85, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Udyr', 'sexo': 'M', 'carrera': 'soft', 'estado S.E.': 'medio',
     'promedio': 78, 'asistencia': 90, 'beca': False, 'deuda': 4, 'tipo de beca': ""},
    {'nombre': 'Martha', 'sexo': 'F', 'carrera': 'soft', 'estado S.E.': 'medio',
     'promedio': 100, 'asistencia': 100, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Camille', 'sexo': 'F', 'carrera': 'soft', 'estado S.E.': 'bajo',
     'promedio': 80, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Andres', 'sexo': 'M', 'carrera': 'med', 'estado S.E.': 'alto',
     'promedio': 70, 'asistencia': 60, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Alison', 'sexo': 'f', 'carrera': 'bio', 'estado S.E.': 'medio',
     'promedio': 98, 'asistencia': 80, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
    {'nombre': 'Adrian', 'sexo': 'M', 'carrera': 'med', 'estado S.E.': 'alto',
     'promedio': 96, 'asistencia': 90, 'beca': False, 'deuda': 0, 'tipo de beca': ""},
]


def beca_academica():
    print("---------------------------------------------------------becas academicas------------------------------------------------------")
    for i in estudiantes:
        if i['tipo de beca'] == "":
            sin_beca = True
        else:
            sin_beca = False
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
        if (cumplep & cumplea & cumpled & sin_beca):
            i['beca'] = True
            i['tipo de beca'] = "a"
            print(
                f"beca otorgada a {i['nombre']}: {i['beca']}, tipo: {i['tipo de beca']}  ")
        


def beca_socioeconomica():
    print("-------------------------------------------------------becas socioeconomicas---------------------------------------------------")
    for i in estudiantes:
        if i['tipo de beca'] == "":
            sin_beca = True
        else:
            sin_beca = False
        if i['estado S.E.'] == "bajo" or i['estado S.E.'] == "medio bajo":
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
        if (cumplep & cumplea & cumpled & sin_beca & socioe):
            i['beca'] = True
            i['tipo de beca'] = "s.e."
            print(
                f"beca otorgada a {i['nombre']}: {i['beca']}, tipo: {i['tipo de beca']}  ")


def run():
    beca_socioeconomica()
    beca_academica()


if __name__ == "__main__":
    run()