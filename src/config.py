import subprocess

def time_zone():
    subprocess.run(['ln', '-sf', '/usr/share/zoneinfo/Asia/Kolkata', '/etc/localtime'])
    subprocess.run(['hwclock', '--systohc'])

def grub():
    subprocess.run(['mkdir', '/efi'])
    subprocess.run(['mount', '/dev/sda2', '/efi'])
    subprocess.run(['rm', '-rf', '/efi/EFI/GRUB'])
    subprocess.run(['grub-install', '--target=x86_64-efi', '--efi-directory=/efi', '--bootloader-id=GRUB'])
    subprocess.run(['grub-mkconfig', '-o', '/boot/grub/grub.cfg'])

def user():
    subprocess.run(['useradd', '-m', '-G', 'storage', 'audio', 'wheel', 'optical', 'disk', 'video', 'ayush'])