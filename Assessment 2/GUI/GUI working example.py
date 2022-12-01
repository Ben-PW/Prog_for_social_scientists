# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:56:39 2022

@author: u48730bp
"""

import numpy as np
import tkinter as tk
import model6 
import matplotlib
matplotlib.use('TkAgg')
import bacteria_framework6
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()

environment = []
model6.readin('wind.raster')

vals = {} # Vals must be defined as a dictionary for find_vals() to work
model6.find_vals(environment)

for new_val in model6.find_vals(environment):     
    if new_val > 0: # find_vals() shows all other values in environment are 0, ideally change this to be less specific    
        new = []
        new.append(new_val) # append the unique value (index) to a separate list to be accessed independently 

num_bacteria = 5000
bacteria = []
landed = []

ycord = model6.find_bomb(environment, new[0])[0] 
xcord = model6.find_bomb(environment, new[0])[1]

for i in range(num_bacteria):

    y = ycord
    x = xcord

    bacteria.append(bacteria_framework6.Bacteria(environment, x, y, i, landed))

while len(landed) < num_bacteria: # Don't stop model until all bacteria have landed
    
    for i in range(num_bacteria): 
           
        bacteria[i].move()
        bacteria[i].risefall()


matplotlib.pyplot.xlim(40, 120)
matplotlib.pyplot.ylim(120, 200)
fig = matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

      
fig = plt.figure(1)
plt.ion()
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

#def update():
#    s = np.cos(np.pi*t)
#    plt.plot(t,s)
    #d[0].set_ydata(s)
#    fig.canvas.draw()

plot_widget.grid(row=0, column=0)
#tk.Button(root,text="Update",command=update).grid(row=1, column=0)
root.mainloop()