"""
    Modelar: un contador
        atributos: 
            - un valor, inicializa en 0
        
        puede:
            - ver el valor
            - incrementar su contador en 1
            - decrementar su contador en 1
"""

valor = [0]

def verValor() -> int:
    """ Devuelve el valor del contador """
    return valor[0] 

def incrementar() -> None:
    """ Esta funcion incrementa el valor del contador """ 
    valor[0] += 1
    
def decrementar() -> None:
    """ Esta función decrementa el valor del contador """   
    valor[0] -= 1



if __name__ == '__main__':
    print(verValor())
    
    incrementar()
    print(verValor())
    
    decrementar()
    print(verValor())


