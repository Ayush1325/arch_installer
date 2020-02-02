import src.partitions as par
import src.assets as ass
import src.packages as pkg

if __name__ == '__main__':
    par.format_all()
    par.swap_space()
    par.mount_all()

    ass.copy_mirrors()

    pkg.install_base()

    ass.copy_fstab()

    ass.copy_project()

    par.chroot()