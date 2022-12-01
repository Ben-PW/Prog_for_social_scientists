# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:26 2022

@author: u48730bp
"""

########################## MODEL

import matplotlib.pyplot

import bacteria_framework6

import time

import readwrite

#import bomb

import pandas

##################################################################### FUNCTIONS


# Function to find unique value in environment
def find_vals(e): # Function to find unique values in environment

    for rowlist in e:
    
        for i in rowlist:
    
            if i not in vals:
    
                vals[i] = 0
    
            vals[i] += 1
            
    return vals
    


# Function to find index of unique value in environment
def find_bomb(myList, v): # Function to find location of outstanding point

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v)) # Returns index of value, x and y can be accessed from this via [] operators


   
############################################################## END OF FUNCTIONS

t1 = time.time()

a = 'wind.raster'
environment = []

reader = readwrite.Readwrite(a, environment)
reader.readin()

t2 = time.time()

print('Environment loaded, time elapsed : ', t2-t1)


# Check data import

# matplotlib.pyplot.imshow(environment)

# matplotlib.pyplot.show()


################################################# Find bombing point

# Find unique value that represents bomb location

vals = {} # Vals must be defined as a dictionary for find_vals() to work
find_vals(environment)
#bombsquad = bomb.Bombsquad(environment, v)

t3 = time.time()
print('Bomb value found, time elapsed : ', t3-t2)


for new_val in find_vals(environment): 
    
    if new_val > 0: # find_vals() shows all other values in environment are 0, ideally change this to be less specific
        
        new = []
        new.append(new_val) # append the unique value (index) to a separate list to be accessed independently 
   
t4 = time.time()
print('Bomb location found, time elapsed : ', t4-t3)  

 

################################# Create agents

num_bacteria = 5000

bacteria = []

landed = []

ycord = find_bomb(environment, new[0])[0] # access first value of first entry in 'new' list (y coordinate of index)
xcord = find_bomb(environment, new[0])[1] # access second value of first entry in 'new' list (x coordinate of index)
                                          # assign now instead of having to iterate loop num_bacteria times

for i in range(num_bacteria):

    y = ycord

    x = xcord

    bacteria.append(bacteria_framework6.Bacteria(environment, x, y, i, landed))

t5 = time.time()
print(num_bacteria, 'bacteria generated, time elapsed : ', t5-t4)

 

################################ Iterate behaviour

 
while len(landed) < num_bacteria: # Don't stop model until all bacteria have landed
    
    for i in range(num_bacteria): 
    
           
        bacteria[i].move()
    
        bacteria[i].risefall()


t6 = time.time()
print('Movement simulated, time elapsed : ', t6-t5)
###################### Checks

#b = bacteria_framework.Bacteria(environment, 50, 150) # Check move() and risefall() functions
#print(b.x, b.y)
#b.move()
#print(b.x,b.y)
#b.risefall()
#print(b.x,b.y)

#print('landed = ', landed) # Check descending behaviour

#print('Number of bacteria that have landed is:',len(landed)) # Check expected numbers are landing

#find_vals(environment) # Check numbers of bacteria falling in locations are being recorded

#################### Create density plot

matplotlib.pyplot.xlim(40, 120)

matplotlib.pyplot.ylim(120, 200)

matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.show()


t7 = time.time()
print('Plotting complete, time elapsed : ', t7-t6)
print('Total time elapsed : ', t7-t1)


reader.readout()
