from .NodoSenal import NodoSenal
class ListaSenal:
    def __init__(self):
        self.cabeza = None
        self.contador_senal = 0
        
    def agregar(self,senal):
        if self.cabeza is None:
            self.cabeza = NodoSenal(senal=senal)
            self.contador_senal += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoSenal(senal=senal)
        self.contador_senal += 1
        
    def imprimir_listaSenal(self):
        print('\nNumero de Senales:', self.contador_senal, '\n')
        print('========================================')
        actual = self.cabeza
        while actual != None:
            print('Nombre:',actual.senal.nombre, 'Tiempo:', actual.senal.tiempo, 'Amplitud:', actual.senal.amplitud)
            actual.senal.lista_datos.imprimir_listaDatos()
            actual.senal.lista_datos_patrones.imprimir_listaDatos()
            actual = actual.siguiente
    
    def grafica_original(self):
        
        actual = self.cabeza
        while actual != None:
            
            actual.senal.lista_datos.graficar(actual.senal.nombre,
                                            str(actual.senal.tiempo),
                                            str(actual.senal.amplitud))
            actual = actual.siguiente
            
    def grafica_lista_patrones(self):
        actual = self.cabeza
        while actual != None:
            
            nombre_archivo = f"{actual.senal.nombre}.png"
            actual.senal.lista_datos_patrones.graficar(actual.senal.nombre, 
                                                    str(actual.senal.tiempo), 
                                                    str(actual.senal.amplitud), 
                                                    nombre_archivo)

            actual = actual.siguiente
    
    def buscar(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual.senal.nombre == nombre:
                return actual.senal
            actual = actual.siguiente
        return None
    
    def agrupar_patrones(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual.senal.nombre == nombre:
                actual.senal.lista_datos.agrupar_patrones()
                return actual.senal
            actual = actual.siguiente
        return None
    
    
    
    
    
        
                
            

        
        
        
    