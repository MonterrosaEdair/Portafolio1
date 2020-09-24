    
#E: Un número
#S: Multiplicacion de pares
#R: Numero debe ser entero

def multiplicatoria(num):
    if isinstance(num,int)and num>=0:
        if num==0:
            return 0
        else:
            return multiplicatoriaaux(num)
    else:
        return ("Error")
            
def multiplicatoriaaux(num):
    if num==0:
        return 1
    elif num%2==0:
        return (num)*multiplicatoriaaux(num-1)
    else:
        return multiplicatoriaaux(num-1)
