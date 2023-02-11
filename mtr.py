import subprocess
import re

def mtr_trace(hostname):
    mtr = subprocess.Popen(['mtr', '-r', '-c', '1', hostname], stdout=subprocess.PIPE)
    mtr.wait()
    mtr_out = mtr.stdout.read().decode('utf-8')
    mtr_out = mtr_out.splitlines()
    mtr_out = mtr_out[1:-1]
    mtr_out = [re.sub(' +', ' ', x) for x in mtr_out]
    mtr_out = [x.split(' ') for x in mtr_out]
    mtr_out = [[x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12]] for x in mtr_out]
    return mtr_out

if __name__ == '__main__':
    mtr_out = mtr_trace('google.com')
    print(mtr_out)



