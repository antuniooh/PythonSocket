# Servidor
import socket
print ("Servidor")
 
HOST = '10.113.22.1'
PORT = 57000
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Escutando a porta...", HOST)
s.bind((HOST,PORT))
s.listen(1)
 
print ("Aceitando a conexao...")
conn,addr= s.accept()

print ('Nova conexão de',addr,'!')

 
print ("recebendo o arquivo...")
arq = open('testeOut','wb')
 
while 1:
    dados=conn.recv(20000)
    if not dados:
        break
    arq.write(dados)
 
print ("saindo...")


arq.close()
conn.close()
