import socket
import sys

ip = input('Entre com o ip do servidor ')
porta = int(input('Entre com a porta do server '))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((ip, porta))
except:
    print('Erro de bind')
    sys.exit()

while True:
    data, addr = s.recvfrom(1024)
    print('sensor ', addr, 'enviou ', data)

print('O servidor encerrou')
s.close()