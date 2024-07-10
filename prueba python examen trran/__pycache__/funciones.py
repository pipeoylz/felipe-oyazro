import random
import csv

def asignar_credito(alumnos):
    credito_alumno = {}

    for alumno in alumnos:
        credito = random.randint(50,200)
        credito_alumno[alumno] = credito
    print("crditos asignados corectamente")
    print(credito_alumno)
    return(credito_alumno)

def clasificacion_credito(credito_alumnos):

    menor_100 = {}
    entre_100_150 = {}
    mayor_150 = {}


    for alumno,credito in credito_alumnos.items():
        if credito < 100:
            menor_100[alumno] = credito
        elif credito <= 150:
            entre_100_150[alumno] = credito
        
        else:
            mayor_150[alumno] = credito
        
    print("creditos menores a 100",len(menor_100))
    for alumno,credito in menor_100.items():
        print(alumno,': $',credito)


def calculo_credito(credito_alumnos):
    creditos = list(credito_alumnos.values())

    if not credito_alumnos:
        print("primero debes incializar los creditos")
        return None,None,None
    
    max_credito = max(creditos)
    min_credito = min(creditos)
    promedio_credito = sum(creditos) / len(creditos)

    return max_credito,min_credito,promedio_credito    

def generar_reporte(credito_alumnos):

    with open('reporte_credito.csv','w') as archivo:
        escritor = csv.writer(archivo,delimiter=',')

        escritor.writerow(['nombre alumno','credito'])

        for alumno,credito in credito_alumnos.items():
            escritor.writerow([alumno,credito])
    print("reporte generado correctamente")
    

    