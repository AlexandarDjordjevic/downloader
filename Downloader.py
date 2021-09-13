import sys
import pycurl
from time import perf_counter
from threading import Thread
from datetime import datetime

class Downloader(Thread):
    on_progress = None
    on_finished = None
    def __init__(self, uri, on_progress = None, on_finished = None, notify_progress = False, csv_file_name = None) :
        self.uri = uri
        self.file_size = 0
        self.handler = pycurl.Curl()
        self.on_finished = on_finished
        self.on_progress = on_progress
        self.notify_progress = notify_progress
        self.csv_file_name = csv_file_name
        if csv_file_name != None:
            self.csv_file_name += datetime.now().strftime("_%d%m%y_%H%M%S") + ".csv"
        Thread.__init__(self)

    def download(self, uri):
        self.total_download_time = 0
        self.total_downloaded = 0
        self.handler.setopt(pycurl.URL, uri)
        self.handler.setopt(pycurl.NOPROGRESS, False)
        self.handler.setopt(pycurl.XFERINFOFUNCTION, self.progress)
        self.handler.setopt(pycurl.WRITEFUNCTION, lambda x: None)
        self.start_time = perf_counter()
        self.handler.perform()

    def run(self):
        for uri in self.uri:
            print("-------------------------------------------")
            print("Downloading URI: {}".format(uri))
            self.download(uri)
            self.print_result()
        self.handler.close()
        if self.on_finished :
            self.on_finished()
        
    def progress(self, total, downloaded, unused1, unused2):
        self.total_download_time = perf_counter() - self.start_time
        self.total_downloaded = downloaded
        if total > 0 :
            download_speed = self.total_downloaded * 8 / self.total_download_time / 1024 / 1024
            if self.notify_progress:
                sys.stdout.write("\033[K")
                print("Downloading: {:.2f}%, {:.2f}Mbps".format(downloaded / total * 100 , download_speed))
            if self.on_progress :
                self.on_progress(download_speed)

    def set_on_progress(self, on_progress):
        self.on_progress = on_progress
        
    def set_on_finished(self, on_finished):
        self.on_finished = on_finished
        
    def print_result(self):
        download_speed = self.total_downloaded * 8 / self.total_download_time / 1024 / 1024
        print("Download finished: ")
        print("File size:\t{:.2f}Mb".format(self.total_downloaded / 1024 / 1024))
        print("Duration:\t{:.2f}s".format(self.total_download_time))
        print("Speed:\t\t{:.2f}Mbps".format(download_speed))
        print("-------------------------------------------")
        if self.csv_file_name != None :
            with open(self.csv_file_name, "a") as file :
                file.write("{},{}\n".format(self.total_downloaded, self.total_download_time * 1000000000))
