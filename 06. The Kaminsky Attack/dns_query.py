#!/usr/bin/python3
from scapy.all import *

#Task 2: Construct DNS request

Qdsec = DNSQR(qname='www.example.com')

dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec)

ip = IP(dst='10.9.0.53', src='10.9.0.5')

udp = UDP(dport=53, sport=1111, chksum=0)

request = ip/udp/dns

#with open('ip_req.bin', 'wb') as f:
#  f.write(bytes(request))

request.show()
send(request)
