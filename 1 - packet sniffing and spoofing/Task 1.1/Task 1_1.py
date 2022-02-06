#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-3358d468f944', filter='src host 10.9.0.6 and tcp and dst port 23', prn=print_pkt)


# 1. Capture only the ICMP packet
# filter='icmp'

# 2. Capture any TCP packet that comes from a particular IP and with a destination port number 23
# filter='src host 10.9.0.6 and tcp and dst port 23'

# 3. Capture packets comes from or to go to a particular subnet
# filter='net 10.9.0.0/24'