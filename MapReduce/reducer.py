#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Programa reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None


# la entrada de datos llega desde STDIN (standard input)
for line in sys.stdin:
    #eliminamos los espacios en blanco iniciales y finales
    line = line.strip()


    # analizamos y recogermos la entrada que obtuvimos de mapper.py
    word, count = line.split('\t', 1)

    # convertimos el valor de string a int
    try:
        count = int(count)
    except ValueError:
        # El valor no es numérico, no se tendrá en cuenta
        continue


    # este interruptor IF solo funciona porque Hadoop ordena la salida del map
    # por tecla (aquí: palabra) antes de pasarla al reductor
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # resultado a STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# No olvidar mostrar la última palabra si es necesario
if current_word == word:
    print '%s\t%s' % (current_word  current_count)