for i in range(10):
    print(i)
    print("vicente gay")
print("------------------------------------------------------------------------------------------------------------------------------")


for repeticion in range(2, 6):
    print(repeticion)
print("--------------------------------------------------------------------------------------------------------------------------")

for i in range(2, 10, 3):
    print(i)
print("-----------------------------------------------------------------------------------------------------------------------------")
print("decremento")

for i in range(0, 20, -5):
    print(i)

print("-----------------------------------------------------------------------------------------------------------------------------")

print("Python")

for letra in 'Python':
    print(letra)

lista = ["Lapiz", "Papel", "Plumones"]
print("len(lista):")
print(len(lista))

for indice in range(len(lista)):
    print(indice,lista[indice])

for elemento in lista:
    print(elemento)
print("-----------------------------------------------------------------------------------------------------------------------------")

print("Diccionario")

estudiante = {"nombre": "Vicente", "edad": 17, "carrera": "Informatica"}

print (estudiante.values())

print("Diccionario con bucle for")

print("------------------------------------------------------------------------------------------------------------------------------")



num = 0

while num < 4:
    print("bucle while - ", num)
    num += 1
else:
    print("bucle while terminado")

print("-----------------------------------------------------------------------------------------------------------------------------")


for letra in "detente":
    if letra == "n":
        break
    print(letra)

print("-----------------------------------------------------------------------------------------------------------------------------")

for letra in  "detente":
    if letra == "n":
        continue
    print(letra)