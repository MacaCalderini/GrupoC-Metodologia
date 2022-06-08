# GrupoC-Metodologia
PROYECTO DE METODOLOGÍA DE LA INVESTIGACIÓN

GRUPO C
-Barolo Ignacio
-Calderini Macarena
-Castillo Santiago
-Natel Guillermina

JUEGO:
“Mundamitas”

El proyecto se basa en un torneo de juego de damas, en el cual a través de los resultados de las partidas se va a ir creando un fixture automático hasta llegar al ganador.

LENGUAJE: 
-Python

LIBRERÍAS: 
- Pygame
- Socket

SISTEMA DE CONTROL DE VERSIONES: 
- Git

IDE: 
- Pycharm

VERSIONES:
- Python 3.10.4
- Git 2.36.0

PLANIFICACIÓN:
- Aprender reglas del juego de Damas.
- Análisis y relevamiento de las tecnologías a utilizar.
- Estudio del lenguaje, librería y sistema de versionado.
- Preparación y acondicionamiento del entorno de desarrollo (Descargas e instalación de programas/librerías requeridas).
- Diseño y Planificación de la lógica algorítmica.
- Diseñar boceto de la estructura y posibles funciones que se usarán.
- Codificación del programa por módulos(tablero, piezas, movimientos, reglas, main, fixture, menú,etc).
- Búsqueda exhaustiva de errores. Testing.
- Configuración del programa para uso en LAN.

DIVISIÓN DE TAREAS: 
El proyecto se irá trabajando de manera conjunta para poder ayudarnos a resolver problemas que se vayan planteando.

HORAS ESTIMADAS DE PROGRAMACIÓN: 
- 60-80 hrs.

CONEXIÓN LAN 
Utilizaremos para la conexión el método sockets a través del puerto TCP/IP, creando dos módulos(cliente, servidor), en el cual se irá transfiriendo la información de los movimientos que se vayan realizando durante las partidas.

Un servidor levantara un socket, el cual es una combinación de dirección de red y puerto, bind agarra este socket y lo asocia con un recurso físico(tarjeta ethernet del equipo), es decir lo dispone hacia el exterior.

Listen coloca estas construcciones en modo escucha de modo que el servidor esté atento a conexiones entrantes.

Cliente levanta un socket y luego llama al método connect(el cual se bloquea), para intentar conectarse al servidor, cuando intenta establecer conexión, el método access y connect se desbloquean, una vez hecho esto se pueden hacer dos cosas,send y recv(enviar y recibir) desde el server al cliente o viceversa, el método recv estará bloqueado hasta recibir algo del otro extremo, utilizando send.

![Conexion LAN](https://user-images.githubusercontent.com/103141738/168706927-9343c5cb-7140-4ff1-ad66-c534d71eef89.png)
