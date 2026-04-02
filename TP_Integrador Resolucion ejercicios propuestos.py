# ============================================================
# Ejercicio 1: Simulacion kiosco:
# ============================================================
cliente = input("Ingrese su nombre: ")
while not cliente.isalpha():
    cliente = input("Ingrese su nombre: ")

cant_productos = input("Ingrese la cantidad de productos: ")
while not cant_productos.isdigit() or int(cant_productos) <= 0:
    cant_productos = input("Ingrese la cantidad de productos: ")

cant_productos = int(cant_productos)

print(f"Cliente: {cliente}")
print(f"Cantidad de productos: {cant_productos}")

precio_total = 0
precio_dto = 0

for i in range(1, cant_productos + 1):
    p = input(f"Ingrese el precio del producto {i}: ")
    while not p.isdigit():
        p = input(f"Ingrese el precio del producto {i}: ")
    
    p = int(p)

    dto = input("El producto tiene descuento? (s/n): ")
    while dto not in ("s", "S", "n", "N"):
        dto = input("El producto tiene descuento? (s/n): ")

    if dto in ("s", "S"):
        precio_dto += p * 0.1

    precio_total += p
    print(f"Producto {i} - Precio: {p} Descuento (S/N): {dto}")

precio_final = precio_total - precio_dto

print(f"Total sin descuentos: $ {precio_total}")
print(f"Total con descuentos: $ {precio_final:.2f}")
print(f"Ahorro: $ {precio_dto:.2f}")
print(f"Promedio por producto: $ {precio_final / cant_productos:.2f}")


# ============================================================
#Ejercicio 2 — “Acceso al Campus y Menú Seguro” usuario correcto: "alumno" , clave correcta: "python123" . Max 3 intentos
# ============================================================

Usuario = input("Ingrese su usuario:")
Contasen = input("Ingrese su password:")
contador = 1
bloqueo = False

while Usuario != "alumno" or Contasen !="python123":
    if contador >= 3:
        bloqueo = True
        break
    contador +=1
    print("Credenciales invalidas")
    Usuario = input("Ingrese su usuario:")
    Contasen = input("Ingrese su password:")

if bloqueo:
  print("Cuenta bloqueada")
else:
    opcion = input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n")
    while not opcion.isdigit:
        print("Ingrese un numero valido")
        opcion = input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n")
    opcion = int(opcion)
    while opcion<1 or opcion >4:
        print("Opcion fuera de rango")
        opcion = int(input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n"))

    while opcion != 4:
        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            clave = input("Ingrese la nueva clave:")
            while len(clave)< 6:
              print("La clave debe tener al menos 6 caracteres")
              clave = input("Ingrese la nueva clave:")
            confirm = input("Confirme la nueva clave:")
            while clave != confirm:
                print("No coinciden las claves")
                clave = input("Ingrese la nueva clave:")
                confirm = input("Confirme la nueva clave:")
            print("Clave actualilzada exitosamente")
        elif opcion == 3:
            print("Vas muy bien! a seguir aprendiendo, cada vez un paso mas cerca del objetivo!")

        opcion = input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n")
        while not opcion.isdigit:
            print("Ingrese un numero valido")
            opcion = input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n")
        opcion = int(opcion)
        while opcion<1 or opcion >4:
            print("Opcion fuera de rango")
            opcion = int(input("Elija una de las siguientes opciones:\n1. Ver estado de inscripción\n2. Cambiar clave\n3. Mostrar mensaje motivacional\n4. Salir\n"))
            
    print("Salida del sistema, hasta la proxima!")


# ============================================================
#Ejercicio 3: Sistema de turnos
# ============================================================
operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
    operador = input("Ingrese nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = 0

while opcion != 5:
    print("\nMENU")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion = input("Ingrese una opción válida (1 a 5): ")
    opcion = int(opcion)

    if opcion == 1:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Ingrese día válido (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Ingrese nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: paciente repetido en Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes - Turno 1")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes - Turno 2")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes - Turno 3")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes - Turno 4")
            else:
                print("No hay cupos disponibles en Lunes.")

        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: paciente repetido en Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes - Turno 1")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes - Turno 2")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes - Turno 3")
            else:
                print("No hay cupos disponibles en Martes.")

    elif opcion == 2:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Ingrese día válido (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Ingrese nombre del paciente a cancelar: ")
        while not paciente.isalpha():
            paciente = input("Ingrese nombre del paciente a cancelar: ")

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado en Lunes - Turno 1")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado en Lunes - Turno 2")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado en Lunes - Turno 3")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado en Lunes - Turno 4")
            else:
                print("Paciente no encontrado en Lunes.")

        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado en Martes - Turno 1")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado en Martes - Turno 2")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado en Martes - Turno 3")
            else:
                print("Paciente no encontrado en Martes.")

    elif opcion == 3:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Ingrese día válido (1=Lunes, 2=Martes): ")
        dia = int(dia)

        if dia == 1:
            print("Agenda de Lunes")
            print("Turno 1:", lunes1 if lunes1 != "" else "libre")
            print("Turno 2:", lunes2 if lunes2 != "" else "libre")
            print("Turno 3:", lunes3 if lunes3 != "" else "libre")
            print("Turno 4:", lunes4 if lunes4 != "" else "libre")
        else:
            print("Agenda de Martes")
            print("Turno 1:", martes1 if martes1 != "" else "libre")
            print("Turno 2:", martes2 if martes2 != "" else "libre")
            print("Turno 3:", martes3 if martes3 != "" else "libre")

    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        libres_martes = 3 - ocupados_martes

        print("Resumen general")
        print("Lunes - Ocupados:", ocupados_lunes, "Libres:", libres_lunes)
        print("Martes - Ocupados:", ocupados_martes, "Libres:", libres_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate entre ambos días.")

print("Sistema cerrado.")

# ============================================================
#Ejercicio 4: Escape room
# ============================================================
energia            = 100
tiempo             = 12
cerraduras_abiertas = 0
alarma             = False
codigo_parcial     = ""
forzar_seguidas    = 0   # contador para la regla anti-spam

print("=== ESCAPE ROOM: LA BÓVEDA ===\n")

nombre = ""
while not nombre.isalpha():
    nombre = input("Ingresá tu nombre de agente (solo letras): ").strip()
    if not nombre.isalpha():
        print("Nombre inválido. Usá solo letras, sin espacios ni números.")

print(f"\nBienvenido/a, agente {nombre.capitalize()}. ¡Buena suerte!\n")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    # -- Chequeo de bloqueo por alarma ANTES de cada turno ---
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSISTEMA BLOQUEADO: alarma activa y tiempo crítico. ¡Derrota por bloqueo!")
        break

    # -- Mostrar estado actual --
    print("─" * 40)
    print(f"  Energía : {energia:>3}  |  Tiempo: {tiempo:>2}  |  Cerraduras: {cerraduras_abiertas}/3")
    print(f"  Alarma  : {'ACTIVA' if alarma else 'OFF'}  |  Código parcial: '{codigo_parcial}' ({len(codigo_parcial)} letras)")
    print("─" * 40)
    print("  1. Forzar cerradura  (-20 energía, -2 tiempo)")
    print("  2. Hackear panel     (-10 energía, -3 tiempo)")
    print("  3. Descansar         (+15 energía,  -1 tiempo)")
    print("─" * 40)

    # -- Validar opción del menú --
    opcion = ""
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        opcion = input("Elegí una opción (1/2/3): ").strip()
        if not opcion.isdigit() or opcion not in ("1", "2", "3"):
            print("Opción inválida. Ingresá 1, 2 o 3.")

    #  OPCIÓN 1 — Forzar cerradura
    if opcion == "1":
        print("\n>> Intentás forzar la cerradura...")

        energia -= 20
        tiempo  -= 2
        forzar_seguidas += 1

        # Regla anti-spam: 3 veces seguidas forzando
        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó! La alarma se activó automáticamente.")
            alarma = True

        else:
            # Riesgo de alarma si energía < 40
            if energia < 40:
                print("¡Energía baja! Hay riesgo de alarma.")
                num_riesgo = ""
                while not num_riesgo.isdigit() or num_riesgo not in ("1", "2", "3"):
                    num_riesgo = input("Elegí un número del 1 al 3: ").strip()
                    if not num_riesgo.isdigit() or num_riesgo not in ("1", "2", "3"):
                        print("Ingresá 1, 2 o 3.")
                if num_riesgo == "3":
                    print("¡Mala suerte! La alarma se activó.")
                    alarma = True
                else:
                    cerraduras_abiertas += 1
                    print(f"¡Cerradura abierta! Total: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f"¡Cerradura abierta! Total: {cerraduras_abiertas}/3")

    #  OPCIÓN 2 — Hackear panel
    elif opcion == "2":
        print("\n>> Hackeando el panel de control...")

        energia -= 10
        tiempo  -= 3
        forzar_seguidas = 0

        # For de 4 pasos mostrando progreso
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 — código acumulado: '{codigo_parcial}'")

        # Si el código llega a 8+ letras, abre una cerradura (si faltan)
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f" ¡Código suficiente! Cerradura desbloqueada. Total: {cerraduras_abiertas}/3")

    #  OPCIÓN 3 — Descansar
    elif opcion == "3":
        print("\n>> Descansás un momento...")
        forzar_seguidas = 0   # corta la racha

        energia += 15
        if energia > 100:
            energia = 100       # tope máximo

        tiempo -= 1

        if alarma:
            print("La alarma está activa: perdés 10 energía extra.")
            energia -= 10

        print(f" Energía ahora: {energia}  |  Tiempo ahora: {tiempo}")

    # -- Chequeo de bloqueo por alarma DESPUÉS de la acción --
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSISTEMA BLOQUEADO: alarma activa con tiempo ≤ 3. ¡Derrota por bloqueo!")
        break

    print()   # línea en blanco entre turnos

#  CONDICIONES DE FIN
print("\n" + "=" * 40)
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA, agente {nombre.capitalize()}!")
    print("  Abriste las 3 cerraduras. La bóveda es tuya.")
elif energia <= 0:
    print(f"DERROTA — Te quedaste sin energía.")
elif tiempo <= 0:
    print(f"DERROTA — Se acabó el tiempo.")
else:
    print(f"DERROTA — La alarma bloqueó el sistema.")
print("=" * 40)


# ============================================================
# EJERCICIO 5: Juego Gladiador
# ============================================================
nombre_gladiador=input("Ingrese el nombre del gladiador: ")

while nombre_gladiador=="" or not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador=input("Ingrese el nombre del gladiador: ")

nombre_gladiador=nombre_gladiador.capitalize()

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3 
danio_base_gladiador = 15 
danio_base_enemigo = 12
turno_gladiador=True

while vida_gladiador>0 and vida_enemigo>0:
    if turno_gladiador:
        print(f"La vida de {nombre_gladiador} es {vida_gladiador}")
        print(f"La vida del enemigo es {vida_enemigo}")
        print(f"Cantidad de pociones de cura disponibles {pociones_vida}")
        while True:
            opcion=input('''
                Indique la accion a realizar:
                1)Ataque pesado
                2)Ataque por rafaga
                3)Curar
                ''')
            while opcion=="" or not opcion.isdigit():
                print("Error: Solo se permiten numeros")
                opcion=input('''
                Indique la accion a realizar:
                1)Ataque pesado
                2)Ataque por rafaga
                3)Curar
                ''')
            opcion=int(opcion)
            match opcion:
                case 1:
                    if vida_enemigo<20:
                        vida_enemigo=vida_enemigo-1.5*danio_base_gladiador
                        print(f"Atacaste al enemigo por {1.5*danio_base_gladiador} puntos de daño")
                    else:
                        vida_enemigo=vida_enemigo-danio_base_gladiador
                        print(f"Atacaste al enemigo por {danio_base_gladiador} puntos de daño")
                    turno_gladiador=False
                    break
                case 2:
                    rafaga=random.randint(1,4)
                    for _ in range(rafaga):
                        vida_enemigo-=5
                        print("> Golpe conectado por 5 de daño")
                    turno_gladiador=False
                    break
                case 3:
                    if pociones_vida>0:
                        vida_gladiador=vida_gladiador+30
                        pociones_vida-=1
                        print(f"Te curaste, tu vida sube a {vida_gladiador}")
                        print(f"Las pociones de cura quedan en {pociones_vida} pociones restantes.")
                    else:
                        print("No dispone de mas pociones de vida")
                        print("Pierdes el turno")
                    turno_gladiador=False
                    break
                case _:
                    print("La opcion ingresada no es valida")
                    print("Intente de nuevo")
    else:
        print("Turno de ataque del enemigo!!")
        vida_gladiador=vida_gladiador-danio_base_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador=True

if vida_gladiador>0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print(f"DERROTA. Has caído en combate.")
