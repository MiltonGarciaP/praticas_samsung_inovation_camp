print("Sistema para calcular el promedio de un alumno.")
print(" ")
Nombre = input("Para comenzar, Cual estu nombre ")
mat = float(input(Nombre.upper() + " Cual es tu califacion en matematicas"))
his = float(input(Nombre.upper() +" Cual es tu califacion en Historia"))
fis = float(input(Nombre.upper() +" Cual es tu califcacion en Fisica"))

resultado = (mat + his + fis) / 3
resultado = int(resultado)

if(resultado >= 5):
    print(Nombre.upper()
    +" Calificaste con la califcacion de " , resultado)
else:
    print(Nombre.upper()
    +" No Calificaste con la califcacion de " , resultado)
    

print ("Fin")
