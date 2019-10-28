# -*- coding: utf-8 -*-
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',1112))
print ('Socket criado!')
sock.listen(5)
print ('Esperando conexão...')
conn, addr = sock.accept()
print ('Nova conexão de',addr,'!')
#Abrir arquivo
flname = ('arquivo_teste.jpg')
fyle = open(flname, 'rb')
kar = fyle.read(6053)
conn.send(kar)
print ('Arquivo enviado!')
fyle.close()
conn.close()
sock.close()
