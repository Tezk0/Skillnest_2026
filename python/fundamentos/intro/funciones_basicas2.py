# Calcula experiencia
def multiplicar_por_2(num):
    lista=[]
    for i in range(num+1):
        lista.append(i*2)
    return lista
print(multiplicar_por_2(5))
# Debe retornar: [0, 2, 4, 6, 8, 10]
print("Barrera ------------------------------------------------------------------------------------------------------------------------")


# Analiza publicaciones
def suma_y_resta(lista1):
    print(lista1[0]+lista1[1])
    return(lista1[0]-lista1[1])
print(suma_y_resta([120,115]))
# Imprime: 235 y retorna: 5
print("Barrera ------------------------------------------------------------------------------------------------------------------------")


# Puntaje ajustado
def sumatoria_menos_longitud(lista2):
    total = 0
    for elemento in lista2:
        total+=elemento
    return total - len(lista2)
print(sumatoria_menos_longitud([10, 5, 3, 7]))
# Suma total = 25, longitud = 4, debe retornar: 21
print("Barrera ----------------------------------------------------------------------------------------------------------------------")

# Ajusta visualizaciones
def valores_multiplicados_segundo(lista3):
    if len(lista3) >= 2:
        lista4=[]
        for elemento in lista3:
            lista4.append(elemento*lista3[1])
        print(len(lista4))
        return lista4
    else:
        print(len(lista3))
        return []
print(valores_multiplicados_segundo([100, 3, 50, 20]))
# Imprime: 4 y retorna: [300, 9, 150, 60]
print(valores_multiplicados_segundo([100]))
# Imprime: 1 y retorna: []
print("Barrera ------------------------------------------------------------------------------------------------------------------------")

# Genera precio fijo
#def valor_multiplicado_longitud(valor, longitud):
    #lista5 

    #No alcanze a terminar sorry profe :(

#valor_multiplicado_longitud(5, 2)
# Debe retornar: [10, 10]

#valor_multiplicado_longitud(7, 5)
# Debe retornar: [35, 35, 35, 35, 35]