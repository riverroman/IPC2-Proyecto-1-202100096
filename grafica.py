def grafica_inicial(lista):
    
    print('\n======================')
    print('   MENU GRAFICA       ')
    print('======================')
    
    print('\n1. Grafica Inicial')
    print('2. Grafica Corregida')
    print('2. Grafica Matriz')
    print('3. Grafica Final')
    print('4. Regresar')
    
    opcion = input('\nIngrese una opcion: ')
    
    if opcion == '1':
        
        busqueda = input('\nIngrese el nombre de la senal: ')
    
        senal_encontrada = lista.buscar(busqueda)
    
        if senal_encontrada is not None:
            print(f'\nSe encontro la senal = {busqueda}')
            
            senal_encontrada.lista_datos.graficar(senal_encontrada.nombre,
                                                senal_encontrada.tiempo,
                                                senal_encontrada.amplitud)
        else:
            print(f'\nNo se encontro la senal = {busqueda}')
    elif opcion == '2':
        
        busqueda = input('\nIngrese el nombre de la senal: ')
        
        senal_encontrada = lista.buscar(busqueda)
        
        if senal_encontrada is not None:
            print(f'\nSe encontro la senal = {busqueda}')
            
            senal_encontrada.lista_datos_patrones.graficar(senal_encontrada.nombre, 
                                                        senal_encontrada.tiempo,
                                                    senal_encontrada.amplitud)
        else:
            print(f'\nNo se encontro la senal = {busqueda}')
            
    elif opcion == '3':
        pass
    elif opcion == '4':
        return
    else:
        print('\nOpcion no valida!')


    