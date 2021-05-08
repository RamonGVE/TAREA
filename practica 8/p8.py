import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

mensaje = input('Ingresa un mesaje: ')

password = input('Ingresa una contraseña: ')
msg['From'] = input('Ingresa tu direccion de correo electronico: ')
msg['To'] = input('Ingresa el correo electronino al que se quiere mandar : ')
msg['Subject'] = input('Descripción: ')

msg.attach(MIMEText(mensaje, 'plain'))

servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()

servidor.login(msg['From'], password)

servidor.sendmail(msg['From'], msg['To'], msg.as_string())
servidor.quit()

print('Mensaje Enviado exitosamente a el correo', msg['To'])
