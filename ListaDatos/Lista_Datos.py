from .NodoDatos import NodoDatos
import os
from Patron.patron import patron

class ListaDatos:
    def __init__(self):
        self.cabeza = None
        self.contador_datos = 0
        
    def agregar(self, dato):
        if self.cabeza is None:
            self.cabeza = NodoDatos(dato=dato)
            self.contador_datos += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NodoDatos(dato=dato)
        self.contador_datos += 1

    def insertar_dato_ordenado(self, dato):
        
        nueva_celda = NodoDatos(dato=dato)
        
        self.contador_celdas = +1
        
        if self.cabeza is None:
            self.cabeza = nueva_celda
            return
        
        if dato.tiempo < self.cabeza.dato.tiempo or (
                dato.tiempo == self.cabeza.dato.tiempo and dato.amplitud <= self.cabeza.dato.amplitud):
            
            nueva_celda.siguiente = self.cabeza
            self.cabeza = nueva_celda
            return
        
        actual = self.cabeza
        
        while actual.siguiente is not None and (
                dato.tiempo >  actual.siguiente.dato.tiempo or (
                    dato.tiempo == actual.siguiente.dato.tiempo and dato.amplitud > actual.siguiente.dato.amplitud)):
            
            actual = actual.siguiente
            
        nueva_celda.siguiente = actual.siguiente
        actual.siguiente = nueva_celda
        

    def imprimir_listaDatos(self):
        print('========================================')
        actual = self.cabeza
        while actual != None:
            print('Tiempo: ', actual.dato.tiempo, 'Amplitud', actual.dato.amplitud , 'Valor: ', actual.dato.valor)
            actual = actual.siguiente
            
    def graficar(self,nombre_senal,tiempo,amplitud):
        
        f = open('bb.dot','w')
        
        text = """
        
            digraph G {"Tiempo="""+tiempo+"""","Amplitud="""+amplitud+""""->" """ "Nombre Senal: " +nombre_senal+ """" bgcolor="white" style="filled"
            subgraph cluster_1 { fillcolor="#07c7a0" style="filled"
            node [shape=box3d fillcolor="gray" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="1" cellspacing="10" cellpadding="10" style="dotted" bgcolor="white">\n"""
            
        actual = self.cabeza
        sentinela_filas = actual.dato.tiempo
        fila_iniciada = False
        
        while actual != None:
            
            if sentinela_filas != actual.dato.tiempo:
                
                sentinela_filas = actual.dato.tiempo
                
                fila_iniciada = False
                
                text += """</TR>\n"""
            
            if fila_iniciada == False:
                
                fila_iniciada = True
                
                text += """<TR>"""
                
                text += """<TD border="1" bgcolor="#90827b">""" + str(actual.dato.valor) + """</TD>\n"""
            
            else:
                
                text += """<TD border="1" bgcolor="#90827b" gradientangle="315">""" + str(actual.dato.valor) + """</TD>\n"""
            
            actual = actual.siguiente
            
        text+=""" </TR></TABLE>>];
                }
                }\n"""
                
        f.write(text)
        f.close()
        
        comando_dot = f'dot -Tpng bb.dot -o "img/Grafico-{nombre_senal}.png"'
        os.system(comando_dot)

        print('\nGrafica Terminada!!')

    def devolver_patrones_por_nivel(self,lista_patrones_nivel):
        
        actual = self.cabeza
        sentinela_de_fila = actual.dato.tiempo
        fila_iniciada = False
        recolector_patron = ""
        
        while actual != None:
            if sentinela_de_fila != actual.dato.tiempo:
                fila_iniciada = False
                lista_patrones_nivel.agregar(patron(sentinela_de_fila,recolector_patron))
                recolector_patron = ""
                sentinela_de_fila = actual.dato.tiempo
            if fila_iniciada == False:
                fila_iniciada = True
                recolector_patron += str(actual.dato.valor)+"-"
            else:
                recolector_patron += str(actual.dato.valor)+"-"
            
            actual = actual.siguiente
        
        lista_patrones_nivel.agregar(patron(sentinela_de_fila, recolector_patron))
        
        return lista_patrones_nivel
                
    def devolver_cadena_por_grupo(self, grupo):
        
        string_resultado = ""
        string_temporal = ""
        buffer = ""
        
        for digito in grupo:
            
            if digito.isdigit():
                buffer += digito
            else:
                string_temporal = ""
                #Aca se recorre la lista
                actual = self.cabeza
                while actual != None:
                    if actual.dato.tiempo == str(buffer):
                        string_temporal += actual.dato.valor+","
                    actual = actual.siguiente
                string_resultado += string_temporal + "\n"
                buffer = ""
                
        return string_resultado
                            
            
            
                
                
                
        
        
        
        
        