# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 13:00:37 2022

@author: u48730bp
"""

########################## MODEL

import csv

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot

import bacteria_framework7

import time
 
t1 = time.time()

environment = []

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

readin('wind.raster')

t2 = time.time()

print('Environment loaded, time elapsed : ', t2-t1)


# Check data import

# matplotlib.pyplot.imshow(environment)

# matplotlib.pyplot.show()

# y axis is inverted, will be fixed later

 

################################################# Find bombing point

# Find unique value that represents bomb location

vals = {}

def find_vals(e): # Function to find unique values in environment

    for rowlist in e:
    
        for i in rowlist:
    
            if i not in vals:
    
                vals[i] = 0
    
            vals[i] += 1
    
    return vals

find_vals(environment)

for new_val in find_vals(environment): # Extract 
    
    if new_val > 0:
        
        new = []
        new.append(new_val)
    
    

t3 = time.time()

print('Bomb value found, time elapsed : ', t3-t2)
 


def find_bomb(myList, v): # Function to find location of outstanding point

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v)) # Returns index of value, x and y can be accessed from this via [] operators
        
ycord = find_bomb(environment, new[0])[0] # assign coordinates here to prevent having to iterate loop over all bacteria when appending
xcord = find_bomb(environment, new[0])[1]

       
t4 = time.time()
print('Bomb location found, time elapsed : ', t4-t3)

#find_bomb(environment, 255) # could make this bit user input from console

# returns (150, 50), location of bomb is y(150), x(50)

#find_bomb(environment, 255)[1]

 

################################# Create agents

 

#num_iterations = 200 ### SWITCH THIS FOR A STOPPING CONDITION LATER

num_bacteria = 5000

bacteria = []

landed = []


for i in range(num_bacteria):

    y = ycord

    x = xcord

    bacteria.append(bacteria_framework7.Bacteria(environment, x, y, i, landed))

t5 = time.time()
print(num_bacteria, 'bacteria generated, time elapsed : ', t5-t4)

 

################################ Iterate behaviour

 
while len(landed) < num_bacteria:
    #for n in range(num_iterations):
    
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

matplotlib.pyplot.xlim(0, 300)

matplotlib.pyplot.ylim(0, 300)

#matplotlib.pyplot(50, 150, marker='o', markersize=20, markeredgecolor='red')

matplotlib.pyplot.imshow(environment)

#for i in range(num_bacteria):

   #matplotlib.pyplot.scatter(bacteria[i].x,bacteria[i].y)

matplotlib.pyplot.show()

t7 = time.time()
print('Plotting complete, time elapsed : ', t7-t6)
print('Total time elapsed : ', t7-t1)

import numpy as np
import matplotlib.pyplot 
  
#data = environment
#matplotlib.pyplot.imshow( data , cmap = 'autumn' , interpolation = 'nearest' )
  
#matplotlib.pyplot.title( "2-D Heat Map" )
#matplotlib.pyplot.show()

 
# set seaborn style
#sns.set_style("white")

# Basic 2D density plot
#sns.kdeplot(x=environment.x, y=environment.y)
#plt.show()

def readout():
    
    with open('out.txt', 'w', newline='') as f:
    
        writer = csv.writer(f, delimiter=',')
        
        for row in environment:
            
            writer.writerow(row) # List of values.
            
        
readout()
'''

Particle behaviours

- Move: N 10% /S 10% /E 5% /W 75%

- RiseFall: self.h >= 75 (up 20% /level 10% /down 70%), self.h < 75 (down 100%)

- Plot: when self.h == 0, append self.x and self.y to list, terminate behaviour

'''