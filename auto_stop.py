import subprocess
import logging

cmd = 'docker attach --no-stdin --sig-proxy=false 14cbb8b6f538'

def main():
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
        print(line)
    