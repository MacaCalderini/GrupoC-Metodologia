

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


    def listaDePartidasR(self):    # devuelve una lista de partidas por ronda
         listaRondas =[]
         i = 0
      #   while i < self.partidas_por_ronda:
      #     fixture = Fixture(self.participantes[i], self.participantes[-i-1])
         #    listaRondas.append(fixture)
          #  i +=1
        # return listaRondas
