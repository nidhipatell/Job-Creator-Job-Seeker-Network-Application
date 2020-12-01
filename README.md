# Job-Creator-Job-Seeker-Network-Application


## One-to-One Jobs

We created job-seeker and job-creator python programs to:

a. Detect the status of a given port at a given IP address. The status of the port could be open—close—filtered. The port could be TCP or UDP. The job description contains at least the target IP and port number, and 

b. Detect all live IP addresses on a given subnet. The job description contains the target subnet
in a.b.c.d/x format


### *Screenshots 1 - 5 show the following functions between the Client and Server:*

SS 1. The Server connects to the Client (IP Address 127.0.0.1, Port # 56328).
![screenshot 1](/screenshots/1.png)

SS 2. Client uses command REQUEST JOB, sent to Server.
![screenshot 2](/screenshots/2.png)

SS 3. Job successful, Port # is 65432.
![screenshot 3](/screenshots/3.png)

SS 4. Client uses command SEND JOB to Server, detection of Client status is checked by Server (Port # 65432 is Open).
![screenshot 4](/screenshots/4.png)

SS 5. Client uses command SEND JOB to Server, detection of all live IP Addresses is successful (IP Addresses in given network's subnet are displayed).



## One-to-Many Jobs

We created job-seeker and job-creator python programs to:

a. Ask more than one job seeker to execute an ICMP flood attack against a given IP or subnet, and 

b. Ask more than one job seeker to execute a TCP flood attack ( any TCP flood attack) against a given port on a given IP.


### *Screenshots 6 - 10 show the following functionalities between the Clients and Server:*

SS 6. Server connects two Clients, Client #1 and Client #2

SS 7. Client #1 (127.0.0.1 58672) and Client #2 (127.0.0.1 58627) have connected to the Server

SS 8. Client #1 (127.0.0.1 58912) and #2 (127.0.0.1 58909), perform TCP Flood attack. Job is successful, sends 2501 packets to the Server through Port 65432. **Different port numbers in Client 1 and Client 2 are a result of a bug, and a typo in the sentence for Client 1 says the job belongs to Client 2.**

SS 9. Client #1 (127.0.0.1 59288) and #2 (127.0.0.1 59292), perform TCP Flood attack. Job is successful, sends 2501 packets to the Server through Port 65432. **Different port numbers in Client 1 and Client 2 are a result of a bug, and a typo in the sentence for Client 1 says the job belongs to Client 2.**

SS 10. Clients #1 and #2 use command QUIT, Server shows that connection between the clients and server is closed.

