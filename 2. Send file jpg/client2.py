# -*- coding: utf-8 -*-
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1112))
flname = ('recebido.jpg')
fyle = open(flname,'wb')
print ('Iniciando...')
fyle.write(sock.recv(6053))
fyle.close()
sock.close()
print ('Arquivo enviado!')
