print("=========")
print("Conversor")
print("=========")

print("Menu de opciones: ")
print(" ")
print("Presiona 1 para convertir de numero a palabra ")
print("Presiona 2 para convertir de palabra a numero ")
print(" ")
opcion = int(input("Cual es tu opcion "))

if opcion == 1:
    numero = int(input("Ingrese el numero que quiere ingresar "))
    if numero == 1:
        print("UNO")
    elif numero == 2:
        print("Dos")
    elif numero == 3:
        print("Tres")
    elif numero == 4:
        print("Cuatro")
    elif numero == 5:
        print("cinco")
    elif numero == 6:
        print("Seis")
    elif numero == 7:
        print("Siete")
    elif numero == 8:
        print("Ocho")
    elif numero == 9:
        print("Nueve")
    else:
        print("No tengo ese numero")
elif opcion == 2:
    palabra = input("Ingrese el numero en letra que quiere convertir ")
    if palabra == "UNO":
        print("1")
    elif palabra == "Dos":
        print("2")
    elif palabra == "Tres":
        print("3")
    elif palabra == "Cuatro":
        print("4")
    elif palabra == "cinco":
        print("5")
    elif palabra == "Seis":
        print("6")
    elif palabra == "Siete":
        print("7")
    elif palabra == "Ocho":
        print("8")
    elif palabra == "Nueve":
        print("9")
    else:
        print("No tengo ese numero")
else:
    print("Ha ingresado un numero irroneo")
print("Fin")
