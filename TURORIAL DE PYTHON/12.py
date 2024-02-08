print("INTRODUCCE DOS NUMEROS A COMPARAR")

num_uno = int(input("Incerta el primer numero"))
num_dos = int(input("Incerta el segundo numero"))

if num_uno == num_dos:
    print("Son Iguales")
if num_dos != num_uno:
    print("Son Diferentes")
if num_uno > num_dos:
    print ("EL " , num_uno , "es mayor que ", num_dos)
if num_uno < num_dos:
    print ("EL " , num_uno , "es menor que ", num_dos)
if num_uno <= num_dos:
    print ("EL " , num_uno , "es menor o igual que ", num_dos)
if num_uno >= num_dos:
    print ("EL " , num_uno , "es mayor o igual que ", num_dos)

print("Fin")
