import socket
#criação do socket tcp/ip
s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
#definindo ip/porta
host = "127.0.0.1"
porta = 8881
#atribuindo ao socket
s.bind((host, porta))
#o mesmo fica “Escutando” até 5 terminais
diferentes
s.listen(5)while True: #laço sempre verdadeiro para sempre
que receber faça algo
#aceita a conexão do cliente
c, e = s.accept()
#recebe os dados do cliente
dados = c.recv(1024)
#se for sair ele retorna sair para o cliente
if dados == "sair":
c.send(dados)
#se não ele converte a variável para maiuscula e
envia ela convertida para o cliente
else:
print(dados)
print("Convertendo Mensagem")
msg = dados.upper()
c.send(msg.encode('ascii'))
c.close()