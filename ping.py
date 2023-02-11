import os

import time


hostname = "www.google.com"
response = ping.Ping().ping(hostname)
if response.is_reached():
    print("Host is reachable, latency is ", response.avg_rtt, "ms")
else:
    print("Host is unreachable")












 




