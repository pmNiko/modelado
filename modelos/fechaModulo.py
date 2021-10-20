"""
    Modelar una fecha

        atributos: 
            - dia
            - mes
            - año

        puede:
            - ver el dia 
            - ver el mes
            - ver el año
            - ver Fecha
            - setearFecha
            - saber si es igual a otra fecha
            - saber si es menor a otra fecha
"""
fecha = [1,2,3]

def verDia() -> int:
    """ deavuelve el dia (fachero) """
    return fecha[0] 

def verMes() -> int:
    """ devuelve el mes  """
    return fecha[1]

def verAnio() -> int:
    """ Devuelve la fecha del año """
    return fecha[2] 

def verFecha() -> None:
    """ Muestra Fecha """
    print(f'{verDia()}/{verMes()}/{verAnio()}')

  
def setearFecha(unaFecha: list) -> None:
    """ se ingresa una fecha y se la setea """
    fecha[0] = unaFecha[0] # dia
    fecha[1] = unaFecha[1] # mes
    fecha[2] = unaFecha[2] # año

def esIgualAOtraFecha(dia: int, mes: int, anio: int) -> bool:
    """Comparar si la fecha ingresada es igual a la fecha almacenada  """
    return (
        verAnio() == anio 
        and 
        verMes() == mes 
        and 
        verDia() == dia
    )

def esMenorAOtraFecha(dia: int, mes: int, anio: int) -> bool:
    """Comparar si la fecha ingresada es menor a la fecha almacenada  """
    return (
        verAnio() < anio 
        or 
        (
            verAnio == anio and
            verMes() < mes
        ) 
        or
        (
            verAnio() == anio and
            verMes() == mes and
            verDia() < dia   
        )        
    )

if __name__ == '__main__':
    setearFecha([1, 2, 2003])
    verFecha()
    

    # print(esIgualAOtraFecha(1, 2, 2003))
  
    print(esMenorAOtraFecha(1,3,2004) )
    

    
    