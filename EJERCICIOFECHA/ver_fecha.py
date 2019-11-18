from dummy_data import dia, mes, anio, hora, minutos
import datetime


def ver_futuro_pasado():
    now = datetime.datetime.now()

    if now.year > anio or now.month > mes:
        return 'pasado'

    if now.year == anio and now.month == mes:
        if now.day > dia:
            return 'pasado'
        else:
            if now.hour > hora:
                return 'pasado'
            else:
                if now.minute > minutos:
                    return 'pasado'
    
    





    if now.year > anio:
        anio_futuro = True
        return 'pasado'
    else:
        if now.year < anio:
            anio_pasado = True
            return 'futuro'
        else:
            anio_actual = True
            return 'actual'

    if now.month > mes:
        mes_futuro = True
        return 'pasado'
    else:
        if now.month < mes:
            mes_pasado = True
            return 'futuro'
        else:
            mes_actual = True
            return 'actual'


    if now.day > dia:
        dia_futuro = True
        return 'pasado'
    else:
        if now.day < dia:
            dia_pasado = True
            return 'futuro'
        else:
            dia_actual = True
            return 'actual'


    if now.hour > hora:
        hora_futuro = True
        return 'pasado'
    else:
        if now.hour < hora:
            hora_pasado = True
            return 'futuro'
        else:
            hora_actual = True
            return 'actual'


    if now.minute > minutos:
        minutos_futuro = True
        return 'futuro'
    else:
        if now.minute < minutos:
            minutos_pasado = True
            return 'futuro'
        else:
            minutos_actual = True
            return 'actual'


resultado = ver_futuro_pasado()

if resultado == 'futuro':
    print(" La fecha introducida es anterior a la actual ")
if resultado == 'pasado':
    print(" La fecha introducida es posterior a la actual ")
if resultado == 'actual':
    print(" La fecha introducida es la actual ")
