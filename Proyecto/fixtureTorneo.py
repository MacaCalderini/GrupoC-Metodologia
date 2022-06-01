

# class Fixture():


class ListaFixture():

    def __init__(self,participantes):                                                # metodo para inicializar los atributos del objeto que creamos(constructor).

        if not type(participantes) is list:                                           #si participantes no es de tipo lista
            raise TypeError("Los participantes deben ser de tipo lista.")             #tiro un error o excepcion de TypeError (error de tipo)
        if len(participantes) % 2 != 0:                                               #si la longitud de la lista participantes al dividirlo por 2 el resto es distinto de 0. VER SI HACEMOS POR POTENCIA DE 2
            raise ValueError("Numero de participantes impar")                         #tiro un error o excepcion de ValueError (error de valor)

        self.participantes = participantes
        self.fixtures_list = None                                                      # es como el valor null,valor vacio.



    def num_rondas(self):    #define la cantidad de rondas VER
        return ((len(self.participantes))/2) * (len(self.participantes)-1)             #longitud de la lista participantes dividido 2 y multiplicado por la longitud de la lista
                                                                                       #menos 1. (para que no se salga del tamaño). s


    def partidas_por_ronda(self):   #devuelve la cantidad de rondas por partidos
        return  len(self.participantes) // 2                                          #longitud de la lista divido por 2 que devuelve un resultado sin decimales.



    def __call__(self):     #funcion invocable para crear una lista de participantes por rounds.
        fixtures_list = []

        while len(fixtures_list) < self.num_rondas():     #itera el while mientras el tamaño de la lista sea menor al numero de rondas en el torneo
            fixtures_list += self.listaDePartidasR()          #carga las partidas por ronda
            self.reordenamiento_participantes()      #llama al metodo para reordenar los elementos y va emparejando a los participantes

        if self.num_rondas() != len(fixtures_list):   #comprueba que el numero de rondas sea igual al tamaño de rondas por torneo, de ser diferente se lanza un msj de error
            raise ValueError(f"Numero de fixtures {self.num_fixtures} != Fixture list length{len(fixtures_list)}")

        self.fixtures_list = fixtures_list            #settea la lista

    def listaDePartidasR(self):  # devuelve una lista de partidas por ronda
         listaRondas =[]
         i = 0
      #   while i < self.partidas_por_ronda:
      #     fixture = Fixture(self.participantes[i], self.participantes[-i-1])
         #    listaRondas.append(fixture)
          #  i +=1
        # return listaRondas

    def reordenamiento_participantes(self):   #funcion de reordenamiento de los elemntos en la lista para asegurar que las rondas no se repitam en los fixtures

        lista_copia = self.participantes[:]    #crea una copia de la lista de participantes
        for i in range(1, len(lista_copia)):          #comienza desde la posicion n°2 de la lista hasta la ultima posicion +1
            if i == 1:
                self.participantes[i] = lista_copia[-1]          #si esta en la posicion 2 le asigna el ultimo valor de la lista
            else:
                self.participantes[i] = lista_copia[i - 1]         #si esta en la posicion 3 le asigna el valor de la anterior posicion y asi sucesivamente


    def imprimir_fixture(self):  #imprimir cada elemento de la lista

        if not self.fixtures_list:    #si no se han agregado los elementos(participantes) a la lista,
            print("Los participantes aun no han sido creados.")     #imprime un mensaje por pantalla
            return None                 #retorna un none( que es vacio)

        fixtures = self.fixtures_list[:]             # Crear una copia de la lista para garantizar que la variable de instancia no se modifique

        round_num = 1            #declara e inicializa la variable de numero de ronda
        while fixtures:
            print("-"*40)                      #imprime separador por guiones
            print(f"Round {round_num}")              # imprime el numero de la ronda
            print("-"*40)                      #imprime separador por guiones

            for _ in range(self.partidas_por_ronda()):    # recorre la lista creada con las partidas por ronda
                print(fixtures.pop(0))                           # imprime el ultimo elemento de la lista y lo elimina
            round_num += 1                      #  aumenta la variable round_num en un por cada vuelta del for
            print()