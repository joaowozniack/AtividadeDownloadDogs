import socket
import sys
import os

ip = '127.0.0.1'
porta = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((ip, porta))
except:
    print(' # erro de bind')
    sys.exit()

while True:
    data, addr = s.recvfrom(1024)
    print('sensor ', addr, ' enviou: ', data)
    os.remove(data)

print('o servidor encerrou')
s.close()