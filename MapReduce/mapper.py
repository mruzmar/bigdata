#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Programa mapper.py"""

import sys
import re

# la entrada de datos llega desde STDIN (standard input)
for line in sys.stdin:
    #eliminamos los espacios en blanco iniciales y finales
    line = line.strip()
    # dividimos la línea en palabras
    words = line.split()
    # Para cada palabra encontrada
    for word in words:
    	# antes limpiamos
    	word = re.sub('[!@#$,;.-?¿¡]', '', word)
        # escribir los resultados en STDOUT (salida estándar);
        print '%s\t%s' % (word, 1)