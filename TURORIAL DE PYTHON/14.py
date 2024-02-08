#Conujuncion
def cojuncion ():
    print("conjuncion (and) ")

    num_uno = int(input("Escribre un numero mayor a 2 y menor a 5 : "))

    if num_uno > 2 and num_uno <  5:
        print("El numero  " , num_uno , " cumple con la condicion." )
    else:
        print("El numero  ", num_uno, "No cumple con la condicion.")

#Disjuncion
def disyunciom ():
    print("Disyuncion (or)")
    palabra = input("Para cumplir con la condicion escribe 'si ' o  'yes' : ")
    palabra = palabra.lower()
    if palabra == "si" or palabra == "yes":
        print("La condicion se comple.")
    else: print("La condicion no se cumplido")

#Negacion

def negacion():
    print("negacion (not)")
    num_uno = int(input("Introduce un numero igual a 5 :"))
    if not num_uno == 5:
        print("El numero  es diferente de cinco y si cumple la condicion.")
    else :
        print("El numero es igual a cinco y no cumple la condicion.")


