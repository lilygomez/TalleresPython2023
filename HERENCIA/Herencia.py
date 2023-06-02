# herencia multiple


class Padre:
    def __init__(self, Nombrep, Ojos, Pelo):
        self.nombrep = Nombrep
        self.ojos = Ojos
        self.pelo = Pelo


class Madre:
    def __init__(self, Nombrem, Estatura, ColorPiel):
        self.nombrem = Nombrem
        self.estatura = Estatura
        self.colorPiel = ColorPiel


class Hijo(Padre, Madre):
    def PresentacionPadres(self):
        print(
            f"nombres es: Liliana y mi padre es: {self.nombrep}  y mi madres es {self.nombrem} mis ojos son {self.ojos} mi pelo es {self.pelo}la estatura la herede de mi madre {self.estatura} mi color de piel es {self.colorPiel}"
         )

Padre1 = Padre("Gustavo", "Azul", "liso")
Madre1= Madre("Lilia", 1.60, "Morena")