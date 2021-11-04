#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:28:43 2021

@author: alfaro
"""

def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            
            dict_fibo[n-1], dict_fibo = fibonacci_aux(n-1, dict_fibo)
            F = dict_fibo[n-1] + dict_fibo[n-2]
        return F, dict_fibo

    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 

if __name__ == '__main__':
    print(fibonacci(6))