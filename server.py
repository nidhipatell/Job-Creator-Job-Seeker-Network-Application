import socket
from _thread import *
import threading
import random

HOST = '127.0.0.1'
PORT = 65432
THREADCOUNT = 0
CLIENT_WITH_JOB = set()
JOBS = ['3+3', '5*6+9']

def threaded_server(connection, addr):
    print(addr)
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
            break
        
        elif data.decode('utf-8') == "REQUEST JOB" and not job_given:
            current_job = random.choice(JOBS)
            connection.sendall(str.encode("250 " + str(current_job)))
            job_given = True
            print("Server: 250 job send to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
        
        elif data.decode('utf-8') == "REQUEST JOB" and job_given:
            connection.sendall(str.encode("452"))
            print("Server: 452 job is already sent to Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]))
        
        elif data.decode('utf-8') == "SEND JOB":
            answer = connection.recv(2048)
            job_given = False
            if int(eval(current_job)) == int(answer.decode('utf-8')):
                connection.sendall(str.encode("251"))
                print("Server: 251 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " got the right answer")
            else:
                connection.sendall(str.encode("453"))
                print("Server: 251 Client #" + str(THREADCOUNT) + " with address of " + str(addr[0]), str(addr[1]) + " got the wrong answer")
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