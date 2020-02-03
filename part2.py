import src.assets as ass
import src.config as conf
import src.packages as pkg

if __name__ == '__main__':
    conf.time_zone()
    ass.localization()
    pkg.install_programs()
    ass.network()
    ass.mkinitcpio()
    conf.grub()
    conf.user()
