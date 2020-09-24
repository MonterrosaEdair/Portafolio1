#E: Un número
#S: Averiguar la sumatoria de un rango de un número
#R: Número debe ser entero positivo
    
def sumatoriaRango(inicio,fin,rango):
    if isinstance(inicio,int) and isinstance(fin,int) and isinstance(rango,int):
        if inicio<fin:
            return sumaA(inicio,fin,rango)
        else:
            return "error"
    else:
        return "error2"
    
def sumaA(inicio,fin,rango):
    if inicio+rango>fin:
        return inicio
    else:
        return inicio+sumaA(inicio+rango,fin,rango)
