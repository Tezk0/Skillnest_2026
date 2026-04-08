class Usuario:   #la moderfokin clase
 
    def __init__(self, nombre, email, edad):
        
        self.nombre = nombre
        #self es pa crear el objeto 
        self.email = email
        self.edad = edad
        self.activo = True
    #el moderfokin def para crear objetos

    #ahora vamos a hacer codigo para un login

    def login(self):
        
        self.activo = True

        print(f"{self.nombre} ha iniciado sesion")

    def logout(self):

        self.activo = False
        print(f"{self.nombre} ha salido de la sesion")


#Estos son instancias de la clase usuario (objetos que fueron creados con una clase)
u1 = Usuario("Sofia",  "sofia@gmail.com",  17)

u2 = Usuario("Diego",  "diego@gmail.com",  18)

print(u1.nombre)
print(u2.nombre)
print(u1.edad)
print(u2.edad)