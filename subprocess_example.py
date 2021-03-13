import subprocess

"""
The subprocess module allows you to spawn new processes,
connect to their input/output/error pipes, and obtain their return codes.
eg: df -h
subprocess.Popen
"""

cmd = "df -h"

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out, err = p1.communicate()

print('out: {0}'.format(out))
print('error : {0}'.format(err))

if p1.returncode == 0:
    print('command : success')
else:
    print('command : failed')
