from random import choice
class Tablero:
    def __init__(self):
        self.tablero = self.crear_tablero()
        self.lista_columnas_vacias = []

    def crear_tablero(self):
        nuevo_tablero = [[0 for col in range(7)] for row in range(6)] # list comprehension nested
        return nuevo_tablero
    
    def mostrar_tablero(self):
        print('Tablero actual:')
        print('-------------')
        for row in self.tablero:
            for col in row:
                print(f'{col}', end=' ')
            print()
        print('-------------')
        print((1), (2), (3), (4), (5), (6), (7))

    def calcular_columnas_disponibles(self): 
        self.lista_columnas_vacias = []
        for c in range(7):  
            if self.tablero[0][c] == 0:  
                self.lista_columnas_vacias.append(c + 1)
        return self.lista_columnas_vacias
        ''''
        for c in range(6, -1, -1):  # Iteramos de 6 a 0 para las columnas
            for r in range(5, -1, -1):
                lina_actual = self.tablero[r][c]
                if lina_actual == 0 and (c - 1) not in self.lista_columnas_vacias:
                    self.lista_columnas_vacias.append(c + 1)
                    break
        return self.lista_columnas_vacias
        '''

class Jugador:
    def __init__(self, ficha: int, tablero: Tablero, es_maquina=False ):
        self.nombre = f'Jugador {ficha}'
        self.ficha = ficha
        self.es_maquina = es_maquina
        self.tablero = tablero
        self.posicion = None

    def __jugada(self):
        try: 
            self.posicion = input('Escriba el numero de la columna que desea colocar su ficha: ')
            self.posicion = int(self.posicion)
        
        except ValueError:
            print('La opción debe ser un número! ')           
        
        return self.posicion

    def __es_jugada_valida(self):
        return self.posicion in self.tablero.calcular_columnas_disponibles()

    def __solicitar_jugada_valida(self):
        while not self.__es_jugada_valida():
            self.__jugada()

    def actualizar_tablero(self):
        self.__jugada()
        if self.__es_jugada_valida():
            for i in range(5, -1, -1):
                if self.tablero.tablero[i][self.posicion - 1] == 0:
                    self.tablero.tablero[i][self.posicion - 1] = self.ficha
                    break
        else: self.__solicitar_jugada_valida()

class Maquina(Jugador):
    def __init__(self, ficha, tablero):
        super().__init__(ficha, tablero, True )

    def __jugada(self):
        self.posicion = choice(self.tablero.calcular_columnas_disponibles())
        return self.posicion

    def actualizar_tablero(self):
        self.__jugada()
        for i in range(5, -1, -1):
            if self.tablero.tablero[i][self.posicion - 1] == 0:
                self.tablero.tablero[i][self.posicion - 1] = self.ficha                    
                break 

class Juego:
    def __init__(self):
        tablero = Tablero()
        self.tablero = tablero
        self.jugador1 = Jugador(1, self.tablero)
        self.jugador2 = self.segundo_jugador()
        self.tablero.mostrar_tablero()
        self.jugador_actual = choice([self.jugador1, self.jugador2])
        self.estado_del_juego = 'en marcha'
        self.juego()

    def __es_maquina(self):
        while True: 
            es_maquina = input('Seleccione el modo de juego: (1) Humano x Humano (2) Humano x Máquina. ')
            try:
                es_maquina = int(es_maquina)
                if es_maquina == 1:
                    return False
                elif es_maquina == 2:
                    return True
                else:
                    while es_maquina != 1 and es_maquina != 2:
                        es_maquina = int(input('Seleccione una opción válida! (1) Humano x Humano (2) Humano x Máquina. '))
                    return True
            
            except ValueError:
                print('Escriba apenas un número!')

    def segundo_jugador(self):
        if self.__es_maquina():
            return Maquina(2, self.tablero) 
        return Jugador(2, self.tablero)
    
    def cambiar_jugador(self):
        if self.jugador_actual == self.jugador1:
            self.jugador_actual = self.jugador2
        else:
            self.jugador_actual = self.jugador1
    
    def cambiar_estado_del_juego(self):
        self.estado_del_juego = 'terminado' 
        
    def verificar_diagonal(self, inicio_row, inicio_col): 
        row, col = inicio_row, inicio_col 
        contador = 0
        while row >= 0 and col < 7:
            if self.tablero.tablero[row][col] == self.jugador_actual.ficha:
                contador += 1
                if contador == 4:
                    return True
            else: 
                contador = 0
            row -= 1
            col += 1
        return False
 
    def verificar_diagonal_inversa(self, inicio_row, inicio_col): 
        row, col = inicio_row, inicio_col 
        contador = 0
        while row >= 0 and col < 7:
            if self.tablero.tablero[row][col] == self.jugador_actual.ficha:
                contador += 1
                if contador == 4:
                    return True
            else: 
                contador = 0
            row -= 1
            col -= 1
        return False

    def hay_ganador_diagonal(self):
        # derecha a izquierda
        for col in range(3, 7): # abajo
            if self.verificar_diagonal_inversa(5, col):
                return True
        
        for row in range(4, 4): # lado
            if self.verificar_diagonal_inversa(row, 6):
                return True

        # izquierda a derecha
        for col in range(6): # abajo 
            if self.verificar_diagonal_inversa(5, col):
                return True
           
        for row in range(3, 5): # lado
            if self.verificar_diagonal(row, 0):
                return True
        return False
    
    def hay_ganador_linea(self):
        for i in range(5, -1, -1): # verifica linea de abajo para arriba
            contador = 0
            for j in range(7): 
                if self.tablero.tablero[i][j] == self.jugador_actual.ficha:
                    contador += 1
                    if contador == 4:
                        return True
                else: contador = 0
        return False
    
    def hay_ganador_coluna(self):
        for col in range(7): # verifica coluna
            contador = 0
            for lina in range(5, -1, -1):
                if self.tablero.tablero[lina][col] == self.jugador_actual.ficha:
                    contador += 1
                    if contador == 4:
                        return True
                else: contador = 0
        return False
    
    def verificar_ganador(self):
        return self.hay_ganador_coluna() or self.hay_ganador_linea() or self.hay_ganador_diagonal()    
        
    def juego(self):
        while self.estado_del_juego == 'en marcha':
            print(self.jugador_actual.nombre, " te toca!", sep=":")
            self.jugador_actual.actualizar_tablero()
            if self.verificar_ganador():
                self.tablero.mostrar_tablero()
                self.cambiar_estado_del_juego()
                print(f'Felicidades {self.jugador_actual.nombre}! Has ganado!')
                
            
            elif not self.tablero.calcular_columnas_disponibles():
                self.tablero.mostrar_tablero()
                self.cambiar_estado_del_juego()
                print('Há sido un empate!')
                
            else:
                self.cambiar_jugador()
                self.tablero.mostrar_tablero()
        
juego = Juego()