#!/usr/bin/env python

# Uso de sys modulo
import sys

# 'file' de STDIN
def read_input(file):
    # Cogemos palabras de cada línea
    for line in file:
        yield line.split()

def main(separator='\t'):
    # Leer datos
    data = read_input(sys.stdin)
    # Procesamos palabras
    for words in data:
        # Procesamos cada palabra
        for word in words:
            # Escribimos a salida
            print '%s%s%d' % (word, separator, 1)

if __name__ == "__main__":
    main()

#yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input wasbs:///example/data/gutenberg/davinci.txt -output wasbs:///example/wordcountout
# Visualización de la salida
#hdfs dfs -text /example/wordcountout/part-00000
