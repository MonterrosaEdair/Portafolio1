#E: Un número
#S: sacar los números pares
#R: Número debe ser entero positivo
    
def par(num):
    if isinstance(num,int)and num <-1:
        if num==0:
            return 0
        else:
            return paresaux(abs(num),0)
    else:
        return ("Número debe ser mayor a 0 y entero")

def paresaux(num,pot):
    if num==0:
        return 0
    else:
        if (num%10)%2==0:
            return (num%10)*(10**pot)+(paresaux(num//10,pot+1))
        else:
            return paresaux(num//10,pot)
