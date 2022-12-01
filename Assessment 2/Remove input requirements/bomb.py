# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:06:27 2022

@author: u48730bp
"""

class Bombsquad:
    
    def __init__(self, environment, v):
        
        self.environment = environment
        
        self.vals = {}
        
        self.v = v
        
        
    def find_value (self):
        
        for rowlist in self.environment:
        
            for i in rowlist:
        
                if i not in self.vals:
        
                    self.vals[i] = 0
        
                self.vals[i] += 1
        
        return self.vals
    
    def find_bomb (self):
        
        for i, x in enumerate(self.environment):

            if self.v in x:

                return (i, x.index(self.v))