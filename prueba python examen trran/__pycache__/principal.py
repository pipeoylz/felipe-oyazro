import funciones as fn

alumnos = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]

credito_alumnos = {}

while True:
    print("bienvenido\n1. inicializar los creditos\n2. a signacion de credito\n3. clasificasion de creditos\n4. calcular estasdistias credito\n.5generacion de reporte\n6. salir ")

    opc = int(input("ingrese una opcion: "))

    if opc==1:
        credito_alumnos = {alumno : 0 for alumno in alumnos}

    elif opc==2:
        if not credito_alumnos:
            print("primero de inicializar los crditos")
        else:
            credito_alumnos = fn.asignar_credito(alumnos)

    elif opc==3:
        if credito_alumnos:
            fn.clasificacion_credito(credito_alumnos)
        else:
            print("primero debes incializar los creditos")

    elif opc==4:
        if credito_alumnos:
            max_credito,min_credito,promedio_credito  = fn.calculo_credito(credito_alumnos)

            if max_credito is not None:
                print("el maximo credito dado es de",max_credito)
                print("el credito minimo dado es de ",min_credito)
                print("el promedio de los creditos dados es de ",promedio_credito)
        
        else:
            print("primero debes inicalizar los creditos")

    elif opc==5:
        if credito_alumnos:
            fn.generar_reporte(credito_alumnos)
        else:
            print("primero debe incializar los creditos")
    elif opc==6:
        print("que tenga un buen dia")
        break
        


    
