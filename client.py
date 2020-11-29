import socket
import sys
from scapy.all import ARP, Ether, srp

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432       # The port used by the server
CLIENT_NUM = None
JOB = None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
    except  socket.error as e:
        print(str(e))
        
    Response = client.recv(1024)
    if Response.decode('utf-8')[:3] == "220":
        CLIENT_NUM = Response.decode('utf-8')[-1]
        print("Client: Client #" + str(CLIENT_NUM) + " Welcome to the Server")
    else:
        print("Client: Server is not ready please try again")
        
    while True:
        command = input("Enter your command type \help for help: ")
        if command == "QUIT":
            client.sendall(str.encode(command))
            sys.exit()
        
        elif command == "REQUEST JOB":
            client.sendall(str.encode(command))
            
        elif command == "CURRENT JOB":
            print("Client: Client #" + str(CLIENT_NUM) + " the current job is: " + JOB)
            continue
            
        elif command == "SEND JOB" and JOB:
            print("Client: Client #" + str(CLIENT_NUM) + " the current job is: ",
                  "Detect all live IP addresses on a given subnet: ", JOB[2:]+"/24")
            if JOB[0] == "3":
                target_ip = JOB[2:] + "/24"
                arp = ARP(pdst=target_ip)
                ether = Ether(dst="ff:ff:ff:ff:ff:ff")
                packet = ether/arp
                result = srp(packet, timeout=5, verbose=1)[0]
                ips = []
                for sent, received in result:
                    ips.append({'ip': received.psrc, 'mac':received.hwsrc})
                print("Abaliable devices in the network: ")
                print("IP" + " "*18 + "MAC")
                for ip in ips:
                    print("{:16}    {}".format(ip['ip'], ip['mac']))    
               
                client.sendall(str.encode(command))
                client.sendall(str(ips).encode())
            else:
                print("NO JOB TAKEN")
            continue
        
        elif command == "\help":
            print("""Commands Avaliable: 
                  ========================
                  \help - for help
                  QUIT - to QUIT the program
                  REQUEST JOB - request a job from job creator
                  CURRENT JOB - shows the current job given
                  SEND JOB - send the server""")
            continue
        
        else:
            print("Client: Client #" + str(CLIENT_NUM) + " invalid command try again!")
            continue
            
        Response = client.recv(1024)
        
        if Response.decode('utf-8')[:3] == "250":
            JOB = Response.decode('utf-8')[4:]
            print("Client: 250 Client #" + str(CLIENT_NUM) + " Job recieved and job is: " + JOB)
            
        elif Response.decode('utf-8')[:3] == '452':
            print("Client: 452 Client #" + str(CLIENT_NUM) + " you already haave a job taken")
        
        elif Response.decode('utf-8') == "251":
            print("Client: 251 Client #" + str(CLIENT_NUM) + " job was correctly done")
        
        elif Response.decode('utf-8') == "453":
            print("Client: 453 Client #" + str(CLIENT_NUM) + " job was not correctly done")
        
    client.close()