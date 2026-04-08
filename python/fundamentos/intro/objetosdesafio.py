class Usuario:
    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.activo = False

    def activar(self):
        self.activo = True
        print(f"Usuario activado")

    def desactivar(self):
        self.activo = False
        print(f"Usuario desactivado")

    def info(self):
        print(self.nombre)
        print(self.email)
        if self.activo == True:
            print("El usuario esta activado")
        else:
            print("El usuario esta desactivado")

u1 = Usuario("Sofia",  "sofia@gmail.com",  17)

u2 = Usuario("Diego",  "diego@gmail.com",  18)

u3 = Usuario("Juan",  "juanitoperez123@gmail.com",  19)


u2.activar()

u1.info()

u2.info()

u3.info()