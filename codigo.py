"""Generadores de turno para calcular el turno donde se esta"""



def generador_perfumeria():
    x = 0
    while True:
        x +=1
        yield "P - "+x

def generador_farmacia():
    x = 0
    while True:
        x +=1
        yield "F - "+x


def generador_cosmetica():
    x = 0
    while True:
        x +=1
        yield "C - "+x
