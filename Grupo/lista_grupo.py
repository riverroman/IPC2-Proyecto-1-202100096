from Grupo.nodo_grupo import Nodo


class lista_grupos:
    def __init__(self):
        self.cabeza = None
        self.contador_grupos = 0
        
    def agregar(self,grupo):
        if self.cabeza is None:
            self.cabeza = Nodo(grupo=grupo)
            self.contador_grupos += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(grupo=grupo)
        self.contador_grupos += 1
        
    def recorrer_imprimir_grupos(self):
        print('===================================================')
        
        actual = self.cabeza
        
        while actual != None:
            
            print('Grupo: ', actual.grupo.el_grupo, 
                'Cadena-Grupo: ', actual.grupo.cadena_grupo)

            actual = actual.siguiente
            
        print('===================================================')