#E: Un número
#S: Contar dígitos
#R: Número debe ser entero positivo

def contarDigitos(num):
    if isinstance (num,int):
        if num==0:
            return 1
        else:
            return contaraux(abs(num))
    else:
        return("Número debe ser entero")

def contaraux(num):
    if num==0:
        return 0
    else:
        return 1+contaraux(num//10)
