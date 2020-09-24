#E: Un número
#S: Sacar lo divisores de un número
#R: El numero debe ser entero
    
def divisores(num):
    if isinstance(num,int)and num>=0:
        if num==0:
            return 0
        else:
            return divi(num,num)

def divi(num,cont):
    if cont==1:
        return cont
    else:
        if num%cont==0:
            print(cont)
            return divi(num,cont-1)
        else:       
            return divi(num,cont-1)
