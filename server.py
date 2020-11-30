import socket
from _thread import *
import threading
import random

HOST = '127.0.0.1'
PORT = 65432
THREADCOUNT = 0
CLIENT_WITH_JOB = set()
JOBS = ['3 ' + socket.gethostbyname(socket.gethostname()), '2 ' + HOST + ' ' + str(PORT)]
JOBS_MULTIPLE = ['4 ' + HOST + ' ' + str(PORT), '5 ' + HOST + ' ' + str(PORT)]
given = []
def threaded_server(connection, addr):
    global THREADCOUNT, given
    print(addr, THREADCOUNT)
    job_given = False
    current_job = None
    connection.send(str.encode("220 " + str(THREADCOUNT)))
    
    print("220 Welcome to the Server you are Client #" + str(THREADCOUNT))
    while True:
        #print("Waiting for data from client #" + str(THREADCOUNT))
        data = connection.recv(2048)
        
        if not data:
            print("Server: Client #" + str(THREADCOUNT), "did not send any commands")
            break
        
        elif data.decode('utf-8') == "QUIT":
            print("Server: 221 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " closing connection")
            THREADCOUNT -= 1
            break
        
        elif data.decode('utf-8') == "REQUEST JOB" and not job_given:
            if THREADCOUNT == 1:
                current_job = random.choice(JOBS)
                connection.sendall(str.encode("250 " + str(current_job)))
                job_given = True
                print("Server: 250 job send to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
            else:
                if not given:
                    current_job = random.choice(JOBS_MULTIPLE)
                    given.append(current_job)
                    connection.sendall(str.encode("250 " + str(current_job)))
                    job_given = True
                    print("Server: 250 job send to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
                else:
                    current_job = given[0]
                    connection.sendall(str.encode("250 " + str(current_job)))
                    job_given = True
                    print("Server: 250 job send to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
                
        
        elif data.decode('utf-8') == "REQUEST JOB" and job_given:
            connection.sendall(str.encode("452"))
            print("Server: 452 job is already sent to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
        
        elif data.decode('utf-8') == "SEND JOB":
            answer = connection.recv(4096)
            job_given = False
            data = answer.decode('utf-8')
            data = eval(data)
            if data[-1] == 3:
                print("Abaliable devices in the network: ")
                print("IP" + " "*18 + "MAC")
                for ip in data:
                    print("{:16}    {}".format(ip['ip'], ip['mac'])) 
                print("Server: 251 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " did the job correctly")
            elif data[-1] == 2:
                print("The ip address:",data[0], "and the port:",data[1],"has the status:",data[2])
                print("Server: 251 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " did the job correctly")
            elif data[-1] == 4:
                given=[]
                print("The ip address:",data[0], "and the port:", data[1],"was used for a TCP/SYN Flood attack by sending over:", data[3], "packets")
                print("Server: 251 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " did the job correctly")
            
            
            current_job = None
            
    connection.close() 

def main():
    global THREADCOUNT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        try:
            server.bind((HOST, PORT))
        except socket.error as e:
            print(str(e))
        print("Waiting for a connection")
        server.listen(5)
        while True:

            conn, addr = server.accept()
            print("Connected to:", addr[0], addr[1])

            start_new_thread(threaded_server, (conn, addr))
            THREADCOUNT += 1
        server.close()

if __name__ == "__main__":
    main()