#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:56:02 2021

@author: alfaro
"""

def medidas_hoja_A(N):
    if N == 0:
        medidas = (841,1189)
    else:
        aux = medidas_hoja_A(N-1)
        medidas = (aux[1]//2, aux[0])
    return medidas
    
if __name__ == '__main__':
    print(medidas_hoja_A(6))