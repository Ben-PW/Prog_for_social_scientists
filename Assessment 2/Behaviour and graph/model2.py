# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:33:45 2022

@author: u48730bp
"""
########################## MODEL

#import os

#import rasterio

#from os import gdal

#import wind.raster

import csv

import matplotlib.pyplot

#import earthpy.plot as ep

#from collections import Counter

import bacteria_framework

 

#data = rasterio.open('C:/Users/Banjoman/Documents/CDT PhD/Masters/Leeds module/Assessment 2/wind.raster')

#data = gdal.open('C:/Users/Banjoman/Documents/CDT PhD/Masters/Leeds module/Assessment 2/wind.raster')

 

 

environment = []

txt = open('wind.raster', newline = '')

reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)

for row in reader:

    rowlist = [] # define each row in data as a list

    for value in row:

        rowlist.append(value) # append each value in the row to the list

    environment.append(rowlist) # append each list of values to the environment list

txt.close()

 

# Check data import

matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.show()

# y axis is inverted, will be fixed later

 

################################################# Find bombing point

# Find unique value that represents bomb location

vals = {}

for rowlist in environment:

    for i in rowlist:

        if i not in vals:

            vals[i] = 0

        vals[i] += 1

vals

# returns {0.0: 89999, 255.0: 1}, 1 value of 255.0 out of 90000 total values

 

# Find location of outstanding point (255)

def find_bomb(myList, v):

    for i, x in enumerate(myList):

        if v in x:

            return (i, x.index(v))

       

find_bomb(environment, 255) # could make this bit user input from console

# returns (150, 50), location of bomb is y(150), x(50)

 

 

################################# Create agents

 

num_iterations = 200 ### SWITCH THIS FOR A STOPPING CONDITION LATER

num_bacteria = 1000

bacteria = []

#landed = []

   

for i in range(num_bacteria):

    y = 150

    x = 50

    bacteria.append(bacteria_framework.Bacteria(environment, x, y))

 

 

################################ Iterate behaviour

 

for n in range(num_bacteria):

    for i in range(num_iterations): ### SWITCH FOR STOPPING CONDITION LATER

       

        bacteria[i].move()

        bacteria[i].risefall()

       

#b = bacteria_framework.Bacteria(environment, 50, 150)

#print(b.x, b.y)

#b.move()

#print(b.x,b.y)

#print('landed = ', landed)

 

matplotlib.pyplot.xlim(0, 300)

matplotlib.pyplot.ylim(0, 300)

matplotlib.pyplot.imshow(environment)

for i in range(num_bacteria):

    matplotlib.pyplot.scatter(bacteria[i].x,bacteria[i].y)

matplotlib.pyplot.show()

'''

Particle behaviours

- Move: N 10% /S 10% /E 5% /W 75%

- RiseFall: self.h >= 75 (up 20% /level 10% /down 70%), self.h < 75 (down 100%)

- Plot: when self.h == 0, append self.x and self.y to list, terminate behaviour

'''
