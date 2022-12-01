# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:57:23 2022

@author: u48730bp
"""

import csv

class Readwrite:
    
    
    def __init__(self, a, environment):
        
        self.a = a
        
        self.environment = environment
        
        
    def readin(self):

        txt = open(self.a, newline = '')
        
        reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC)
        
        for row in reader:
        
            rowlist = [] # define each row in data as a list
        
            for value in row:
        
                rowlist.append(value) # append each value in the row to the list
        
            self.environment.append(rowlist) # append each list of values to the environment list
        
        txt.close()
        
        
    def readout(self):
        
        with open('out.txt', 'w', newline='') as f:
        
            writer = csv.writer(f, delimiter=',')
            
            for row in self.environment:
                
                writer.writerow(row) 
        