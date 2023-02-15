"""Metodo de Euler"""
import math

def funcion_euler(velocidad, tiempo_inicial, c, m, recorrido):
    """Desarrolla el metodo de eules retorna resultado"""
    # Gravedad
    g = 9.8
    # print(f"({velocidad}) + ({g} - ({c}/ {m}) * {velocidad}) * ({recorrido} - {tiempo_inicial})")
    velocidad = (velocidad) + (g - (c / m) * velocidad) * (recorrido- tiempo_inicial)
    return velocidad

def funcion(m,c,tiempo):
    """Desarrolla funcion retorna resultado"""
    # Euler
    e = math.e
    # Gravedad
    g = 9.8
    # print(f"(({g}*{m})/{c})* (1 - (e^-({c}/{m})) * {tiempo}")
    valor = ((g*m)/c) * (1-(e**-(c/m * (tiempo))))
    return valor


# Coeficiente rozamiento
c = 12.5
# Masa
m = 68.1
# Tiempo inicial para la formula analitica
tiempo_inicial_formula = 0
# Tiempo inicial para eular
tiempo_inicial = 0
# Velocidad inicial
velocidad = 0
# Tiempo final
recorrido = 0
# Salto
salto = 2
contador = 0
print()
print("METODO ANALITICO\t|\t\tMETODO DE EULER")
print("t(s)\t|\tV(m/s)\t|\t\tt(s)\t|\tV(m/s)")
print("----\t \t------\t|\t\t----\t \t------")

while True:
    velocidad = funcion_euler(velocidad,tiempo_inicial,c,m,recorrido)
    valor = funcion(m,c,tiempo_inicial_formula)
    if tiempo_inicial_formula == 0:
        print(f"{tiempo_inicial_formula}\t\t{round(valor, 2)}\t\t\t|\t\t{tiempo_inicial_formula}\t \t{round(velocidad, 2)}")
    else:
        print(f"{tiempo_inicial_formula}\t \t{round(valor,2)}\t\t|\t\t{tiempo_inicial_formula}\t \t{round(velocidad,2)}")
    recorrido += salto
    tiempo_inicial = recorrido - salto
    tiempo_inicial_formula = recorrido
    contador += 1
    if contador == 51:
        break
