# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:53:44 2022

@author: u48730bp
"""

########################## MODEL

import csv

import matplotlib.pyplot

import bacteria_framework5

import readwrite

 
 
#Readwrite = []
environment = []
a = 'wind.raster'

reader = readwrite.Readwrite(a, environment)
#Readwrite.append(readwrite.Readwrite(a, environment))
reader.readin()
'''
def readin(a):

    txt = open(a, newline = '')
    
    reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
    
    for row in reader:
    
        rowlist = [] # define each row in data as a list
    
        for value in row:
    
            rowlist.append(value) # append each value in the row to the list
    
        environment.append(rowlist) # append each list of values to the environment list
    
    txt.close()

readin('wind.raster')
'''
# Check data import

matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.show()

# y axis is inverted, will be fixed later

 

################################################# Find bombing point

# Find unique value that represents bomb location

vals = {}

def find_vals(e):

    for rowlist in e:
    
        for i in rowlist:
    
            if i not in vals:
    
                vals[i] = 0
    
            vals[i] += 1
    
    return vals

find_vals(environment)

# returns {0.0: 89999, 255.0: 1}, 1 value of 255.0 out of 90000 total values

 

# Find location of outstanding point (255)

def find_bomb(myList, v):

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v))

       

find_bomb(environment, 255) # could make this bit user input from console

# returns (150, 50), location of bomb is y(150), x(50)

 

 

################################# Create agents

 

#num_iterations = 200 ### SWITCH THIS FOR A STOPPING CONDITION LATER

num_bacteria = 5000

bacteria = []

landed = []


for i in range(num_bacteria):

    y = 150

    x = 50

    bacteria.append(bacteria_framework5.Bacteria(environment, x, y, i, landed))

 

 

################################ Iterate behaviour

 
while len(landed) < num_bacteria:
    #for n in range(num_iterations):
    
    for i in range(num_bacteria): 
    
           
        bacteria[i].move()
    
        bacteria[i].risefall()

       
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

#matplotlib.pyplot(50, 150, marker='o', markersize=20, markeredgecolor='red')

matplotlib.pyplot.imshow(environment)

#for i in range(num_bacteria):

   #matplotlib.pyplot.scatter(bacteria[i].x,bacteria[i].y)

matplotlib.pyplot.show()

reader.readout()

'''

Particle behaviours

- Move: N 10% /S 10% /E 5% /W 75%

- RiseFall: self.h >= 75 (up 20% /level 10% /down 70%), self.h < 75 (down 100%)

- Plot: when self.h == 0, append self.x and self.y to list, terminate behaviour

'''