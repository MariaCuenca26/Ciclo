class ciclo:
    
    def __init__(self,num=26 ):
        self.numero=num
        
    def usowhile(self):
        #print("dentro de la clase",self.numero)
        #ciclo repetitivo que se ejecuta mientras las condiciones se cumplan (verdadero),
        #es decir sale por falso
        caracter=""
        while caracter not in ('a','e','i','o','u'):
            caracter = input("Ingrese vocal: ").lower()
            #caracter = caracter.lower()
        
        print("Felicitaciones el caracter:{} es una vocal".format(caracter))
    
ciclo2 = ciclo()
#print("fuera de la clase",ciclo2.numero)  
#print(ciclo2.usowhile())
ciclo2.usowhile()
        