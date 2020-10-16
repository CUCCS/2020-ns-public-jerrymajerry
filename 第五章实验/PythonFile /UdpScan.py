#!/usr/bin/env python-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

dst_ip = "172.16.111.102"
src_port = RandShort()
dst_port = 53

pkt=IP(dst=dst_ip)/UDP(dport=dst_port)
res=sr1(pkt, timeout=5, verbose=False)
if res==None:
	print("open or filtered")
elif res.haslayer(ICMP):
        if res.getlayer(ICMP).type == 3 and res.getlayer(ICMP).code == 3:
	        print("closed")