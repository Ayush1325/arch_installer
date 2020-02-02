import subprocess

def format_all():
    subprocess.run(['mkfs.ext4', '-F', '/dev/sda'])