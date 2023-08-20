import xml.etree.ElementTree as ET
from ListaDatos.Lista_Datos import ListaDatos
from ListaSenal.Lista_Senal import ListaSenal
from ListaDatos.datos import Datos
from ListaSenal.senal import Senal

def cargar_xml():
    
    try:
        
        archivo = input("\nIngrese la ruta del archivo XML : ")
    
        tree = ET.parse(archivo)
        root = tree.getroot()
    
        lista_senal_temporal = ListaSenal()
    
        for senal in root.findall('senal'):
            senal_nombre = senal.get('nombre')
            tiempo_senal = senal.get('t')
            amplitud_senal = senal.get('A')
        
            lista_datos_temporal = ListaDatos()
            lista_datos_patrones_temporal = ListaDatos()
        
            for dato in senal.findall('dato'):
                tiempo_dato = dato.get('t')
                amplitud_dato = dato.get('A')
                valor = dato.text
                
                nuevo = Datos(tiempo_dato, amplitud_dato, valor)
                lista_datos_temporal.agregar(nuevo)
                
                if tiempo_dato == '':
                    tiempo_dato = 0
                
                if amplitud_dato == '':
                    amplitud_dato = 0
                
                if valor == None:
                    valor = 0
                    
                nuevo = Datos(tiempo_dato, amplitud_dato, valor)

                if tiempo_dato != '' and amplitud_dato != '':
                    lista_datos_patrones_temporal.agregar(nuevo)
                
            lista_senal_temporal.agregar(Senal(senal_nombre, tiempo_senal, amplitud_senal, lista_datos_temporal, lista_datos_patrones_temporal))
    
        lista_senal_temporal.imprimir_listaSenal()
        lista_senal_temporal.grafica_lista_patrones()
        
    except FileNotFoundError:
        
        print("\nNo se pudo cargar el archivo XML, verifique la ruta ingresada")


            
                
                
            
            

    


