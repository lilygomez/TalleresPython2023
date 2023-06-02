#HERENCIA:subclase(clase hija) que hereda los atriburtos y metodos de una superclase(clase padre)
class Persona:
    def __init__(self,Nombre,Edad,DNI):
        self.nombre=Nombre
        self.edad=Edad
        self.DNI=DNI
    
    def presentacion(self):
        print(f'Mucho gusto soy {self.nombre} tengo {self.edad}')
    
    
persona1=Persona('Miguel', 19, 1002105913)
print(persona1)
persona1.presentacion()

class Docente(Persona):
    def __init__(self, Nombre, Edad, DNI, Especialidad, SubMódulo, Universidad):
        super().__init__(Nombre, Edad, DNI)
        self.especialidad=Especialidad
        self.subMódulo=SubMódulo
        self.universidad=Universidad
    
docente1=Docente("Nairobi", 25, 1002105914, "Matemáticas", "Álgebra", "CESDE")
docente1.presentacion()

#Metodo que calcules el promedio del estiante y decir si pasó o no

class Estudiante(Persona):
    def __init__(self, Nombre, Edad, DNI, Cursos, Aula, Semestre, Nota):
        super().__init__(Nombre, Edad, DNI)
        self.cursos=Cursos
        self.aula=Aula
        self.semestre=Semestre
        self.nota=Nota
    
        
estudiante1=Estudiante("Anuel", 28, 1002105915, "Python", 405,"2°",4.8 )
estudiante1.presentacion()
print(estudiante1)
        
        

        