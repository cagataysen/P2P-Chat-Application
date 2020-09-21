import socket
import json


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 5000))

data = {}

while True:
    msg, addr = client.recvfrom(1024)
    gelen = msg.decode('utf-8')
    print("received message: " + gelen)
    geljson = json.loads(gelen)


    print(addr)
    try:
        if data[geljson["ip_address"]] != geljson["username"]:
            data[geljson["ip_address"]]= geljson["username"]
        
    except:
        data[geljson["ip_address"]]= geljson["username"]

    with open('dictionary.json', 'w') as f:
        json.dump(data,f)





    