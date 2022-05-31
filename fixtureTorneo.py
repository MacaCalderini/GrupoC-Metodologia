

# class Fixture():


class ListaFixture():

    def __init__(self,participantes):

        if not type(participantes) is list:                                           #si participantes no es de tipo lista
            raise TypeError("Los participantes deben ser de tipo lista.")             #tiro un error o excepcion de TypeError (error de tipo)
        if len(participantes) % 2 != 0:                                               #si la longitud de la lista participantes al dividirlo por 2 el resto es distinto de 0. VER SI HACEMOS POR POTENCIA DE 2
            raise ValueError("Numero de participantes impar")                         #tiro un error o excepcion de ValueError (error de valor)

        self.participantes = participantes
        self.fixtures_list = None                                                      # es como el valor null,valor vacio.



    def num_rondas(self):    #define la cantidad de rondas VER
        return ((len(self.participantes))/2) * (len(self.participantes)-1)             #longitud de la lista participantes dividido 2 y multiplicado por la longitud de la lista
                                                                                       #menos 1. (para que no se salga del tamaño). s


    def partidas_por_ronda(self):  #devuelve la cantidad de rondas por partidos
        return  len(self.participantes) // 2                                          #longitud de la lista divido por 2 que devuelve un resultado sin decimales.


    """ Genera un round robin fixture list. """
    def __call__(self):
        fixtures_list = []

        while len(fixtures_list) < self.num_rondas(): #itera el while mientras el tamaño de la lista sea menor al numero de rondas en el torneo
            fixtures_list += self.listaDePartidasR()  #carga las partidas por ronda
            self.reordenamiento_items()               #llama al metodo para reordenar los elementos y va emparejando a los participantes

        if self.num_rondas() != len(fixtures_list):   #comprueba que el numero de rondas sea igual al tamaño de rondas por torneo, de ser diferente se lanza un msj de error
            raise ValueError(f"Numero de fixtures {self.num_fixtures} != Fixture list length{len(fixtures_list)}")

        self.fixtures_list = fixtures_list            #settea la lista

    def listaDePartidasR(self):    # devuelve una lista de partidas por ronda
         listaRondas =[]
         i = 0
      #   while i < self.partidas_por_ronda:
      #     fixture = Fixture(self.participantes[i], self.participantes[-i-1])
         #    listaRondas.append(fixture)
          #  i +=1
        # return listaRondas

    def reordenamiento_items(self):
        """ Algoritmo de reordenamiento de elementos en la lista para asegurar que las rondas no se repitan
        en el fixtures. """

        lista_copia = self.participantes[:]           #crea una copia de la lista de participantes
        for i in range(1, len(lista_copia)):          #comienza desde la posicion n°2 de la lista hasta la ultima posicion +1
            if i == 1:
                self.participantes[i] = lista_copia[-1] #si esta en la posicion 2 le asigna el ultimo valor de la lista
            else:
                self.participantes[i] = lista_copia[i - 1] #si esta en la posicion 3 le asigna el valor de la anterior posicion y asi sucesivamente
