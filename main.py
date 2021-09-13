from Downloader import *
from Plot import *


uri1 = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
uri2 = 'https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip'
uri100Mb = 'https://speed.hetzner.de/100MB.bin'

#http://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps_3840x2160_12000k/bbb_30fps_3840x2160_12000k_0.m4v
#http://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps_320x180_200k/bbb_30fps_320x180_200k.m4v

class StreamRepresentation:
    def __init__(self, url_base, url_append, chunk_name, chunk_extension, chunk_number):
        self.name = chunk_name
        self.fragments = list()
        for i in range (1, chunk_number):
            self.fragments.append("{}{}{}{}.{}".format(url_base, url_append, chunk_name, i, chunk_extension))


#url_dash.append('http://rdmedia.bbc.co.uk/dash/ondemand/bbb/2/avc3/1920x1080p25/{:06}.m4s'.format(id))

if __name__ == '__main__':
    stream_list = list()
    stream_list.append(StreamRepresentation('http://dash.akamaized.net/akamai/bbb_30fps/', 'bbb_30fps_3840x2160_12000k/', 'bbb_30fps_3840x2160_12000k_', 'm4v', 160))
    stream_list.append(StreamRepresentation('http://dash.akamaized.net/akamai/bbb_30fps/', 'bbb_30fps_320x180_200k/', 'bbb_30fps_320x180_200k_', 'm4v', 160))
    
    for stream in stream_list:
        plot = Plot(y_limit = 80)
        downloader = Downloader(stream.fragments, plot.insert, plot.exit, False, csv_file_name=stream.name)
        downloader.start()
        plot.draw()
    input("Press enter to exit!")