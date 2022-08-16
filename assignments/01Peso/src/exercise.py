def main():
    #escribe tu código abajo de esta línea
    peso_inicial = float(input('Dame el peso incial: '))
    peso_final = float(input('Dame el peso final: '))
    meses = int(input('Dame la cantidad de meses: '))
    peso_mes = (peso_inicial-peso_final)/meses
    print('Lo que debes bajar por mes es:',peso_mes)

if __name__ == '__main__':
    main()
