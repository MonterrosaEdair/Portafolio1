#E: 2 números
#S: Multiplicar un número por su factor sin el operando
#R: El numero debe ser entero
        
def multiplicarRecursivo(num,factor):
    if isinstance(num,int) and isinstance(num,int) and num>=0 and factor>=0:
        if num==0:
            return 0
        else:
            return num+multi(num,factor-1)
    else:
        return ("Error")
