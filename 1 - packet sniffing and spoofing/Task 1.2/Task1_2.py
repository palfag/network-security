## Spoofed ICMP Echo request

from scapy.all import *

a = IP()
a.dst = '10.9.0.5'
a.src = '10.9.0.10'

b = ICMP()

p = a / b

send(p)