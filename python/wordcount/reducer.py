#!/usr/bin/env python

# importamos módulos
from itertools import groupby
from operator import itemgetter
import sys

# 'file' de STDIN
def read_mapper_output(file, separator='\t'):
    # Cada línea
    for line in file:
        # Split por cada caracter separador
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # Leemos datos usando read_mapper_output
    data = read_mapper_output(sys.stdin, separator=separator)
    # Conjunto de palabras y conteo en 'group'

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            # Para cada palabra incluimos la veces que aparece
            #   en 'group' y creamos el total
            total_count = sum(int(count) for current_word, count in group)
            # Escribimos a salida
            print "%s%s%d" % (current_word, separator, total_count)
        except ValueError:
            # Excepción cuando no es número
            pass

if __name__ == "__main__":
    main()


#yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input wasbs:///example/data/gutenberg/davinci.txt -output wasbs:///example/wordcountout
# Visualización de la salida
#hdfs dfs -text /example/wordcountout/part-00000
