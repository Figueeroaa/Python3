
while True:

    print("1. suma")

    print("2. resta")

    print("3. multiplicacion")

    print("4. division")
    
    print("5. salir")
    menu =int(input("Ingrese opcion"))
    if menu in (1,2,3,4):

        n1 = int(input("Ingrese numero:\n"))
        n2 = int(input("Ingrese numero:\n"))
    if menu==5:
        break
    if menu==1:
        resultado=n1+n2
    elif menu==2:
        resultado=n1-n2
    elif menu==3:
        resultado=n1*n2
    elif menu==4:
        resultado=n1/n2
    print(resultado)
