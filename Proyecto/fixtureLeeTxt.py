#Importaciones
import argparse
from time import sleep
from random import shuffle

#Importaciones Locales
from fixtureTorneo import ListaFixture

# Lectura del txt
""" Obtener participantes del archivo """
archivo= open("example.txt", "r")
# Quita cada linea para deshacerte de /n
participantes = [l.strip() for l in archivo.readlines()]
archivo.close()

shuffle(participantes)

fixgen = ListaFixture(participantes)
fixgen()
fixgen.imprimir_fixture()