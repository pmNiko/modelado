"""
    Modelar:   una valla

        atributos: 
            - estado

        puede:
            - recuperar su estado
            - cambiar su estado
"""

estadoValla = [True]
#True significa que la valla está baja

# guetter
def verEstado() -> bool:
    """ Devuelve el estado de la valla """
    return estadoValla[0]

def cambiarEstado() -> None:
    """ Cambia el estado de la valla """
    # if verEstado(): 
    #     estadoValla[0] = False
    # else:
    #     estadoValla[0] = True
    
    estadoValla[0] = not verEstado()
      
if __name__ == '__main__':
    print(verEstado())
    
    cambiarEstado()
    print(verEstado())
    
    cambiarEstado()
    print(verEstado())
    
    cambiarEstado()
    print(verEstado())

  