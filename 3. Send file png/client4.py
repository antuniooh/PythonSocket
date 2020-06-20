# Cliente 
import socket
 
print ("Cliente")
 
HOST='localhost'
PORT=57000
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
print ("conectando com servidor...")
s.connect((HOST,PORT)) 
 
print ("abrindo arquivo...")
arq = open('teste.png','rb')

print("enviado arquivo")
for i in arq:
    s.send(i)
 
print("saindo...")
arq.close()
s.close()
