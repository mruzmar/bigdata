from __future__ import print_function
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

# Json que contiene los datos
data = '{"nombre": "John Sanders", "ciudad": {"nombre": "Madrid", "cp": 28006}}'

# Parseo de JSon
datos = json.loads(data, object_hook=lambda d: Namespace(**d))

#recogida de datos en objetos
print (datos.nombre, datos.ciudad.nombre, datos.ciudad.cp)
