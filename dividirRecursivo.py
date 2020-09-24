#E: 2 números
#S: dividir un número por su dividendo sin el operando
#R: El numero debe ser entero
    
def dividirRecursivo(divisor,dividendo):
    if isinstance(divisor,int) and isinstance(dividendo,int)or isinstance(divisor,float) or isinstance(dividendo,float) :
        if divisor==0:
            return 1
        elif dividendo==0:
            return "Error"
        else:
            return diviraux(divisor,dividendo)
        
def diviraux(divisor,dividendo):
    if divisor==dividendo:
        return 1
    elif divisor<dividendo:
        return 0
    else:
        return 1+diviraux(divisor-dividendo,dividendo)
