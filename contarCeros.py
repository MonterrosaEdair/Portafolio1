#E: Un número
#S: Buscar que tiene ceros
#R: Número debe ser entero

def contarCeros(num):
    if isinstance(num,int):
        if num==0:
            return 1
        else:
            return contarcerosaux(abs(num))
        

def contarcerosaux(num):
    print(num)
    if num==0:
        return 0
    else:
        if num%10==0:
            return 1+contarcerosaux(num//10)
        else:
            return contarcerosaux(num//10)
