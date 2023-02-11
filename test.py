import math

def MTR_bw(packet_size, time_interval):
    bits_per_packet = packet_size * 8
    bits_per_sec = bits_per_packet / time_interval
    return math.floor(bits_per_sec / 1000) # convert bits/sec to kbits/sec

# example
packet_size = 1000 # bytes
time_interval = 0.2 # seconds

print(MTR_bw(packet_size, time_interval)) # 5000 kbits/sec
