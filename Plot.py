import matplotlib
import matplotlib.pyplot as plt
from threading import Thread, Lock
import time
import numpy as np

class Plot():
    def __init__(self, y_limit = 100, max_number_of_items = 0):
        plt.ion()
        self.y_limit = y_limit
        self.fig, self.x1 = plt.subplots()
        self.number_of_items = 0
        self.max_number_of_items = max_number_of_items
        self.x = list()
        self.y = list()
        self.run = True

    def insert(self, value):
        if self.max_number_of_items != 0 and self.number_of_items >= self.max_number_of_items - 1 :
            self.x.pop(0)
            self.y.pop(0)
        self.number_of_items += 1
        self.x.append(self.number_of_items)
        self.y.append(value)
    
    def exit(self):
        self.run = False
    
    def draw(self):
        while self.run:
            self.x1.cla()
            # plt.yscale('linear')
            plt.ylim([0, self.y_limit])
            self.x1.plot(self.x, self.y);
            plt.pause(0.01)
        plt.show()



    