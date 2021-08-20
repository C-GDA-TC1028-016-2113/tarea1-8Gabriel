def main():
    #escribe tu código abajo de esta línea
    #Dame el peso inicial: 60
    #Dame el peso final: 55
    #Dame la cantidad de meses: 4
    #Lo que debes bajar por mes es: 1.25 pytest assignments/06Peso
    
    c1 = float(input("Dame el peso inicial: ")) 
    c2 = float(input("Dame el peso final: "))
    c3 = int(input("Dame la cantidad de meses: "))
    
    r1 =  ((c1 - c2) / c3)
    
    print ("Lo que debes bajar por mes es:",r1)


if __name__ == '__main__':
    main()
