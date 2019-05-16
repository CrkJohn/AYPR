import datetime
import csv
import os
import getpass
import smtplib
import config

CORREO = input ("Ingresa tu correo:   ")
CONTRASEÑA = getpass.win_getpass ()

def login(CORREO, CONTRASEÑA):
        try:
                server = smtplib.SMTP('smtp.office365.com:587')
                server.ehlo()
                server.starttls()
                server.login(CORREO, CONTRASEÑA)
                print("Ingreso exitoso")
        except:
                print("Válido unicamente para estudiantes de la ECI")
login(CORREO, CONTRASEÑA)
print (datetime.datetime.today())
print ("Hola, bienvenido al programa de reservas de salas de estudio")
mesasC = 40
mesasF = 18
mesasD = 12
cont = 0
def abrir ():
        with open ('Datos.csv') as archivo:
                leer= csv.reader(archivo)
                a= []
                for i in leer:
                        a.append(i)
        return a

def sobreescribir(lista):
        try:
                archivito = open("Datos.csv","x")
        except:
                os.remove("Datos.csv")
                archivito = open("Datos.csv","x")
        for i in lista:
                archivito.write(",".join(i)+"\n")
        archivito.close()
while (mesasC > 0) and (mesasF > 0) and (mesasD > 0):
        print ("EL SIGUIENTE ES NUESTRO MENU: ")                                                                        
        print ("1. Hacer una reserva")
        print ("2. Mostrar las reservas hechas")
        print ("3. Borrar una reserva")
        print ("4. Salir")
        opcion = int(input("Seleccione una opcion del menú:   "))
        if (opcion == 1):
                
                cont = int(cont) + 1
                print ("Las siguientes son la cantidad de mesas disponibles:  ")
                print ("Bloque C: " + str(mesasC) + "  mesas")
                print ("Bloque F: " + str(mesasF) + "  mesas")
                print ("Bloque D: " + str(mesasD) + "  mesas")
                sala= input ("¿En que bloque quieres hacer la reserva?:  ")
                if (sala == "C") or (sala == "c") and (mesasC > 0):
                        nombre = input ("Digite su nombre:   ")
                        apellido = input ("Digite su apellido:   ")
                        carnet = input ("Digite el numero de carnet:   ")

                        print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet + "  en la sala: " + sala)
                        mesasC = mesasC - 1
                        confir= input("Todos los datos correctos: responda si o no   ")
                        if (confir == "si") or (confir == "SI"):
                        
                                archivo = open ("Datos.csv", "a")
                                archivo.write (str(cont))
                                archivo.write (",")
                                archivo.write (nombre)
                                archivo.write (",")
                                archivo.write (apellido)
                                archivo.write (",")
                                archivo.write (carnet)
                                archivo.write (",")
                                archivo.write (sala)
                                archivo.write ("\n")

                                archivo.close ()
                                def send_email(subject, msg):
                                        try:
                                                server = smtplib.SMTP('smtp.gmail.com:587')
                                                server.ehlo()
                                                server.starttls()
                                                server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                                                message = 'Subject: {}\n\n{}'.format(subject, msg)
                                                server.sendmail(config.EMAIL_ADDRESS, CORREO, message)
                                                server.quit()
                                                print("Enviamos los datos de tu reserva al Correo")
                                        except:
                                                print("Algo fallo con tu cuenta, verifica tu correo")


                                subject = "Reserva Exitosa"
                                msg = "Hola, la reserva fue exitosa." + "\n" + " Datos: " + nombre + " " + " " + apellido + "\n" + carnet + " en la sala " + sala + " con el numero de reserva: " + str(cont) 

                                send_email(subject, msg)
                                
                                print ("LA RESERVA FUE EXITOSA")
                                print  ("SU NUMERO DE RESERVA ES: " + str(cont) )
                                
                        else:
                                print ("Lo siento empieza el proceso de nuevo")

                elif (sala == "F") or (sala == "f") and (mesasF > 0):
                        nombre = input ("Digite su nombre:   ")
                        apellido = input ("Digite su apellido:   ")
                        carnet = input ("Digite el numero de carnet:   ")

                        print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet+ "  en la sala: " + sala)
                        mesasF = mesasF - 1
                        confir= input("Todos los datos correctos: responda si o no   ")
                        if (confir == "si") or (confir == "SI"):
                        
                                archivo = open ("Datos.csv", "a")
                                archivo.write (str(cont))
                                archivo.write (",")
                                archivo.write (nombre)
                                archivo.write (",")
                                archivo.write (apellido)
                                archivo.write (",")
                                archivo.write (carnet)
                                archivo.write (",")
                                archivo.write (sala)
                                archivo.write ("\n")

                                archivo.close ()
                                print ("LA RESERVA FUE EXITOSA")
                                print  ("SU NUMERO DE RESERVA ES: " + str(cont) )
                        
                        else:
                                print ("Lo siento empieza el proceso de nuevo")

                elif (sala == "D") or (sala == "d") and (mesasD > 0):
                        nombre = input ("Digite su nombre:   ")
                        apellido = input ("Digite su apellido:   ")
                        carnet = input ("Digite el numero de carnet:   ")

                        print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet+ "  en la sala: " + sala)
                        mesasD = mesasD - 1
                        confir= input("Todos los datos correctos: responda si o no   ")
                        if (confir == "si") or (confir == "SI"):
                        
                                archivo = open ("Datos.csv", "a")
                                archivo.write (str(cont))
                                archivo.write (",")
                                archivo.write (nombre)
                                archivo.write (",")
                                archivo.write (apellido)
                                archivo.write (",")
                                archivo.write (carnet)
                                archivo.write (",")
                                archivo.write (sala)
                                archivo.write ("\n")

                                archivo.close ()
                                print ("LA RESERVA FUE EXITOSA")
                                print  ("SU NUMERO DE RESERVA ES: " + str(cont) )
                        
                        else:
                                print ("Lo siento empieza el proceso de nuevo")
        if (opcion == 2):
                print ("Los registros existentes son:  ")
                archivo = open("Datos.csv")

                print (archivo.read())

                archivo.close()                
        if (opcion == 3):
                borrar1= int(input ("Digite su numero de reserva:  "))
                y = abrir()
                y.pop(borrar1)
                sobreescribir(y)
                
        if (opcion == 4):
                exit()



