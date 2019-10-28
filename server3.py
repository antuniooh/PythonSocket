# -*- coding: utf-8 -*-
import socket
from PIL import Image
port = 8000
host = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(5)



while True:
    conn, addr = s.accept()
    print('Conectado a {}'.format(addr))
    with open('logo_python.png', 'rb') as f:
        conn.send(f.read())
        l = f.read()
    #im = Image.open(l)
    #im.show()
        f.close()

print('Arquivo enviado')
