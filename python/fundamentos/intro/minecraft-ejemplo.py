class Bloque:
    def __init__(self, nombre, dureza, herramienta):
        self.nombre = nombre
        self.dureza = dureza
        self.herramienta = herramienta
        self.roto = False

    def minar(self, herramienta):
        if herramienta == self.herramienta:
            self.roto = True
            return f"✔ Obtuviste {self.nombre}!"
        return "No sirve esta herramienta"
    
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__vida = 20   #Esto es privado
        self.__hambre = 20

    @property
    def vida(self):
        return self.__vida
    
    def recibir_daño(self, cantidad):
        if self.__vida == 0:
            return "Te moriste jilipollas"
        return f"❤ vida: {self.__vida}/20"
    
class Mob:
    def __init__(self, nombre, vida, daño):
        self.nombre =  nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, jugador):
        jugador.recibir_daño(self.daño)
        return f"{self.nombre} te ataco!!"
    
class Zombie(Mob):
    def __init__(self):
        super().__init__("Zombie", 20, 1)
        self.quema_con_sol = True

    def atacar(self, jugador):
        resultado = super().atacar(jugador)
        return resultado + "io soy un zombi y t ataque"
    
piedra = Bloque("Piedra", 1.5, "pico")
madera = Bloque("Madera", 2.0, "hacha")
diamante = Bloque("Diamante", 5.0, "pico_hierro")
tierra = Bloque("Tierra", 1.0, "pala")
obsidiana = Bloque("Obsidiana", 6.7, "pico_diamante")
mineral_hierro = Bloque("Hierro Crudo", 1.8, "pico_piedra")

print(piedra.minar("pico"))
print(madera.minar("pico"))
print(diamante.minar("pico_hierro"))
print(f"¿Piedra rota? {piedra.roto}")
print(tierra.minar("pala"))
print(obsidiana.minar("pico_diamante"))
print(mineral_hierro.minar("pico_piedra"))