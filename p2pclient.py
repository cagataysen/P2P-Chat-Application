import socket 
import json

def returnUserIP(username, dicti):
    for ips in dicti:
        name = dicti[ips]
        if name == username:
            return ips

    print("couldnt find")
    return -1


    
while True:

    try:
        with open('dictionary.json') as f:
            dicti = json.load(f)

    except:
        print("cdnt open dictionary")    

    print(json.dumps(dicti, indent=4, sort_keys=True))

    select = input("Type in username to send a message")
    print(dicti)

    


    TCP_IP = returnUserIP(select,dicti)
    TCP_PORT = 5001
    BUFFER_SIZE = 1024
    
    if TCP_IP != -1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(TCP_IP)
        try:
            s.connect((TCP_IP, TCP_PORT))
            msg = input("mesaj ne = ")
            s.send(msg.encode('utf-8'))
            print("message sent: " + msg)
            s.close()
        except:
            print("couldnt connect")
