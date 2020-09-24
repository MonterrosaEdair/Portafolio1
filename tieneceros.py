#E: Un número
#S: Verificar si el número tiene ceros o no
#R: Número debe ser entero positivo
        
def tieneceros(num):
    if num==0:
        return True
    else:
        return tienecerosaux(abs(num))
    
def tienecerosaux(num):
    if num==0:
        return True
    else:
        if num%10==0:
            return True
        else:
            return False
