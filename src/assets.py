from shutil import copyfile, copytree
import subprocess

def copy_mirrors():
    copyfile('assets/mirrorlist', '/etc/pacman.d/mirrorlist')

def copy_fstab():
    copyfile('assets/fstab', '/mnt/etc/fstab')

def copy_project():
    copytree('~/arch-installer', '/mnt/arch-installer')

def localization():
    copyfile('assets/locale.gen', '/etc/locale.gen')
    copyfile('assets/locale.conf', '/etc/locale.conf')
    subprocess.run(['source', '/etc/locale.conf'])
    subprocess.run(['locale-gen'])

def network():
    copyfile('assets/hosts', '/etc/hosts')
    copyfile('assets/hostname', '/etc/hostname')

def mkinitcpio():
    copyfile('assets/mkinitcpio.conf', '/etc/mkinitcpio.conf')
    subprocess.run(['mkinitcpio', '-P'])