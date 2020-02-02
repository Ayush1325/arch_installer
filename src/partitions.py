import subprocess

def format_all():
    subprocess.run(['mkfs.ext4', '-F', '/dev/MainLinux/lvolroot'])
    subprocess.run(['mkfs.ext4', '-F', '/dev/MainLinux/lvolhome'])

def swap_space():
    subprocess.run(['mkswap', '/dev/MainLinux/lvolswap'])
    subprocess.run(['swapon', '/dev/MainLinux/lvolswap'])

def mount_all():
    subprocess.run(['mount', '/dev/MainLinux/lvolroot', '/mnt'])
    subprocess.run(['mkdir', '/mnt/home'])
    subprocess.run(['mount', '/dev/MainLinux/lvolhome', '/mnt/home'])
