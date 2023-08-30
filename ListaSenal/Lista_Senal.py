from .NodoSenal import NodoSenal
from Grupo.grupo import grupo
import xml.etree.ElementTree as ET

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


    def calcular_los_patrones(self, nombre_senal):
        
        actual = self.cabeza
        
        while actual != None:
            
            if actual.senal.nombre == nombre_senal:
                
                actual.senal.lista_patrones_nivel = actual.senal.lista_datos_patrones.devolver_patrones_por_nivel(actual.senal.lista_patrones_nivel)
                
                actual.senal.lista_patrones_nivel.recorrer_imprimir()
                
                lista_patrones_temporal = actual.senal.lista_patrones_nivel
                grupos_sin_analizar = lista_patrones_temporal.encontrar_coincidencias()
                
                print(grupos_sin_analizar)
                
                buffer = ""
                
                for digito in grupos_sin_analizar:

                    if digito.isdigit() or digito == ",":
                        buffer += digito
                        
                    elif digito == "-" and buffer != "":
                        cadena_grupo = actual.senal.lista_datos.devolver_cadena_por_grupo(buffer)
                        actual.senal.lista_grupos.agregar(grupo=grupo(buffer, cadena_grupo))
                        buffer = ""
                    else:
                        buffer = ""
                actual.senal.lista_grupos.recorrer_imprimir_grupos()

                return  
            actual = actual.siguiente
            
        print('\nNo se encontro la Carcel!\n')
                
    
    
    def generar_xml_salida(self):
        
        mis_senales = ET.Element('senalesReducidas')
        lista_senales = ET.SubElement(mis_senales, 'listasenal')
        
        actual = self.cabeza
        
        while actual != None:
            
            senal = ET.SubElement(lista_senales, 'senal')
            
            nombre = ET.SubElement(senal, 'Nombre')
            nombre.text = actual.senal.nombre
            
            tiempo = ET.SubElement(senal, 'Tiempo')
            tiempo.text = actual.senal.tiempo
            
            amplitud = ET.SubElement(senal, 'Amplitud')
            amplitud.text = actual.senal.amplitud
            
            actual_lista_patrones = actual.senal.lista_datos_patrones.cabeza
            lista_patrones = ET.SubElement(senal,'listaPatrones')

            while actual_lista_patrones != None:
                
                valor = ET.SubElement(lista_patrones, 'listaPatrones')
                valor.text = str(actual_lista_patrones.dato.valor)
                actual_lista_patrones = actual_lista_patrones.siguiente
            
            actual = actual.siguiente
            
            my_data = ET.tostring(mis_senales)
            my_data = str(my_data)
            self.xml_arreglado(mis_senales)
            
            
            arbol_xml = ET.ElementTree(mis_senales)
            arbol_xml.write("./Xml/salida.xml", encoding="UTF-8", xml_declaration=True)


    def xml_arreglado(self, element, indent = " "):
        
        queue = [(0, element)]
        
        while queue:
            
            level, element = queue.pop(0)
            
            children = [(level + 1, child) for child in list(element)]
            
            if children:
                
                element.text = '\n' + indent * (level + 1)
                
            if queue:
                
                element.tail = '\n' + indent * queue[0][0]
                
            else:
                
                element.tail = '\n' + indent * (level - 1)
                
            queue[0:0] = children
        
    def buscar(self, nombre):
        actual = self.cabeza
        while actual != None:
            if actual.senal.nombre == nombre:
                return actual.senal
            actual = actual.siguiente
        return None
    
    
    
    
    
        
                
            

        
        
        
    