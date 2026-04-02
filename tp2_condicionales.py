#Actividad 1
Edad = int(input("Ingresa tu edad en años"))
if Edad > 18:
    print("Es mayor de edad")

#Actividad 2
nota = int(input("Ingresá tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3
numero = int(input("Ingresá un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Actividad 4
edad = int(input("Ingresá tu edad: "))
Texto = "Por tu edad perteneces a la categoría:"
if edad < 12:
    print(f"{Texto} Niño/a")
elif edad < 18:
    print(f"{Texto} Adolescente")
elif edad < 30:
    print(f"{Texto} Adulto/a joven")
else:
    print(f"{Texto} Adulto/a")

#Actividad 5

Contraseña = input("Ingrese una contraseña entre 8 y 14 caraceteres")

if len(Contraseña) > 14 or len(Contraseña) <8:
    print ("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
consumo_mensual = int(input("ingrese su consumo mensual de energía eléctrica en kilovatios (kWh)")) 
if consumo_mensual < 150:
    print("Consumo bajo")
elif 300< consumo_mensual <=500:
    print("Consumo alto")
elif consumo_mensual >500:
    print("Consumo alto")
    print("Considere medidas de ahorro energético")
else:
    print("Consumo medio")

#Actividad 7
texto = input("Ingresá una palabra o frase (No la finalices con espacios ni signos de ningún tipo): ")

ultima_letra = texto[len(texto) - 1].lower()

if ultima_letra in "aeiouáéíóú":
    texto = texto + "!"

print(texto)

#Actividad 8
nombre = input("Ingresá tu nombre: ")
opcion = int(input("Elegí una opción del 1 al 3 sabiendo que: 1 = MAYÚSCULAS, 2 = minúsculas, 3 = Primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#Actividad 9
magnitud = float(input("Ingresá la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (no suele causar daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (daños graves a gran escala)")

#Actividad 10
hemisferio = input("¿En qué hemisferio estás? (Coloca N o S, sabiendo que N = Norte y S = Sur): ").upper()
mes = int(input("Ingresá el número del mes (1 al 12): "))
dia = int(input("Ingresá el día: "))


if hemisferio == "S":
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Verano")

elif hemisferio == "N":
    # En el hemisferio norte es todo al revés
    if (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Invierno")


