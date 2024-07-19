#Definir la suma total dada 
suma_total = 60

menor_numero = (suma_total - 6) //3

#imprimir resultado
print (f"el menor de los tres nuemros pares consecutivos es: {menor_numero}")


segundo_numero = menor_numero + 2
tercer_numero = menor_numero + 4
suma_verificacion = menor_numero + segundo_numero + tercer_numero

print(f"los numeros sin: {menor_numero},{segundo_numero},{tercer_numero}")
print(f"las suma de los nuemros es: {suma_verificacion}")
