#!/usr/bin/env python-
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

dst_ip = "172.16.111.102"
src_port = RandShort()
dst_port = 80

pkt=IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags='')
res=sr1(pkt, timeout=5, verbose=False)
if res==None:
    print("open or closed or filtered")
elif res.haslayer(TCP):
    if res.getlayer(TCP).flags== 'AR':
        print("closed")
