import getpass
import smtplib
import config
CORREO = input ("Ingresa tu correo:   ")
CONTRASEÑA = getpass.win_getpass ()

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD) and (CORREO, CONTRASEÑA)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, CORREO, message)
        server.quit()
        print("Enviamos los datos de tu reserva al Correo")
    except:
        print("Algo fallo con tu cuenta, verifica tu correo")


subject = "Reserva Exitosa"
msg = "Hola, tienes una reserva en la sala de estudio del bloque F, a las 5:30 p.m"

send_email(subject, msg)
