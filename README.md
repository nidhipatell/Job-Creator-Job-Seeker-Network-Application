# Job-Creator-Job-Seeker-Network-Application


##One-to-One Jobs

We created job-seeker and job-creator python programs to:

a. Detect the status of a given port at a given IP address. The status of the port could be open—close—filtered. The port could be TCP or UDP. The job description contains at least the target IP and port number, and 

b. Detect all live IP addresses on a given subnet. The job description contains the target subnet
in a.b.c.d/x format


Screenshots 1 - 5 show the following functions between the Client and Server:

SS 1. The Server connects to the Client (IP Address 127.0.0.1, Port # 56328).

SS 2. Client uses command REQUEST JOB, sent to Server.

SS 3. Job successful, Port # is 65432.

SS 4. Client uses command SEND JOB to Server, detection of Client status is checked by Server (Port # 65432 is Open).

SS 5. Client uses command SEND JOB to Server, detection of all live IP Addresses is successful (IP Addresses in given network's subnet are displayed).



##One-to-Many Jobs

We created job-seeker and job-creator python programs to:

a. Ask more than one job seeker to execute an ICMP flood attack against a given IP or subnet, and 

b. 

