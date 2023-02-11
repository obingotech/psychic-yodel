import subprocess
import re

def mtr_trace(hostname):
    mtr = subprocess.Popen(['mtr', '--no-dns', '--report', hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = mtr.communicate()
    lines = out.decode().split("\n")
    
    hops = []
    for line in lines:
        match = re.match("(\d+)\s+(\S+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\S+)", line)
        if match:
            hops.append({
                'hop': match.group(1),
                'hostname': match.group(2),
                'loss': match.group(3),
                'sent': match.group(4),
                'last': match.group(5),
                'best': match.group(6)
            })
    
    return hops

print(mtr_trace("google.com"))
