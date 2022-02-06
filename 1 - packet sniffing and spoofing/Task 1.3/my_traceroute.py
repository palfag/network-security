from tabnanny import verbose
from scapy.all import *
from scapy.layers.inet import *


counter = 1

def print_pkt(pkt):
    my_traceroute(pkt)


def my_traceroute(pkt):
    global counter
    if ICMP in pkt \
            and pkt[ICMP].type == 11\
            and pkt[ICMP].code == 0:
        print("{}: {}".format(counter, pkt[IP].src))
        counter = counter + 1
        a.ttl = a.ttl + 1
        send(a/b, verbose = 0)
    if ICMP in pkt \
            and pkt[ICMP].type == 0\
            and pkt[ICMP].code == 0:
        print("{}: {}".format(counter, pkt[IP].src))
        print("*************** The End **************")
        sys.exit(0)


a = IP()
print("**** Welcome on palfag Traceroute ****")
a.dst = input("Select an IP: ")
a.ttl = 1
b = ICMP()
send(a/b, verbose = 0)
pkt = sniff(iface='en0', filter='', prn=my_traceroute)
