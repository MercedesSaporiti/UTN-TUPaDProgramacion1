"""
1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla.

3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.

4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.

5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.

6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.

7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo:𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números"""

# Actividad 1
print("Hola mundo!")

# Actividad 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}, mucho gusto en saludarte!")

# Actividad 3
edad = int(input("¿Cuántos años tenés? "))
residencia = input("¿En qué localidad vivís? ")
print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}")

# Actividad 4
pi = 3.1415
radio = float(input("Ingresá el radio del círculo: "))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# Actividad 5
Segundos = int(input("Ingrese una cantidad de segundos"))
Convert_hs= float(Segundos/(60*60))
print(f"{Segundos} equivalen a {Convert_hs: .2f} horas")

# Actividad 6
numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Actividad 7
print("Hola, vamos a hacer un ejercico, para esto necesitamos que pienses en 2 numeros enteros que no sean 0, listo?")
num1 = int(input("Ingresá el primer número (distinto de 0): "))
num2 = int(input("Ingresá el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 

print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")

# Actividad 8
print("Vamos a calcular tu indice de masa corporal (IMC), para eso necesitamos tu peso y altura")
Peso = float(input("Ingresá tu peso expresado en kg, con 1 solo decimal. Ej: 55.3 :"))
Altura = float(input("Ingresá tu altura expresada en metros, con 1 o 2 decimales. Ej: 1.65 :"))
IMC = Peso/Altura**2
print(f"Tu IMC es de: {IMC: .2f}")

# Actividad 9
celsius = float(input("Ingresá la temperatura en grados Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print(f"{celsius} °C equivalen a {fahrenheit} °F")

# Actividad 10
print("Pensa en 3 numeros enteros del 1 al 500")
nro1 = int(input("Ingresa el primer numero:"))
nro2 = int(input("Ingresa el segundo numero:"))
nro3 = int(input("Ingresa el tercer numero:"))
promedio = (nro1+ nro2+ nro3)/3

print(f"El promedio de {nro1},{nro2} y {nro3} es: {promedio: .2f}")