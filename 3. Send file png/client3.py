# -*- coding: utf-8 -*-
import socket
from PIL import Image
host = '127.0.0.1'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("Recebendo Dados...\n")
with open('recebido.png', 'wb') as f:
        print('file opened')
        print('Recebendo dados...')
        data = s.recv(200000)
        f.write(data)
        print(data)
        print("ENVIADO")
        f.close()
with open('recebido.png', 'rb') as f:
        im = Image.open(f)
        im.show()

print('Transferência completa!!!')
s.close()
print('Conexão encerrada.')
