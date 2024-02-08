
print("================================")
print("Compañia multinacional Rappi ")
print("================================")
print("Se le estara calculando sus vacaciones")
print("================================")
print(" ")

nombre = input(" Digite su Nombre ")
nombre = nombre.upper()
print("")
departmento = int (input(nombre+" Digite la clave de su departamento "))
print("")
antiguedad = int(input(nombre+" Digite la antiguedad en años en la empresa "))
print("")

if departmento == 1:
    if  antiguedad == 1:
        print("6 dias de vacaciones le tocan "+ nombre)
    elif antiguedad >= 2 and antiguedad <= 6:
        print("14 dias de vacaciones  "+ nombre)
    elif antiguedad >= 7:
        print("20 dias de vacaciones " + nombre)
        
elif departmento == 2:
    if  antiguedad == 1:
        print("7 dias de vacaciones le tocan "+ nombre)
    elif antiguedad >= 2 and antiguedad <= 6:
        print("15 dias de vacaciones  "+ nombre)
    elif antiguedad >= 7:
        print("22 dias de vacaciones " + nombre)

elif departmento == 3:
    if  antiguedad == 1:
        print("10 dias de vacaciones le tocan "+ nombre)
    elif antiguedad >= 2 and antiguedad <= 6:
        print("20 dias de vacaciones  "+ nombre)
    elif antiguedad >= 7:
        print("30 dias de vacaciones " + nombre)
else:
    print ("Codigo no valido")
print("Fin.")
