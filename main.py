from Downloader import *
from Plot import *


uri1 = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
uri2 = 'https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip'
uri100Mb = 'https://speed.hetzner.de/100MB.bin'



if __name__ == '__main__':
    plot = Plot(y_limit = 50)
    downloader = Downloader(uri100Mb, plot.insert, plot.exit, True)
    downloader.start()
    plot.draw()