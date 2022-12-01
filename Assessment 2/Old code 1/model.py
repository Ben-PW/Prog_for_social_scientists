# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

####################### MODEL ##############################

"""

Created on Mon Sep 12 10:09:33 2022

 

@author: Banjoman

"""

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

 

'''  Unsuccessful attempts

#####                                  

m = {}

for rowlist in environment:

    n = {}

    for i in rowlist:

        n[i] = n.get(i, 0) + 1

    m[i] = m.get(i, 0) + 1

 

#####

def count_elements(seq):

     n = {}

     for i in seq:

         n[i] = n.get(i, 0) + 1

     return n

 

for rowlist in environment:

    for i in rowlist:

        count_elements(rowlist)

 

print(n)

'''  

 

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

 

num_bacteria = 5000

bacteria = []

   

for i in range(num_bacteria):

    y = 150

    x = 50

    bacteria.append(environment, x, y)

 

'''

Particle behaviours

- Move: N 10% /S 10% /E 5% /W 75%

- RiseFall: self.h >= 75 (up 20% /level 10% /down 70%), self.h < 75 (down 100%)

- Plot: when self.h == 0, append self.x and self.y to list, terminate behaviour

'''