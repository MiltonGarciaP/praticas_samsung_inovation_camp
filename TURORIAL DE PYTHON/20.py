def calculadora():
    print("Bienvenido a la calculadora")
    print("")
    print("Elija un opcion")
    print("1. Multiplicacion")
    print("2. Suma")
    print("3. Division")
    print("4. Resta")
    print("5. Exponente")
    print("6. Modulo o Resto")
    print("")
    opcion = int(input("Ingrese la opcion a elegir"))
    print("")
    
    if opcion == 1:
        print("Ha elegido la multiplicacion")
        numero = int(input("Ingrese el primer numero"))
        numero *= int(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    elif opcion == 2:
        print("Ha elegido la suma")
        numero = int(input("Ingrese el primer numero"))
        numero += int(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    elif opcion == 3:
        print("Ha elegido la Division")
        numero = float(input("Ingrese el primer numero"))
        numero /= float(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    elif opcion == 4:
        print("Ha elegido la Resta")
        numero = int(input("Ingrese el primer numero"))
        numero -= int(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    elif opcion == 5:
        print("Ha elegido la Exponenciacion")
        numero = int(input("Ingrese el primer numero"))
        numero **= int(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    elif opcion ==  6:
        print("Ha elegido la Modulo o resto")
        numero = int(input("Ingrese el primer numero"))
        numero %= int(input("Ingrese el segundo  numero"))
        print("El resultado es : " , numero)
    else:
        print("Ha elegido una opcion incorrecta")
calculadora()
        
    
