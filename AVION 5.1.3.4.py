from os import system

#Precios

asientoNormal = 78900
asientoVip = 240000

pasajeros = []
def CreaPasajero():
    nombre = input("Ingrese el nombre del pasajero: ")
    rut = input("Ingrese el rut del pasajero (Sin puntos y sin guión): ")

    while not (8 <= len(rut) <= 9):

        print("Rut inválido. ")
        
        rut = input("Ingrese el rut del pasajero (Sin puntos y sin guión): ")

    celular = input("Ingrese el numero celular del pasajero: ") 
    while not (celular.isdigit() and len(celular) == 9):
        print("Celular inválido. ")
        celular = input("Ingrese el numero celular del pasajero: ") 
    bancoelegido = banco()                                         #Llamando a banco y asignandolo en variable banco elegido. Para colocarla en el diccionario
    

    #Descuento 
    if bancoelegido == "Banco Duoc":
         print("")
         print("Felicidades tienes un descuento del 15%")
         print("")

         Descuento = True

    elif bancoelegido == "Otro medio de pago":
         print("")
         print("Pago tarifa normal, compra con BancoDuoc para más Beneficios ☆")
         print("")

         Descuento = False

    #pasajes
    
    while True:
        try:
            asiento_elegido = int(input("Escribe un numero de asiento a escoger,(del 1 al 42): "))
            if asiento_elegido in avion:
                if asiento_elegido >= 1 and asiento_elegido <= 30:
                    print("")
                    print("elegiste un asiento normal")
                    print("")

                    print("Escogiste correctamente el asiento nro: ", asiento_elegido)
                    print("")

                    if Descuento:
                        print("Con descuento BancoDuoc tu pasaje queda en: ", "$",asientoNormal * 0.75,  )
                    elif Descuento == False:
                        print("El pasaje tiene un valor de: ","$", asientoNormal )          
                    avion[asiento_elegido - 1] = '.X'
                        # Crear un diccionario con los datos del pasajero
                    pasajero = {
                        "nombre": nombre,
                        "rut": rut,                 
                        "celular": celular,
                        "banco": bancoelegido,
                        "asiento": asiento_elegido
                    }
                    pasajeros.append(pasajero) #Lista de diccionarios de pasajero
                    break
                elif asiento_elegido >= 31 and asiento_elegido <= 42:
                    print("")

                    print("Elegiste un asiento vip")
                    print("")
                    print("Escogiste correctamente el asiento nro: ", asiento_elegido)
                    print("")

                    if Descuento:
                        print("Con descuento BancoDuoc tu pasaje queda en: ", "$",asientoVip * 0.75,  )
                    elif Descuento == False:
                        print("El pasaje tiene un valor de: ","$", asientoVip )
                    avion[asiento_elegido - 1] = '.X'
                    pasajero = {
                        "nombre": nombre,
                        "rut": rut,                 
                        "celular": celular,
                        "banco": bancoelegido,
                        "asiento": asiento_elegido
                    }


                    pasajeros.append(pasajero)
                    break
            elif asiento_elegido not in avion:
                print("El asiento escogido no esta disponible, prueba con otro")
        except:
             print('intentalo nuevamente')


#Creacion de asientos
avion = []
for i in range (42):
    avion.append(i + 1)

#Bancos

def banco():
    sw = 0
    print("Bancos")
    print("1. Banco Duoc")
    print("2. Otro medio de pago")

    while sw == 0:

        bank = (input("Ingrese banco a elegir(1/2): "))
        if bank =="1":
            bancoelegido = "Banco Duoc"
            sw = 1
        elif bank =="2":
            bancoelegido = "Otro medio de pago"
            sw = 1
        else:
            print("Opcion inválida.")
            print("")

    return bancoelegido
        
#Menu de asientos
def asientos():
            print("---✈︎  AEROLÍNEAS DuocUC  ✈︎---")
            print("|  ","",avion[0],"",avion[1],"",avion[2],"     ", "",avion[3],"",avion[4],"",avion[5],"|")
            print("|  ","",avion[6],"", avion[7],"",  avion[8],"     ",      avion[9],  avion[10],  avion[11],"|")
            print("|  ",avion[12], avion[13],  avion[14],"     ",      avion[15],  avion[16],  avion[17],"|")
            print("|  ",avion[18], avion[19],  avion[20],"     ",      avion[21],  avion[22],  avion[23],"|")
            print("|  ",avion[24], avion[25],  avion[26],"     ",      avion[27],  avion[28],  avion[29],"|")
            print("|___________________________|")
            print("|___________________________|")
            print("|  ",avion[30], avion[31],  avion[32],"     ",      avion[33],  avion[34],  avion[35],"|")
            print("|  ",avion[36], avion[37],  avion[38],"     ",      avion[39],  avion[40],  avion[41],"|")

            print("---✈︎  AEROLÍNEAS DuocUC  ✈︎---")

def modificar_pasajero():
    asientoModificar= int(input("Número de asiento: "))
    rutModificar = input("RUT del pasajero: ")
    for pasajero in pasajeros:
        if pasajero['rut'] == rutModificar and pasajero['asiento'] == asientoModificar:
            if input("¿Modificar nombre? (s/n): ").lower() == 's':  
                pasajero["nombre"] = input("Nuevo nombre: ")
            if input("¿Modificar teléfono? (s/n): ").lower() == 's':
                pasajero["celular"] = input("Nuevo teléfono: ")
            print("Datos actualizados.")

        else:
            print("Datos no coinciden.")


while True:
    try:
        print("-- BIENVENIDO a AEROLÍNEAS DuocUC -✈︎")
        print("1. Ver asientos disponibles: ")
        print("2. Comprar asiento: ")
        print("3. Anular vuelo: ")
        print("4. Modificar datos del pasajero: ")
        print("5. Salir")

        print("6. Mostrar datos de los pasajeros. ")


        opcion = int(input("INGRESA OPCIÓN: "))
        print("")
        if opcion == 1:
            system('cls')

            asientos()
            input("presiona enter para volver al menú")
            system('cls')
        elif opcion == 2:
            system('cls')
            

            print("-- MENÚ DE COMPRA 🛒--")
            CreaPasajero()
            input("presiona ENTER para volver al Menú")
            system('cls')
        elif opcion == 3:
            system('cls')

            print("Has entrado en anular vuelo")
            while True:
                 try:
                    anularvuelo = int(input("Ingrese número de asiento a anular: "))
                    if avion[anularvuelo - 1] == ".X":
                        print("Pasaje Anulado exitosamente")
                        avion[anularvuelo - 1] = anularvuelo 
                        for pasajero in pasajeros:
                            if pasajero["asiento"] == anularvuelo:
                                pasajeros.remove(pasajero)

                    else:
                        print("No se pudo anular")
                    input("Presiona ENTER para volver al Menú")
                    system('cls')

                    break
                 except:
                     print("ingresa un valor numerico")
                     print('')
                     print('')
                     print("||||||||||||||||||||||||||||||||||")
                     input("Presiona enter para volver al menú")
                     print("||||||||||||||||||||||||||||||||||")
                     system('cls')
                     
                     
                     break
                     

        elif opcion == 4:
            system('cls')

            print("MODIFICAR DATOS DEL PASAJERO: ")#Opcion para revisar que los datos se esten almacenando/Guardando/Modificando de manera correcta
            modificar_pasajero()
            input("Presiona ENTER para volver al Menú")
            system('cls')
        elif opcion == 5:
            print("Hasta luego...")
            break
        elif opcion == 6:
                for pasajero in pasajeros:
                    print(pasajero)
                    print("")
                    

    except:
        print("try again, sorry")