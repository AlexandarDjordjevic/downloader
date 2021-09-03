import pycurl
from time import perf_counter

uri1 = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
uri2 = 'https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip'



def progress(total, downloaded, unused1, unused2):
    current_time = perf_counter()
    elapsed_time = 0
    if progress.previous_time > 0:
        elapsed_time = current_time - progress.previous_time
    progress.previous_time = current_time 
    
    new_downloaded = downloaded - progress.previous_downloaded
    progress.previous_downloaded = downloaded
    if elapsed_time > 0 and new_downloaded > 0:
        speed = new_downloaded * 8 / elapsed_time / 1024 / 1024
        print("New downloaded: {}, elapsed time {}, speed is {}".format(new_downloaded, elapsed_time, speed))
    # if total > 0:
        # print("Time {:.2f}mbps, progress: {:.2f}%".format(speed, downloaded/total * 100), end='\r', flush=True)

downloader = pycurl.Curl()
downloader.setopt(downloader.URL, uri1)

downloader.setopt(pycurl.NOPROGRESS, False)
downloader.setopt(pycurl.XFERINFOFUNCTION, progress)
progress.previous_time=0
progress.previous_downloaded = 0
downloader.setopt(pycurl.WRITEFUNCTION, lambda x: None)
t = perf_counter()
downloader.perform()
elapsed_time = perf_counter() - t
file_size = downloader.getinfo(downloader.CONTENT_LENGTH_DOWNLOAD)
print("File size:       {}".format(file_size))
print("Process time:    {}".format(elapsed_time))
print("Download speed:  {:.2f}mb/s".format(file_size * 8 / elapsed_time / 1024 / 1024))
downloader.close()