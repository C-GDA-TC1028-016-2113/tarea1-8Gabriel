def main():
    #escribe tu código abajo de esta línea
    #Dame x1: 3.6
    #Dame y1: -1.3
    #Dame x2: 8.6
    #Dame y2: 2.5
    #Pendiente: 0.76
    #m = (y2 - y1) / (x2 - x1) pytest assignments/07PendienteLinea
    
    x1 = float(input("Dame x1: ")) 
    y1 = float(input("Dame y1: ")) 
    x2 = float(input("Dame x2: ")) 
    y2 = float(input("Dame y2: ")) 
    
    m = (y2 - y1) / (x2 - x1)
     
    print ("Pendiente:",m)

if __name__ == '__main__':
    main()
