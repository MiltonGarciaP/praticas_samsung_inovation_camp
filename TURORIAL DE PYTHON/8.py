print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cúal es tu nombre?")
mate = int(input(nombre.upper() +" ¿Cúal es tu calificacion en matematicas?"))
histo = int(input(nombre.upper() +" ¿Cúal es tu calificacion en historia?"))
quimi =int(input(nombre.upper() +" ¿Cúal es tu calificacion en quimica?"))
lengua = int(input(nombre.upper() +" ¿Cúal es tu calificacion en lengua ?"))

resultado = (mate + histo + quimi + lengua) / 4
resultado = int(resultado)
if resultado >= 5:
    print("Haz calificado con ", resultado)
if resultado <= 4:
    print ("No haz calificado ", resultado)
