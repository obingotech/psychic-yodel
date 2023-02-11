import subprocess

# Get output from MTR command
result = subprocess.run(['mtr', '--report', 'google.com'], stdout=subprocess.PIPE)

# Parse the output
for line in result.stdout.decode('utf-8').split('\n'):
    if not line.startswith('HOST'):
        print(line)

# Output:
#  1.|--
#  2.|--
