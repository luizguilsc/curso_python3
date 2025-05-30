import subprocess
import sys

print(sys.platform)

cmd = ['ping', '8.8.8.8']

proc = subprocess.run(
    cmd, capture_output=True,
    text=True,
)

# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)