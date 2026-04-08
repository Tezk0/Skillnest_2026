
for i in range(30):
    if i % 3:
        print("Fizz")
    elif i % 5:
        print("Buzz")
    if i % 3 and i % 5:
        print("FizzBuzz")

print("Barrera ___________________________________________________________________________________________________________")

numero = int(input("ingrese un número")) 

for i in range(11):
    print(f"{numero} X {i} = {numero * i}")


print("Barrera ___________________________________________________________________________________________________________")

num = 1

while num <= 100:
    print(num)
    num +=1

print("Barrera ___________________________________________________________________________________________________________")

def piramide(n):
    for i in range(1, n + 1):
        espacios = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        print(espacios + asteriscos)
piramide(5)