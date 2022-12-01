# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:20:53 2022

@author: u48730bp
"""

import matplotlib
#matplotlib.use('Agg')
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import csv
import bacteria_framework7
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

################################## Functions


# Function to generate frames of animation
def update (frame_number):
    
    fig.clear()
    
        
    for i in range(num_bacteria): 
        
               
        bacteria[i].move()
        
        bacteria[i].risefall()
            
        
    matplotlib.pyplot.xlim(40, 120)

    matplotlib.pyplot.ylim(120, 200)

        #matplotlib.pyplot(50, 150, marker='o', markersize=20, markeredgecolor='red')

    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_bacteria):
        matplotlib.pyplot.scatter(bacteria[i].x,bacteria[i].y)
    
   
        
    
# Function to determine number of frames animated 
def gen_func(b = [0]):
    a = 0
       
    while len(landed) < num_bacteria: # Yield frames until all bacteria have landed
        yield a			# Returns control and waits next call.
        a = a + 1
        


# Function to run amination
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_func, repeat=False)
    canvas.draw()


# Function to read in environment data
def readin(a):

    txt = open(a, newline = '')
    
    reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
    
    with txt:
    
        for row in reader:
        
            rowlist = [] # define each row in data as a list
        
            for value in row:
        
                rowlist.append(value) # append each value in the row to the list
        
            environment.append(rowlist) # append each list of values to the environment list
        
        #txt.close()


# Function to find specific value of bomb location
def find_vals(e): # Function to find unique values in environment

    for rowlist in e:
    
        for i in rowlist:
    
            if i not in vals:
    
                vals[i] = 0
    
            vals[i] += 1
    
    return vals


# Function to find index of value found by find_vals()
def find_bomb(myList, v): 

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v))
        
        
####################################### Script begins
    
num_bacteria = 500

bacteria = []

landed = []

environment = []

vals = {}



readin('wind.raster')



find_vals(environment)

for new_val in find_vals(environment): # Extract 
    
    if new_val > 0:
        
        new = []
        new.append(new_val)
        

        
ycord = find_bomb(environment, new[0])[0] # assign coordinates here to prevent having to iterate loop over all bacteria when appending
xcord = find_bomb(environment, new[0])[1]

for i in range(num_bacteria):

    y = ycord

    x = xcord

    bacteria.append(bacteria_framework7.Bacteria(environment, x, y, i, landed))
    
        
fig = matplotlib.pyplot.figure(figsize=(300, 300))
#fig = Figure()
ax = fig.add_axes([0, 0, 1, 1])

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)


# Create base GUI
root = tkinter.Tk()


# Title GUI = 'Model'
root.wm_title("Model")

# Configure GUI to use raster data plot as element of GUI
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) #, master=root)
#canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(animation, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Add menu element to GUI
menu_bar = tkinter.Menu(root)

# Configure menu element to be menu bar
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)

# Configure menu to cascade options 
menu_bar.add_cascade(label="Model", menu=model_menu)

# Cascading option gives 'Run model' prompt, tied to run()
model_menu.add_command(label="Run model", command=run)

#def gen_function() -> obj 
#root = tkinter.Tk()


tkinter.mainloop()
