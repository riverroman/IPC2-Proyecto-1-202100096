from Patron.nodo_patron import Nodo

class lista_patrones:
    def __init__(self):
        self.cabeza = None
        self.contador_patrones = 0
        
    def agregar(self, patron):
        if self.cabeza is None:
            self.cabeza = Nodo(patron=patron)
            self.contador_patrones += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(patron=patron)
        self.contador_patrones += 1
        
    def recorrer_imprimir(self):
        
        print('======================================================')
        
        actual = self.cabeza
        
        while actual != None:
            print('Nivel: ', actual.patron.nivel, 
                'Cadena: ', actual.patron.cadena_patron)

            actual = actual.siguiente
            
        print('======================================================')
        
    
    def eliminar(self, nivel):
        
        actual = self.cabeza
        anterior = None
        
        while actual and  actual.patron.nivel != nivel:
            anterior = actual
            actual = actual.siguiente
            
        if anterior is None:
            self.cabeza = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
        
            
    def encontrar_coincidencias(self):

        resultado = " " 
        
        while self.cabeza:
            actual = self.cabeza
            temp_string = ""
            temp_niveles =   ""
            
            while actual:
                if actual.patron.cadena_patron == self.cabeza.patron.cadena_patron:
                    temp_niveles += (actual.patron.nivel)+","
                actual = actual.siguiente
                
            buffer = ""
            
            for digito in temp_niveles:
                if digito.isdigit():
                    buffer += digito
                else:
                    if buffer != "":
                        self.eliminar(buffer)
                        buffer=""
                    else:
                        buffer = ""
            
            resultado += temp_niveles + "--"
        return resultado            
            
            
            
            
            
            
            

            
            