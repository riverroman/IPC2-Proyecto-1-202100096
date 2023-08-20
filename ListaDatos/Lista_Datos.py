from .NodoDatos import NodoDatos
import os
import sys

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

    def imprimir_listaDatos(self):
        print('========================================')
        actual = self.cabeza
        while actual != None:
            print('Tiempo: ', actual.dato.tiempo, 'Amplitud', actual.dato.amplitud , 'Valor: ', actual.dato.valor)
            actual = actual.siguiente


    def graficar(self,nombre_senal,tiempo,amplitud):
        
        ruta_guardado = '/Users/riverroman/Desktop/IPC2-Proyecto-1-202100096/img/'
        nombre_archivo = f'{nombre_senal}.png'
        
        
        f = open('bb.dot','w')
        
        text = """

            digraph G {"Tiempo="""+tiempo+"""","Amplitud="""+amplitud+""""->" """ "Nombre Senal: " +nombre_senal+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster_1 { fillcolor="#07c7a0" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="3" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
            
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
                
                text += """<TD border="3" bgcolor="yellow" gradientangle="315">""" + str(actual.dato.valor) + """</TD>\n"""
            
            else:
                
                text += """<TD border="3" bgcolor="yellow" gradientangle="315">""" + str(actual.dato.valor) + """</TD>\n"""
            
            actual = actual.siguiente
            
        text+=""" </TR></TABLE>>];
                }
                }\n"""
                
        f.write(text)
        f.close()
        
        comando_dot = f'dot -Tpng bb.dot -o "{ruta_guardado}{nombre_archivo}"'
        os.system(comando_dot)

        print('\nGrafica Terminada!!')

        
        