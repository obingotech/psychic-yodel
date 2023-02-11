import time
import psutil


last_recv = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_recv + last_sent

while True:
    recv = psutil.net_io_counters().bytes_recv
    sent = psutil.net_io_counters().bytes_sent
    total = recv + sent
 
    recv_speed = recv - last_recv
    sent_speed = sent - last_sent
    total_speed = total - last_total

    mb_recv = recv_speed / 1024.0 / 1024.0
    mb_sent = sent_speed / 1024.0 / 1024.0
    mb_total = total_speed / 1024.0 / 1024.0

    print(f"{mb_recv:.2f} MB/s received, {mb_sent:.2f} MB/s sent, {mb_total:.2f} MB/s total",{time.strftime("%H:%M:%S")})

    last_recv = recv
    last_sent = sent
    last_total = total

    time.sleep(1)

