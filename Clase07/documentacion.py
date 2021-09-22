#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def valor_absoluto(n):
    """Obtiene el valor absoluto de un numero
    Precondicion: n debe ser un numero
    Poscondicion: devuelve el valor absoluto de n
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """Suma todos los numeros pares que pertenecen a un iterador l.
    Precondicion: l debe ser una iterador cuyos elementos sean 
    numeros, en el caso de diccionarios las claves deben ser numeros
    Poscondicion: devuelve la suma total de todos los elementos pares
    """
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0
    return res
    # EL invariante en el ciclo es la suma de todos los elementos ya 
    # recorridos

def veces(a, b):
    """Suma b veces el numero a.
    Precondicion: a debe ser un numero y b un entero no negativo
    Poscondicion: devuelve a * b
    """
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res
    # el invariante en el ciclo es el numero de veces restantes que se debe
    # sumar a


def collatz(n):
    """Cuenta los pasos necesarios para realizar la conjetura de Collatz para
    un numero n hasta obtener 1.
    Precondicion: n es un numero entero y postivo
    Poscondicion: se devuelve el numero de pasos realizados hasta obtener 1
    siguiendo la conjetura de collatz"""
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
    # El invariante en el ciclo es res, el cual el numero de pasos para ir
    # desde el valor inicial de n hasta el valor actual de n
