import subprocess

def install_base():
    subprocess.run(['pacstrap', '/mnt', 'base', 'linux', 'linux-firmware', 'base-devel'])

def install_programs():
    subprocess.run(['pacman', '-Sy', '--noconfirm', 'amd-ucode', 'ntfs-3g', 'grub', 'os-prober', 'lvm2', 'efibootmgr', 'firefox', 'zsh', 'sudo', 'emacs', 'vim', 'nvidia', 'git'])
