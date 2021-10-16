#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alfaro
"""

import os
import sys


def archivos_png(directorio):
    archivos = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-4:] == ".png":
                archivos.append(name)
    return archivos
    
    
    
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'nombre del \
                         directorio')
    print(archivos_png(sys.argv[1]))