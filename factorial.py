#E: Un número
#S: Sacar la recursion con el método de fibonacci
#R: Número debe ser entero positivo
    
def factorial(num):
    if isinstance(num,int) and num>=0:
        if num==0:
            return 0
        else:
            return num*factorial(num-1)
    else:
        return ("Error")
