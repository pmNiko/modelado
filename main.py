from modelos import auto

if __name__ == '__main__':
    print(auto.desplazamientoDelAuto())

    auto.desplazar(50)
    print(auto.desplazamientoDelAuto())

    auto.resetearDesplazamiento()
    print(auto.desplazamientoDelAuto())
