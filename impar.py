#E: Un número
#S: Sacar los números impares
#R: Número debe ser entero positivo
        
def impar(num):
    if isinstance(num,int) and num>=0:
        if num==0:
            return 0
        else:
            return impa(num,0)
    else:
        return "error"

def impa(num,pot):
    if num==0:
        return 0
    else:
        if (num%10)%2==1:
            return ((num%10)*(10**pot)+impa(num//10,pot+1))
        else:
            return impa(num//10,pot)
