# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:26 2022

@author: u48730bp
"""

########################## MODEL

import matplotlib.pyplot

import bacteria_framework8

import time

import bomb

import readwrite

######################### Create classes

# Create reader class - used to read environment files in and out
a = 'wind.raster'
environment = [] # Will contain data representing environment

reader = readwrite.Readwrite(a, environment)

# Create bombsquad class - used to find value and location of bomb point
new = [] # Will contain the numerical value of the unique value (representing bombing point)

bombsquad = bomb.Bombsquad(environment, new)


######################### Load environment

t1 = time.time()

reader.readin()

t2 = time.time()

print('Environment loaded, time elapsed : ', t2-t1)


######################### Find numerical value of bombing point

bombsquad.find_value()

t3 = time.time()
print('Bomb value found, time elapsed : ', t3-t2)

   
######################### Create agents

num_bacteria = 5000

bacteria = [] # create list to store generated agents

landed = [] # create list to store number of landed bacteria

ycord = bombsquad.find_bomb()[0] # access first value of first entry in 'new' list (y coordinate of index)
xcord = bombsquad.find_bomb()[1] # access second value of first entry in 'new' list (x coordinate of index)
                                       # assign now instead of having to iterate loop num_bacteria times
t4 = time.time()
print('Bomb location found, time elapsed : ', t4-t3)  


for i in range(num_bacteria): # append required values to the bacteria agents

    y = ycord

    x = xcord

    bacteria.append(bacteria_framework8.Bacteria(environment, x, y, i, landed))

t5 = time.time()
print(num_bacteria, 'bacteria generated, time elapsed : ', t5-t4)

 

################################ Iterate behaviour

 
while len(landed) < num_bacteria: # Don't stop model until all bacteria have landed
    
    for i in range(num_bacteria): 
    
           
        bacteria[i].move() # Iterate horizontal movement
    
        bacteria[i].risefall() # Vertical movement and landing


t6 = time.time()
print('Movement simulated, time elapsed : ', t6-t5)



#################### Create density plot

matplotlib.pyplot.xlim(40, 120)

matplotlib.pyplot.ylim(120, 200)

matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.show()


t7 = time.time()
print('Plotting complete, time elapsed : ', t7-t6)
print('Total time elapsed : ', t7-t1)


reader.readout() # Create export environment
