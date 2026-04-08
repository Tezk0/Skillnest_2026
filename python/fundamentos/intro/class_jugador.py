class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__vida = 20   #Esto es privado
        self.__hambre = 20

    @property
    def vida(self):
        return self.__vida
    
    def recibir_daño(self, cantidad):
        self.__vida = max(0, self.__vida - cantidad)
        if self.__vida == 0:
            return "Te moriste jilipollas"
        print(f"Recibiste {cantidad} puntos de daño!")
        return f"❤ vida: {self.__vida}/20"
    
    def comer(self, comida):
        recupera = {"manzana": 4, "carne": 8, "pan": 5}
        if comida in recupera:
            self.__hambre = min(20, self.__hambre + recupera[comida])
            return f"🍗 Hambre: {self.__hambre}/20"
        return f"❌ {comida} no es comestible"
    
steve = Jugador("Steve")
print(steve.recibir_daño(6))
print(steve.vida)

steve.__vida = 99999999999

print(steve.comer("carne"))
