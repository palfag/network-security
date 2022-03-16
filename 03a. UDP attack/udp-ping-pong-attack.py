#!/usr/bin/python3

from scapy.all import *

print("Triggering UDP Ping Pong...")

ip = IP(src="10.9.0.6", dst="10.9.0.7")
udp = UDP(sport=9090, dport=9090)
data = "Let the Ping Pong game start!\n"
pkt = ip/udp/data
send(pkt)
