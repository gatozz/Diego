#https://github.com/gatozz/Diego.git

import csv
lista=[]

def actualizar():
    resp=input("¿Esta seguro de cambiar el nombre del equipo? (s/n) : \n")
    if resp.lower()=='s':
        for j in lista:
            print("")
    elif resp.lower()=='n':
        print("Operacion cancelada")
    else:
        print("Respuesta no valida")
        print("Por favor ingrese s/n")
        actualizar()

def estadisticas():
    cont=0
    acum=0
    puntos=0
    for j in lista:
        cont=cont+1
        acum=int(acum+j[2])
    prom=acum/cont
    print("El promedio de puntos es de : ",prom)
    for j in lista:
        p = j[2]
        if puntos<p:
            puntos=j[2]
    print("La mayor cantidad de puntos fueron : ",puntos)

while True:
    try:
        print("")
        print("Menu")
        print("")
        print("1. Aregar equipo")
        print("2. Lista de equipo")
        print("3. Actualizar nombre de equipo por id")
        print("4. Generar BBDD")
        print("5. Cargar BBDD")
        print("6. Estadisticas")
        print("0. Salir")
        print("")
        op=int(input("Ingrese una opcion : \n"))

        if op==1:
            categoria=0
            print("")
            print("Agregar equipo")
            print("")
            id=int(input("Ingrese numero de ID : \n"))
            nombre=input("Ingrese nombre : \n")
            puntos=int(input("Ingrese puntos : \n"))
            if puntos <= 40:
                       categoria="Amateur"
            if 41 <= puntos <= 80:
                       categoria="Principiante"
            if 80 <= puntos <= 120:
                       categoria="Avanzado"
            if puntos > 120:
                       categoria="Idolos"
            equipos=[id,nombre,puntos,categoria]
            lista.append(equipos)
            print("Equipo agregado correctamente")

        elif op==2:
            print("")
            print("Lista de eqipos")
            print("")
            for j in lista:
                print(f"ID : {j[0]} Nombre : {j[1]} Puntos : {j[2]} Categoria : {j[3]}")
                print(".-.-.-.-.-.-.")
            
        elif op==3:
            print("")
            print("Actualizar nombre de equipo")
            print("")
            id_actualizar=int(input("Ingrese id de equipo : \n"))
            actualizar()
            
            
        elif op==4:
            print("")
            print("Generando BBDD")
            print("")
            with open ('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
                escritor_csv=csv.writer(bbdd_equipos)
                escritor_csv.writerow(['id','nombre','puntos','categoria'])
                escritor_csv.writerows(lista)
            print("Archivo generado correctamente")
            print("")

        elif op==5:
            print("")
            print("Cargando base de datos")
            print("")
            lista.clear()
            cont=0
            with open ('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
                lector_csv=csv.reader(bbdd_equipos)
                for fila in lector_csv:
                    if cont==0:
                        cont+=1
                        continue
                    i=int(fila[0])
                    n=fila[1]
                    p=int(fila[2])
                    c=fila[3]
                    listita_chica=[i,n,p]
                    lista.append(listita_chica)
            
        elif op==6:
            print("")
            print("Estadisticas")
            print("")
            estadisticas()
            
            

        elif op==0:
            print("")
            print("Adios")
            break
    except:
        print("Error Ingrese una opcion valida")
        print("Redirigiendo al menu principal")
        print(".-.-.-.-.-.-.-.-.")
