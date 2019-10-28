# Cliente 
import socket
 
print ("Cliente")
 
HOST='localhost' #coloca o host do servidor 
PORT=57000
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
print ("conectando com servidor...")
s.connect((HOST,PORT)) #conecta na mesma porta e no mesmo host
 
print ("abrindo arquivo...")
arq = open('message.txt','rb')

print("enviado arquivo")
for i in arq:
    #print i
    s.send(i)
 
print("saindo...")
arq.close()
s.close()
