from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template




#funcion de prueba
def enviar_correo_prueba():

    subject = 'Notificacion de pedido'

    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    ['jdvera@espol.edu.ec']) #Destinatario

    message.attach_alternative('hola', 'text/html')
    message.send()

    print('correo enviado')
    
    
#funcion de prueba
def enviar_correo(usuario,password,correo):

    subject = 'Cambio de password'
    
    mensaje='Hola '+usuario+' '+'tu contraseña actual es: '+password

    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [correo]) #Destinatario


    message.attach_alternative(mensaje, 'text/html')
    message.send()

    print('correo enviado')

