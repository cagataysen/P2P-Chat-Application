import socket

while True:
  TCP_IP = ''
  TCP_PORT = 5001
  BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
      
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((TCP_IP, TCP_PORT))
  s.listen(1)
    
  conn, addr = s.accept()
  print ('Connection address:'+ str(addr))
  while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:"+ data.decode('utf-8'))

  conn.close()