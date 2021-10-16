#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alfaro
"""

import os
import pandas as pd


#leemos las dos datasets y los almacenamos en forma de DataFrames
fname_parques = os.path.join('..','Data','arbolado-en-espacios-verdes.csv')
df_parques = pd.read_csv(fname_parques)
fname_veredas = os.path.join('..','Data',
                'arbolado-publico-lineal-2017-2018.csv')
df_veredas = pd.read_csv(fname_veredas)

#creamos una lista de columnas con los nombres de los valores de altura y 
#diametro segun cada dataset
col_parques = ['altura_tot', 'diametro']
col_veredas = ['altura_arbol', 'diametro_altura_pecho']

#a partir de los dos primeros DF creamos un Df nuevo filtrando por nombre 
#cientfico
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][
                   col_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'
                   ][col_veredas].copy()
#estandariamos los nombres para evitar confusiones
df_tipas_veredas = df_tipas_veredas.rename(columns = {'altura_arbol': 
                   'altura_tot', 'diametro_altura_pecho': 'diametro'})

#agregamos una columna llamada ambiente cuyo valor es 'parque' o 'vereda' 
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

#unimos ambos DF con la informacion distingada por el valor de la columna 
#'ambiente'
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#creamos un boxplot para los diametros distinguidos por ambientes 
df_tipas.boxplot('diametro', by = 'ambiente')

#creamos un boxplot para las alturas distinguidas por ambientes 
df_tipas.boxplot('altura_tot', by = 'ambiente')


#Para hacer el analisis para otras especies conviene usar una funcion que 
#realice el mismo procedimiento y reciba como argumento los nombre cientifico
#usados en cada archivo