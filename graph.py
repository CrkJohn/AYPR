from tkinter import *
from tkinter import font  as tkfont
from tkinter import messagebox

import datetime
import csv
import os
import getpass
import smtplib
import config

fields = ('Nombres', 'Apellidos', 'N° Carnet', '¿En que bloque quieres hacer la reserva?: ')
class Contenedor(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container =  Frame(self)
        self.title("Reservas")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, EliminarReserva,pageReserva):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        button1 =  Button(self, text="Crear Reserva",
                            command=lambda:controller.show_frame("pageReserva"))
        button2 =  Button(self, text="Eliminar Reserva",
                            command=lambda: controller.show_frame("EliminarReserva"))
        button1.pack()
        button2.pack()


class EliminarReserva( Frame):
    global ent

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label =  Label(self, text="Eliminar reservas", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        row = Frame(self)
        lab = Label(row, width=35, text="Numero de la reserva: ", anchor='w')
        self.ent = Entry(row)
        self.ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        self.ent.pack(side=RIGHT, expand=YES, fill=X)
        b1 = Button(self, text='eliminar',command=self.eliminar)
        b1.pack(side=LEFT, padx=5, pady=5)
        b3 = Button(self, text='Quit', command=controller.destroy)
        b3.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(self, text='Volver', command=lambda: controller.show_frame("StartPage"))
        b2.pack(side=LEFT, padx=5, pady=5)


            
    def eliminar(self):
        borrar1= int(self.ent.get())
        y = self.abrir()
        ind = -1
        for num,elementos in enumerate(y):
            if int(elementos[0]) == borrar1:
                ind = num
        if(ind != -1):
            y.pop(ind-1)
            self.sobreescribir(y)
        else:
            messagebox.showerror("ERROR","El número de la reserva no esta en la base de datos, intentelo mas tarde.")
    def abrir (self):
        with open ('Datos.csv') as archivo:
                leer= csv.reader(archivo)
                a= []
                for i in leer:
                        a.append(i)
        return a
        
    def sobreescribir(sefl,lista):
        try:
            archivito = open("Datos.csv","x")
        except:
             os.remove("Datos.csv")
             archivito = open("Datos.csv","x")
        for i in lista:
                archivito.write(",".join(i)+"\n")
        archivito.close()


class pageReserva(Frame):
    global mesasC,  mesasF , mesasD , cont , entries
    mesasC = 40
    mesasF = 18
    mesasD = 12
    cont = 0
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Reservas", font=controller.title_font)
        self.entries = self.makeform(self, fields)
        b1 = Button(self, text='Reservar',command=self.reservar)
        b1.pack(side=LEFT, padx=5, pady=5)
        b3 = Button(self, text='Quit', command=controller.destroy)
        b3.pack(side=LEFT, padx=5, pady=5)
        b2 = Button(self, text='Volver', command=lambda: controller.show_frame("StartPage"))
        b2.pack(side=LEFT, padx=5, pady=5)

        
    def makeform(self,root, fields):
       entries = {}
       for field in fields:
          row = Frame(root)
          lab = Label(row, width=35, text=field+": ", anchor='w')
          ent = Entry(row)
          ent.insert(0,"0")
          row.pack(side=TOP, fill=X, padx=5, pady=5)
          lab.pack(side=LEFT)
          ent.pack(side=RIGHT, expand=YES, fill=X)
          entries[field] = ent
       return entries
    
    def abrir (self):
            with open ('Datos.csv') as archivo:
                    leer= csv.reader(archivo)
                    a= []
                    for i in leer:
                            a.append(i)
            return a

  
    def reservar(self):
        global mesasC,  mesasF , mesasD , cont , entries
        #while (mesasC > 0) and (mesasF > 0) and (mesasD > 0):
        cont = int(cont) + 1
        sala= (self.entries['¿En que bloque quieres hacer la reserva?: '].get())
        nombre = (self.entries['Nombres'].get())
        apellido = self.entries['Apellidos'].get()
        carnet = self.entries['N° Carnet'].get()
        print(sala,nombre,apellido,carnet)
        confir = "SI"
        if (sala == "C") or (sala == "c") and (mesasC > 0):
                print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet + "  en la sala: " + sala)
                mesasC = mesasC - 1
                #confir= input("Todos los datos correctos: responda si o no   ")
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
                print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet+ "  en la sala: " + sala)
                mesasF = mesasF - 1
                #confir= input("Todos los datos correctos: responda si o no   ")
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
                print ("Los datos de la reserva son: " + nombre + " " + apellido + "  con el carnet: " + carnet+ "  en la sala: " + sala)
                mesasD = mesasD - 1
                #confir= input("Todos los datos correctos: responda si o no   ")
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
                        print  ("SU NUMERO DE RESERVA ES: " + str(cont))      
                else:
                        print ("Lo siento empieza el proceso de nuevo")
        


if __name__ == "__main__":
    app = Contenedor()
    app.mainloop()
