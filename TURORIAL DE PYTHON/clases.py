def print_hi(name):
    class Persona:
        def __init__(self, nombre, edad, ocupacion):
            self.nombre = nombre
            self.edad = edad
            self.ocupacion = ocupacion

        def presentarse(self):
            return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}."

        def cumplir_anios(self):
            self.edad += 1
            return f"Feliz cumpleaños! Ahora tengo {self.edad} años."

        def cambiar_ocupacion(self, nueva_ocupacion):
            self.ocupacion = nueva_ocupacion
            return f"Mi nueva ocupación es {self.ocupacion}."

    class Coche:
        def __init__(self, marca, modelo, anio):
            self.marca = marca
            self.modelo = modelo
            self.anio = anio

        def describir_coche(self):
            return f"Este es un {self.marca} {self.modelo} del año {self.anio}."

        def actualizar_modelo(self, nuevo_modelo):
            self.modelo = nuevo_modelo
            return f"El modelo ha sido actualizado a {self.modelo}."

        def calcular_antiguedad(self, anio_actual):
            antiguedad = anio_actual - self.anio
            return f"El coche tiene {antiguedad} años de antigüedad."

    class Libro:
        def __init__(self, titulo, autor, genero):
            self.titulo = titulo
            self.autor = autor
            self.genero = genero

        def info_libro(self):
            return f"{self.titulo} escrito por {self.autor}. Género: {self.genero}."

        def cambiar_genero(self, nuevo_genero):
            self.genero = nuevo_genero
            return f"El género ha sido cambiado a {self.genero}."

        def leer_libro(self):
            return f"Estoy leyendo {self.titulo} de {self.autor}."

    class Mascota:
        def __init__(self, nombre, especie, edad):
            self.nombre = nombre
            self.especie = especie
            self.edad = edad

        def presentarse(self):
            return f"Hola, soy {self.nombre}, una mascota de {self.edad} años de edad."

        def envejecer(self):
            self.edad += 1
            return f"Feliz cumpleaños! Ahora tengo {self.edad} años."

        def cambiar_nombre(self, nuevo_nombre):
            self.nombre = nuevo_nombre
            return f"Mi nuevo nombre es {self.nombre}."

    # Crear objetos para cada clase
    persona1 = Persona("Juan", 30, "Ingeniero")
    persona2 = Persona("María", 25, "Doctora")

    coche1 = Coche("Toyota", "Corolla", 2018)
    coche2 = Coche("Ford", "Focus", 2015)

    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía")
    libro2 = Libro("1984", "George Orwell", "Ciencia Ficción")

    mascota1 = Mascota("Luna", "Perro", 5)
    mascota2 = Mascota("Simba", "Gato", 3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
