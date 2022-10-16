#!/usr/bin/env python3
import sys
from urllib import response
from scapy.all import *
from time import *
import json
from collections import OrderedDict


def traceroute(url):
    responses = {}
    routes = set()
    for _ in range(30):
        route = []
        for ttl in range(1, 25):
            probe = IP(dst=url, ttl=ttl) / ICMP()
            t_i = time()
            ans = sr1(probe, verbose=False, timeout=0.8)
            t_f = time()
            rtt = (t_f - t_i)*1000
            if ans is not None:

                if ttl not in responses:
                    responses[ttl] = []
                route.append(ans.src)
                responses[ttl].append((ans.src, rtt))
        # remuevo ips duplicadas consecutivas
        route = [route[i]
                 for i in range(1, len(route)) if route[i] != route[i-1]]
        routes.add(tuple(route))
    return responses, routes


url = 'vnu.edu.vn'
responses, routes = traceroute(url)
file_name = url.replace(".", "_")
with open(f'traceroute_results/{file_name}_responses.json', 'w') as f_responses:
    json.dump(responses, f_responses)
with open(f'traceroute_results/{file_name}_routes.json', 'w') as f_routes:
    json.dump(tuple(routes), f_routes)

print("Finished!")
