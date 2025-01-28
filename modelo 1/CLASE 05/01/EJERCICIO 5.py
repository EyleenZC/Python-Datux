# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Calcular la suma desde 1 hasta el número ingresado
suma = sum(range(1, numero + 1))

# Mostrar el resultado
print(f"La suma de los números de 1 hasta {numero} es: {suma}")
