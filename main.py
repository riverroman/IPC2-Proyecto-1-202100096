from app import cargar_xml

print('======================')
print(' PROYECTO 1 - IPC 2   ')
print('======================\n')

def main():
    
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
            cargar_xml()
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            print('\nPrograma Finalizado.....!\n')
            break
        else:
            print('\nOpcion no valida!')
            continue
        
main()






