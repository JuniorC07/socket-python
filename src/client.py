import socket
while True:
#criação do coket para o cliente
server = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
#definindo ip e porta
host= "127.0.0.1"
port = 8881
#leitura de uma string
msg = raw_input('Digite algo: ')
#conecta com o servidor
server.connect((host, port))
#envia para o servidor
server.send(msg)
#recebe dados do servidor
dados = server.recv(1024)#se for igual a sair ele sai do loop e fecha
if dados == "sair":
break;
#se não ele mostra a mensagem já convertida em
maiuscula
print(dados.decode('ascii'))
server.close()