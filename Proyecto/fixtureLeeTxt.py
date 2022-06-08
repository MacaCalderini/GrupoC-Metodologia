
#Importaciones
import argparse
from time import sleep
from random import shuffle

#Importaciones Locales
from fixtureTorneo import ListaFixture

# Lectura del txt

def get_part(file_name):
    """ Obtener participantes del archivo """
    try:
        with open(file_name) as tf:
            # Quita cada linea para deshacerte de /n
            participantes = [l.strip() for l in tf.readlines()]
    except FileNotFoundError:
        print("No se pudo ubicar el archivo. Inténtalo de nuevo!")
        sleep(4)   #Permitir que el usuario lea el mensaje anterior
        quit()
    else:
        return participantes


def main():

    parser = argparse.ArgumentParser(
        description=" ListaFixture"
    )

    # Añadir parametros
    parser.add_argument('file_name', help="team list")

    # Analizar los argumentos
    args = parser.parse_args()

    # Obtener el nombre del archivo
    file_name = args.file_name

    # Asegurar extension agregada
    if file_name[-4:] != '.txt': file_name += '.txt'

    participantes = get_part(file_name)
    shuffle(participantes)

    fixgen = ListaFixture(participantes)
    fixgen()
    fixgen.imprimir_fixture()


if __name__ == "__main__":
    main()
