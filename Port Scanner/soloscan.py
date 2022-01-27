import socket

ip = input("Digite o host ou ip a ser verificado: ")
num = int(input("Digite a quantidade de portas a serem verificadas: "))

ports = []

while num > 0:
	ports.append(int(input("Digite a porta a ser verificada: ")))
	num -= 1

print("Resultado")
for port in ports:
	# socket.AF_INET -> IPV4 | socket.SOCK_STREAM -> TCP
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.05)

	code = client.connect_ex((ip, port)) # TCP socket error

	if code == 0:
		print(str(port), " -> Aberta")
	else:
		print(str(port), " -> Fechada")