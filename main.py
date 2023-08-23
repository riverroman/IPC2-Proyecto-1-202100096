from app import cargar_xml
from Datos.datos import informacion_personal
from grafica import grafica_inicial
from time import sleep
from progress.bar import Bar

print('======================')
print(' PROYECTO 1 - IPC 2   ')
print('======================\n')

def main():
    
    lista_senal = None
    
    while True:
        
        print('\n======================')
        print('   MENU PRINCIPAL     ')
        print('======================') 
        
        print('\n1. Cargar Archivo')
        print('2. Procesar Archivo')
        print('3. Escribir Archivo de Salida')
        print('4. Mostrar Datos del Estudiante')
        print('5. Generar Grafica')
        print('6. Inicializar Sistema')
        print('7. Salir\n')
        
        opcion = input('Ingrese una opcion: ')
        
        if opcion == '1':
            lista_senal = cargar_xml()
        elif opcion == '2':
            carga()
        elif opcion == '3':
            pass
        elif opcion == '4':
            informacion_personal()
        elif opcion == '5':
            if lista_senal is not None:
                grafica_inicial(lista_senal)
            else:
                print('\nPrimero debe cargar un archivo XML')
                continue
        elif opcion == '6':
            pass
        elif opcion == '7':
            print('\nPrograma Finalizado.....!\n')
            break
        else:
            print('\nOpcion no valida!')
            continue
        
def carga():
    
    print('\n========================================================')
    
    with Bar('Generando...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()
            
    print('========================================================')
    
main()



