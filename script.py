#!/usr/bin/env python3
import sys
from scapy.all import *
from time import *

def traceroute(url):
    responses = {}
    for i in range(30):
        print()
        for ttl in range(1,25):
            probe = IP(dst=url, ttl=ttl) / ICMP()
            t_i = time()
            ans = sr1(probe, verbose=False, timeout=0.8)
            t_f = time()
            rtt = (t_f - t_i)*1000
            if ans is not None:

                if ttl not in responses: 
                    responses[ttl] = []
                responses[ttl].append((ans.src, rtt))

                if ttl in responses: 
                    print(ttl, responses[ttl])