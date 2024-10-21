# 1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.
# 2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
# 3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False
# 4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.
# 5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "Nombre: {}. Edad: {}. {}".format(self.get_nombre(), self.get_edad(), self.tomar_alcohol()) 
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_edad(self, edad):
        self.edad = edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print(self)
    def es_mayor_de_edad(self):
        if self.get_edad() >= 18:
            return True
        else:   
            return False
    def tomar_alcohol(self):
        if self.es_mayor_de_edad():
            return "{} es mayor de edad. Puede tomar alcohol".format(self.get_nombre())
        else: 
            return "{} es menor de edad. Que se vaya a dormir".format(self.get_nombre())
    def es_mayor_que(self, persona):
        if self.get_edad() > persona.get_edad():
            return True
        else:
            return False

def get_mayor(persona1, persona2):
    if persona1.get_edad() > persona2.get_edad():
        return persona1
    else:
        return persona2

persona1 = Persona("Aylen", 37)
persona2 = Persona("Andres", 29)

print(persona1)
persona2.print_persona()

if persona1.es_mayor_que(persona2):
    print("{} es mayor que {}".format(persona1.get_nombre(), persona2.get_nombre()))
else:
    print("{} es mayor que {}".format(persona2.get_nombre(), persona1.get_nombre()))

print("Persona mayor: {}".format(get_mayor(persona1, persona2).get_nombre()))

# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def get_nota(self):
        return self.nota
    def get_nombre(self):
        return self.nombre
    def __str__(self):
        return "Alumno: {}. Nota: {}. Estado: {}".format(self.get_nombre(), self.get_nota(), self.set_estado())
    def set_estado(self):
        if self.get_nota() >= 6:
            return "APROBADO"
        else:
            return "DESAPROBADO, BURRX"

alumno1 = Alumno("Aylen", 10)
alumno2 = Alumno("Andres", 5)

print(alumno1)
print(alumno2)

# 7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self, nombre, lado1, lado2, lado3):
        self.nombre = nombre
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def __str__(self):
        return 'El lado mayor es: {}. El triángulo "{}" es: {}'.format(self.lado_mayor(), self.get_nombre(), self.tipo_triangulo())
    def get_nombre(self):
        return self.nombre
    def get_lado1(self):
        return self.lado1
    def get_lado2(self):
        return self.lado2
    def get_lado3(self):
        return self.lado3
    def lado_mayor(self):
        if self.get_lado1() > self.get_lado2():
            if self.get_lado1() > self.get_lado3():
                return self.get_lado1()
            else: 
                return self.get_lado3()
        elif self.get_lado2() > self.get_lado3():
            return self.get_lado2()
        else:   
            return self.get_lado3()
    def tipo_triangulo(self):
        if self.get_lado1() == self.get_lado2() and self.get_lado2() == self.get_lado3():
            return "EQUILATERO"
        elif self.get_lado1() == self.get_lado2() or self.get_lado2() == self.get_lado3() or self.get_lado1() == self.get_lado3():
            return "ISÓSCELES"
        else:
            return "ESCALENO"
        
triangulo1 = Triangulo("El del moño", 6,6,6)
triangulo2 = Triangulo("La vaca Lola",6,6,3)
triangulo3 = Triangulo("CFK", 6,7,8)

print(triangulo1)
print(triangulo2)
print(triangulo3)

# 8) Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class CalculaDora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def __str__(self):
        return "Los números ingresados son {} y {}. La SUMA es {}, la RESTA {}, la MULTIPLICACIÓN {} y la DIVISIÓN {}.".format(self.get_num1(), self.get_num2(), self.suma(), self.resta(), self.multiplicacion(), self.division())
    def get_num1(self):
        return self.num1
    def get_num2(self):
        return self.num2
    def suma(self):
        return self.get_num1() + self.get_num2()
    def resta(self):
        return self.get_num1() - self.get_num2()
    def multiplicacion(self):
        return self.get_num1() * self.get_num2()
    def division(self):
        return self.get_num1() / self.get_num2()

print(CalculaDora(2,5))

# 9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,Editar contacto, Cerrar agenda.

class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_telefono(self, telefono):
        self.telefono = telefono
    def set_mail(self, mail):
        self.mail = mail
    def get_nombre(self):
        return self.nombre
    def get_telefono(self):
        return self.telefono
    def get_mail(self):
        return self.mail
    def __str__(self):
        return "Nombre: {}. Teléfono: {}. E-mail: {}".format(self.get_nombre(), self.get_telefono(), self.get_mail())

class Agenda:
    def __init__(self):
        self.contactos = []
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
    def listar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

agenda1 = Agenda()
contacto1 = Contacto("Aylen", 3413314232, "a.pell@hotmail.com.ar")
agenda1.agregar_contacto(contacto1)
agenda1.agregar_contacto(Contacto("Andres", 3412123654, "andres@gmail.com.ar"))
agenda1.listar_contactos()
