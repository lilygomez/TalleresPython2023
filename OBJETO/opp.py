#Programación orientada a objetos: Es un paradigma (Modelo) que imita objetos reales. 
#Permite reutilizar y segmentar codigo en pequeñas tareas.
#OBJETO: Algo que se compone de atributos (Caracteristicas) (Funcionalidad)


"""
           Objeto: Vehiculo
           Atributos: Color,Marca, Modelo, Precio, Cilindraje
           Metodos: Descontar, Apagar, Andar
    """
    
    #Primcipios: Herencia, Abstracción, Encapsulamiento, Polimorfismo.
    #CLASE: Sistema donde se crean los atributos, Metodos del objeto.
    #Ejemplo:
"""class Vehiculo:
        Color = "Rosado"
        Marca = "Audi"
        Modelo = 2023
        Precio = 2000000000000
        Cilindraje = "2000 CC" 
    #Instancia del objeto
    Vehiculo1 = Vehiculo()
    Print(Vehiculo1.Color)
    Self hace referencia al objeto que se va a instanciar """
    
class Vehiculo:
        def _init_(self,Color,Modelo,Marca,Precio,Cilindraje):
            self.color = Color 
            self.marca = Marca
            self.modelo = Modelo
            self.precio = Precio
            self.cilindraje = Cilindraje
            self.rebaja = False
            self.encender = False
        def InfoProducto(Self):
            print(f"Las caracteristicas del vehiculo son:\nColor: {self.Color}\nMarca: {self.Marca}\nModelo {self.Modelo}\nPrecio{self.Precio}\Cilindraje{self.Cilindraje}")
        def andar(self):
            if self.encender:
                print("Inicio la marcha")
            else:
                print("Debe encender el veiculo para iniciar la marcha")
        def andar(self):
            if self.encender:
                print("iniciar marcha")
            else:
                print("debe")
                
                
                 
#Instanciar el objeto 
Vehiculo1 = Vehiculo("Rosado", "Audi", 2023, 2000000000000, "2000 CC", True)
Vehiculo2 = Vehiculo("Azul", "Chevrolet", 2022, 7000000000000, "1600 CC", False)
print(Vehiculo1.Modelo)
print(Vehiculo2.Marca)
Vehiculo.InfoProducto()

Vehiculo1.marca = "kia" #modificacion el atributo marca
print(Vehiculo1.marca)
Vehiculo1.andar()
print(" el precio del vehiculo 2 es", Vehiculo2.precio)
Vehiculo2.Descuento(30)
print("el precio despues del aplicado el desucento al vehiculo 2 es: ")
Vehiculo2.precio
Vehiculo1.InfoProducto()
Vehiculo2.InfoProducto()