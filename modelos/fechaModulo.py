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



def esIgual(dia: int, mes: int, anio: int) -> bool:
    """Comparar si la fecha ingresada es igual a la fecha almacenada  """
    return (
        verAnio() == anio 
        and 
        verMes() == mes 
        and 
        verDia() == dia
    )

def esMenor(dia: int, mes: int, anio: int) -> bool:
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
    
def esMenorOIgual(dia: int, mes: int, anio: int) -> bool:
    """ Responde si es menor o igual a otra fecha """
    return esMenor(dia, mes, anio) or esIgual(dia, mes, anio)
    
def esMayor(dia: int, mes: int, anio: int) -> bool:
    """ Responde si es mayor a otra fecha """
    return not esMenorOIgual(dia, mes, anio)


def esMayorOIgual(dia: int, mes: int, anio: int) -> bool:
    """ Responde si es mayor o igual """
    return not esMenor(dia, mes, anio)

def entreDosFechas(fecha_inicial: list[int], fecha_final: list[int]) -> bool:
    """ Responde si se encuentra entre dos fechas pasadas como parametro """
    return (
        esMayorOIgual(fecha_inicial[0], fecha_inicial[1], fecha_inicial[2])
        and 
        esMenorOIgual(fecha_final[0], fecha_final[1], fecha_final[2])
    )
    
    
if __name__ == '__main__':
    setearFecha([1, 2, 2003])
    
    fecha_start = [1,1,2002]
    fecha_end = [1,1,2004]
    
    print(entreDosFechas(fecha_start, fecha_end))
    

    
    