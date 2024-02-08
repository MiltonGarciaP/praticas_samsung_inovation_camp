print("************************************************************")
print("* Programa para determinar Cual es el numero mas grande de tres numeros *")
print("************************************************************")


num_uno = int(input("Introduce el primer numero "))
num_dos = int(input("Introduce el segundo numero "))
num_tres = int(input("Introduce el tercer numero "))

if num_uno > num_dos and num_uno > num_tres:
    print("El numero ", num_uno, " es el mayor de todos")
elif num_tres > num_dos and num_tres > num_uno:
    print("El numero ", num_tres, " es el mayor de todos")
elif num_dos > num_uno and num_dos > num_tres:
    print("El numero ", num_dos, "es el mayor de todos")
else:
    print("Los numeros son iguales")
    
