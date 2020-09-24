#E: 2 números
#S: Sacar la potencia de un número
#R: Número debe ser entero positivo

def potencia(num,ele):
    if isinstance(num,int) and isinstance(ele,int):
        if ele>=0:
            return 1
        else:
            return potenciaaux(num,ele)

def potenciaaux(num,ele):
    if ele==0:
        return 1
    else:
        return num+potenciaaux(num,ele-1)
