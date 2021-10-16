#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alfaro
"""

from datetime import datetime

def vida_en_segundos(fecha_nac_cadena):
    '''devuelve la cantidad de segundos que viviste (asumiendo que naciste a 
    00 hs de tu fecha de nacimiento).
    Recibe como entrada una cadena en formato 'dd/mm/AAAA' (día, mes, año con 
    2, 2 y 4 dígitos, separados con barras normales)
    Devuelve un float'''
    
    #convierto la cadena a un objeto datetime
    fecha_nac = datetime.strptime(fecha_nac_cadena, '%d/%m/%Y')
    #obtengo el timedelta
    dif_tiempo = datetime.now() - fecha_nac
    #paso la diferencia de timepo a segundos
    dif_tiempo_segundos = dif_tiempo.total_seconds()
    
    #redondeo el valor a dos decimales y devuelvo la cantidad en segundos
    return round(dif_tiempo_segundos,2)

if __name__ == "__main__":
    fecha_nacimiento = '14/05/1997'
    print(vida_en_segundos(fecha_nacimiento))