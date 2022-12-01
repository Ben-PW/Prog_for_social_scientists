# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:44 2022

@author: u48730bp
"""

############################### BACTERIA FRAMEWORK

import random

 

class Bacteria():

    def __init__(self, environment, x, y, i, landed):

        self.x = x

        self.y = y

        self.environment = environment

        self.height = 75
        
        self.i = i
        
        self.landed = landed

       

    def move(self):
        
        if self.height > 0: # If height is above zero

        #rand = random.random()

            if random.random() <= 0.1: # 10% chance to move North
    
                self.y = (self.y + 1) % 300
    
                #print('y+1')
    
            elif random.random() > 0.1 and random.random() <= 0.2: # 10% chance to move South
    
                self.y = (self.y - 1) % 300
    
                #print('y-1')
    
            elif random.random() > 0.2 and random.random() <= 0.95: # 75% chance to move East
    
                self.x = (self.x + 1) % 300
    
                #print('x+1')
    
            else:
    
                self.x = (self.x - 1) % 300 # 5% chance to move West
    
                #print('x-1')

        else:
            pass # If height not above zero, don't move

                

    def risefall(self):

        if self.height > 0: # If height of bacteria is above ground

            if self.height >= 75: # If height is equal/greater than 75

                if random.random() <= 0.2: # 20% chance to increase height

                    self.height = (self.height + 1)
                    #print('rising')

                elif random.random() > 0.2 and random.random() <= 0.3: # 10% chance to stay level

                    pass

                else:

                    self.height = (self.height - 1) # Otherwise height will reduce by 1
                    #print('falling (75+)')

            else:

                    self.height = (self.height - 1) # If height is sub 75, reduce height by 1
                    #print('falling (75-')

        else:

            seen = set(self.landed) # If height is not greater than 0, add to list of landed bacteria
            
            if self.i not in seen:

                self.landed.append(self.i) # Only add to landed list if it is not already in the list
                
                self.environment[self.y][self.x] += 15 # New arrivals add to local value, 15 selected as seems to visualise well
                #print('storing location')
            
            else:
                pass

            #print('Bacteria landed')
