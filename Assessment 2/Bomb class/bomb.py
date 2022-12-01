# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:06:27 2022

@author: u48730bp
"""
#import model8

class Bombsquad:
    
    def __init__(self, environment, new):
        
        self.environment = environment
        
        self.vals = {}
        
        self.new = new
        
        
    def find_value (self):
        
        for rowlist in self.environment:
        
            for i in rowlist:
        
                if i not in self.vals: # If integer not detected in self.vals dictionary
        
                    self.vals[i] = 0 # set the recorded number of the vals to zero
        
                self.vals[i] += 1 # Otherwise, add 1 to the existing value
        
                for new_val in self.vals: 
                    
                    if new_val > 0: # find_vals() shows all other values in environment are 0, ideally change this to be less data specific

                        self.new.append(new_val) # Add the value to the 'new' list
                        
                        
    
    def find_bomb (self):
        
        for i, x in enumerate(self.environment):

            if self.new[0] in x: # if the first value in 'new' is found in a row of environment

                return (i, x.index(self.new[0])) # return the index (coordinates) of that value