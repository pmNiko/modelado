"""
    Modelar:   un auto 

        atributos: 
            - una velocidad, al iniciar esta parado

        puede:
            - puede ver su velocidad
            - puede acelerar una determinada velocidad
            - puede frenar 
"""

velocidadAuto = [0]

def verVelocidad() -> int:
    """Devuelve la velocidad del auto"""
    return velocidadAuto[0]

def acelerar(velocidad: int) -> None:
  """ Acelera el auto """
  velocidadAuto[0] += velocidad

def frenar() -> None:
    velocidadAuto[0] = 0

if __name__ == '__main__':
    print(verVelocidad()) 
    
    acelerar(320)
    print(verVelocidad()) 
    
    frenar()
    print(verVelocidad()) 

    