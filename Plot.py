import matplotlib
import matplotlib.pyplot as plt
from threading import Thread, Lock
import time
import numpy as np
from datetime import datetime

class Plot():
    def __init__(self, y_limit = 100, max_number_of_items = 0, output_file = None):
        plt.ion()
        self.y_limit = y_limit
        self.fig, self.x1 = plt.subplots()
        self.number_of_items = 0
        self.max_number_of_items = max_number_of_items
        self.x = list()
        self.y = list()
        self.run = True
        self.output_file = output_file
        if output_file != None:
            self.output_file += datetime.now().strftime("%d%m%y_%H%M%S") + ".png"
        self.lock = Lock()
        
    def insert(self, value):
        self.lock.acquire(True)
        if self.max_number_of_items != 0 and self.number_of_items >= self.max_number_of_items - 1 :
            self.x.pop(0)
            self.y.pop(0)
        self.number_of_items += 1
        self.x.append(self.number_of_items)
        self.y.append(value)
        self.lock.release()
    
    def exit(self):
        if self.output_file != None :
            plt.savefig(self.output_file, format="png")
            print("Saving file {}".format(self.output_file))
        self.run = False
    
    def draw(self):
        while self.run:
            self.lock.acquire(True)
            self.x1.cla()
            # plt.yscale('linear')
            plt.ylim([0, self.y_limit])
            self.x1.plot(self.x, self.y)
            self.lock.release()
            plt.pause(0.001)
            plt.show()



    