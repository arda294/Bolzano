from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import time
from threading import *

class Plot:
    def __init__(self):
        self.figure = Figure(figsize=(10,10), dpi=100)
        self.plot1 = self.figure.add_subplot(111)
        self.start = 3
        self.end = 5
        self.prec = 10
        self.x = np.linspace(self.start,self.end)
        self.y = self.expression(self.x)
        self.plot1.plot(self.x,self.y)
    
    def is_acc(self, num, prec=2):
        return (10**(-prec)) > abs(num)
    
    def sign(self, num):
        return 1 if num > 0 else -1
    
    def expression(self, num):
        return num**3 - 100
    
    def draw_plot(self, start, end, xmid, ymid, iteration):
        x = np.linspace(start, end)
        y = self.expression(x)
        self.plot1.cla()
        self.plot1.plot(x,y)
        self.plot1.text((xmid), ((self.expression(xmid))/2), f' Difference : {-self.expression(xmid)}\n Error : {abs(self.expression(xmid)):%}')
        self.plot1.plot([xmid,xmid], [0,self.expression(xmid)])
        self.plot1.plot(xmid,ymid,'go',label='Mid Point')
        self.plot1.legend()
        
        self.plot1.set_title(f'Iteration No : {iteration}')
        canvas.draw()
        canvas.get_tk_widget().pack()
    
    def solver(self, x1, x2, prec=2):
        plot_button['state'] = DISABLED
        i = 1
        y1 = self.expression(x1)
        y2 = self.expression(x2)
        xmid = (x1+x2)/2
        ymid = self.expression(xmid)
        self.draw_plot(x1, x2, xmid, 0, i)

        while not self.is_acc(ymid, prec):
            if self.sign(ymid) == self.sign(y1):
                x1 = xmid
            else:
                x2 = xmid
            y1 = self.expression(x1)
            y2 = self.expression(x2)
            xmid = (x1+x2)/2
            ymid = self.expression(xmid)
            print(f'{i} {x1} {xmid} {x2} {ymid}')
            self.draw_plot(x1, x2, xmid, 0, i)
            time.sleep(1)
            i += 1
        # plt.show()
        plot_button['state'] = NORMAL
    
    def solve(self):
        Thread(target= lambda: self.solver(self.start, self.end, self.prec)).start()
    

def window_setup(Plot_obj):
    window = Tk()
    window.title('Praktikum 1 Bolzano')
    window.geometry("720x720")
    plot_button = Button(master=window,
                        command=lambda: Plot_obj.solve(),
                        height=2,
                        width=10,
                        text='Start')
    plot_button.pack()
    canvas = FigureCanvasTkAgg(Plot_obj.figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return window, canvas, plot_button


def solve(Plot_obj):
    pass

if __name__ == '__main__':
    plot_obj = Plot()
    window, canvas, plot_button = window_setup(plot_obj);
    window.mainloop()
   
    
    
    
