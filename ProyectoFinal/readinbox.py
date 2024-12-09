import imaplib
import os

SERVER= 'imap.gmail.com'
USER='correoarquitectura976'
PASS='xfyiphumvjnfhxav'
MAIL='correoarquitectura976@gmail.com'

#Conectar al Servidor
server=imaplib.IMAP4_SSL(SERVER,993)

#logueo
server.login(USER,PASS)

#Acceder a las Bandejas
status, count=server.select('Inbox')
status, data=server.fetch(count[0],'(UID BODY[TEXT])')

flag=str((data[0][1]))
print(flag)

server.close()
server.logout()

