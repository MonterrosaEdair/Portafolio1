#E: Un número
#S: Averiguar la sumatoria de un número
#R: Número debe ser entero positivo
    
def sumatoria(ini,fin):
    if isinstance(ini,int) and isinstance(fin,int)and ini>=0 and fin>=0:
        if fin==0:
            return ini
        else:
            return ini+sumatoriaaux(ini,fin,0)
    else:
        return "Error"

def sumatoriaaux(ini,fin,cont):
    if cont==fin:
        return 0
    else:
        nuevo=inicio+1
        return nuevo+sumatoriaaux(nuevo,fin,cont+1)
