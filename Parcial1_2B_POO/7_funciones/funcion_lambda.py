#Aqui se muestran dos funciones las cuales se desglosaron de manera en que se pudiera desarrollar la funcion lambda


def multiplicacion (numero1,numero2):
    return numero1*numero2

multiplicacion= lambda numero1,numero2:numero1*numero2

resultado1=multiplicacion(10,7)
resultado2=multiplicacion(56,6)

print(resultado1)
print(resultado2)


(lambda numero1 , numero2: print(numero1 * numero2))(45,12)



