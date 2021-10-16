""" Modelo de auto """
ruedas = [0]
desplazamiento = [0]


def ruedasDelAuto() -> int:
    """ Devuelve el numero de ruedas """
    return ruedas[0]


def desplazamientoDelAuto() -> int:
    """ Devuelve el dezplamiento del auto """
    return desplazamiento[0]


def cantidadDeRuedas(cantidadDeRuedas: int) -> None:
    """ Setea las ruedas """
    ruedas[0] = cantidadDeRuedas


def desplazar(un_desplazamiento: int) -> None:
    """ Alterar el desplazamiento del auto """
    desplazamiento[0] = un_desplazamiento


def resetearDesplazamiento() -> None:
    """ Reinicia el desplazamiento """
    desplazamiento[0] = 0


if __name__ == '__main__':
    print(ruedasDelAuto())
    cantidadDeRuedas(4)
    print(ruedasDelAuto())
