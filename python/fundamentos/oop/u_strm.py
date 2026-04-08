class UsuarioStreaming:

    def __init__(self, nombre, email, suscripcion):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []

    def agregar_a_lista(self, titulo):
        self.lista_reproduccion.append(titulo)
        print(f"Se ha añadido el titulo '{titulo}' a la lista de reproduccion")
        return self

    def ver_contenido(self):
        for elemento in self.lista_reproduccion:
            print(f"Se esta reproduciendo {elemento}")
        return self

    def cambiar_suscripcion(self, nueva_suscripcion):
        print(f"El usuario {self.nombre} ha cambiado de suscripcion a {nueva_suscripcion}")
        self.suscripcion = nueva_suscripcion
        return self

    def mostrar_info_usuario(self):
        print(f"El nombre del usuario es {self.nombre}, su email es {self.email}, su tipo de suscripcion es {self.suscripcion}")
        for elemento in self.lista_reproduccion:
            print(f"Su lista de reproduccion contiene la serie '{elemento}'")
        return self

u1 = UsuarioStreaming("juan", "juan@gmail.com", "deluxe")

u1.agregar_a_lista("jjk").agregar_a_lista("opm").agregar_a_lista("dexter")
u1.mostrar_info_usuario()