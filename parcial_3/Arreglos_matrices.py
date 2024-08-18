arreglo = [1, 2, 3, 4, 5]

print("Primer elemento del arreglo:", arreglo[0])  
print("Tercer elemento del arreglo:", arreglo[2])  

arreglo[2] = 10
print("Arreglo modificado:", arreglo)  

print("Elementos del arreglo:")
for elemento in arreglo:
    print(elemento)

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Elemento en la primera fila, primera columna de la matriz:", matriz[0][0])  
print("Elemento en la segunda fila, tercera columna de la matriz:", matriz[1][2])  

matriz[0][2] = 10
print("Matriz modificada:")
for fila in matriz:
    print(fila)  

print("Elementos de la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print() 
