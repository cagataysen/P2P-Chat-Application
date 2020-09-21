import socket
import time
import json

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


message = input("enter your username: ")
broadcastJSON = {"username":message,"ip_address":socket.gethostbyname(socket.gethostname())}
broadcastJSON = json.dumps(broadcastJSON)
while True:
    server.sendto(broadcastJSON.encode('utf-8'), ('<broadcast>', 5000 ))
    print("message sent!!!")
    time.sleep(5)
