import time
import subprocess
import psutil



def get_speed():
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

        print(f"{mb_recv:.2f} MB/s received, {mb_sent:.2f} MB/s sent, {mb_total:.2f} MB/s total", {time.strftime("%H:%M:%S")})

        last_recv = recv
        last_sent = sent
        last_total = total

        time.sleep(1)

print("Starting iperf3 server...")
subprocess.Popen(["iperf3", "-s"])
time.sleep(1)
print("Starting iperf3 client...")
subprocess.Popen(["iperf3", "-c", ""])
time.sleep(1)
print("Starting speed test...")
get_speed()

# Output:
# Starting iperf3 server...
# Starting iperf3 client...
# Starting speed test...
# 0.00 MB/s received, 0.00 MB/s sent, 0.00 MB/s total {'11:00:00'}
# 0.00 MB/s received, 0.00 MB/s sent, 0.00 MB/s total {'11:00:01'}
# 0.00 MB/s received, 0.00 MB/s sent, 0.00 MB/s total {'11:00:02'}
#  




